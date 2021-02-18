/*
 *********************************************************************************
 * Author: Uriel Martinez-Hernandez
 * Email: u.martinez@bath.ac.uk
 * Date: 5-February-2021
 *
 * University of Bath
 * Multimodal Interaction and Robotic Active Perception (inte-R-action) Lab
 * Centre for Autonomous Robotics (CENTAUR)
 * Department of Electronics and Electrical Engineering
 *
 * Description:
 *
 *********************************************************************************
 */

#include <moveit/move_group_interface/move_group_interface.h>
#include <moveit/planning_scene_interface/planning_scene_interface.h>
#include <moveit_msgs/DisplayRobotState.h>
#include <moveit_msgs/DisplayTrajectory.h>
#include <moveit_msgs/AttachedCollisionObject.h>
#include <moveit_msgs/CollisionObject.h>
#include <moveit_visual_tools/moveit_visual_tools.h>
#include <moveit/trajectory_processing/iterative_time_parameterization.h>
#include "std_msgs/String.h"
#include <iostream>
#include <unistd.h>
#include <map>
#include <sstream>

using namespace std;

string objectString = "";
bool robotMove = false;
string gripper_state = "";
namespace rvt = rviz_visual_tools;

void robotMoveCallback(const std_msgs::String::ConstPtr& msg)
{
//  ROS_INFO("I heard: [%s]", msg->data);
 
 	objectString.clear();

    objectString = msg->data; 

    cout << "Robot move: " << robotMove << endl; 
    cout << "Object: " << objectString << endl;
}

void gripperStatusCallback(const std_msgs::String::ConstPtr& msg)
{
//  ROS_INFO("I heard: [%s]", msg->data);
 
    gripper_state.clear();

    gripper_state = msg->data; 

    cout << "Gripper State: " << gripper_state << endl;
}

// Map high level position to joint angles as seen on teach pendant
// Order is: shoulder_pan_joint, shoulder_lift_joint, elbow_joint, wrist_1_joint, wrist_2_joint, wrist_3_joint
struct jnt_angs{double angles[6];};
std::map<std::string, jnt_angs> create_joint_pos(){
    std::map<std::string, jnt_angs> joint_positions;
    joint_positions["home"] = {-11.75, -83.80, 47.90, -125.0, -90.0, 354.1};
    joint_positions["bring_side_1"] = {-48.10, -62.90, 40.2, -68.6, -89.8, 354.1};
    joint_positions["bring_side_2"] = {-25.4, -62.90, 40.2, -68.6, -89.8, 354.1};
    joint_positions["bring_side_3"] = {-8.5, -62.90, 40.2, -68.6, -89.8, 354.1};
    joint_positions["bring_side_4"] = {12.9, -62.90, 40.2, -68.6, -89.8, 354.1};
    joint_positions["take_box"] = {79.9, -62.90, 40.2, -68.6, -89.8, 354.1};
    joint_positions["deliver_2_user"] = {56.9, -62.90, 40.2, -68.6, -89.8, 354.1};
    joint_positions["deliver_box"] = {-150.0, -62.90, 40.2, -68.6, -89.8, 354.1};
    return joint_positions;
};

class moveit_robot {
    public:
        // Setup
        // MoveIt! operates on sets of joints called "planning groups" and stores them in an object called
        // the `JointModelGroup`. Throughout MoveIt! the terms "planning group" and "joint model group"
        // are used interchangably.
        const std::string PLANNING_GROUP;

        // The :move_group_interface:`MoveGroup` class can be easily
        // setup using just the name of the planning group you would like to control and plan for.
        moveit::planning_interface::MoveGroupInterface move_group;

        // We will use the :planning_interface:`PlanningSceneInterface`
        // class to add and remove collision objects in our "virtual world" scene
        moveit::planning_interface::PlanningSceneInterface planning_scene_interface;

        const robot_state::JointModelGroup* joint_model_group;

        // Now, we call the planner to compute the plan and visualize it.
        // The plan variable contains the movements that the robot will perform to move
        // from one point to another
        moveit::planning_interface::MoveGroupInterface::Plan plan;

        moveit::core::RobotStatePtr current_state;
        std::vector<double> joint_group_positions;

        // Visualization
        // The package MoveItVisualTools provides many capabilties for visualizing objects, robots,
        // and trajectories in RViz as well as debugging tools such as step-by-step introspection of a script
        moveit_visual_tools::MoveItVisualTools visual_tools;
        Eigen::Isometry3d text_pose;

        // Gripper message, cmd publisher and status subscriber
        std_msgs::String  gripper_msg;
        ros::Publisher gripper_cmds_pub;
        ros::Subscriber gripper_feedback_sub;

        moveit_robot(ros::NodeHandle* node_handle);
        void move_robot(std::map<std::string, double> targetJoints);
        void open_gripper();
        void close_gripper();
        void z_move(double dist);
    
    private:
        ros::NodeHandle nh_; // we will need this, to pass between "main" and constructor

};

moveit_robot::moveit_robot(ros::NodeHandle* node_handle) : nh_(*node_handle), PLANNING_GROUP("manipulator"), visual_tools("world"), move_group(moveit::planning_interface::MoveGroupInterface(PLANNING_GROUP)) {

    // Raw pointers are frequently used to refer to the planning group for improved performance.
    const robot_state::JointModelGroup* joint_model_group = move_group.getCurrentState()->getJointModelGroup(PLANNING_GROUP);

    visual_tools.deleteAllMarkers();

    // Remote control is an introspection tool that allows users to step through a high level script
    // via buttons and keyboard shortcuts in RViz
    visual_tools.loadRemoteControl();

    // RViz provides many types of markers, in this demo we will use text, cylinders, and spheres
//    Eigen::Affine3d text_pose = Eigen::Affine3d::Identity();
    //Eigen::Isometry3d 
    text_pose = Eigen::Isometry3d::Identity();
    text_pose.translation().z() = 1.75;
    visual_tools.publishText(text_pose, "HRI Static Demo - v 0.1.0", rvt::WHITE, rvt::XLARGE);

    // Batch publishing is used to reduce the number of messages being sent to RViz for large visualizations
    visual_tools.trigger();

    // Getting Basic Information
    // 
    // We can print the name of the reference frame for this robot.
    ROS_INFO_NAMED("UR3 robot", "Reference frame: %s", move_group.getPlanningFrame().c_str());

    // We can also print the name of the end-effector link for this group.
    ROS_INFO_NAMED("UR3 robot", "End effector link: %s", move_group.getEndEffectorLink().c_str());

    // We can get a list of all the groups in the robot:
    ROS_INFO_NAMED("tutorial", "Available Planning Groups:");
    std::copy(move_group.getJointModelGroupNames().begin(), move_group.getJointModelGroupNames().end(),
            std::ostream_iterator<std::string>(std::cout, ", "));


    // Now, we call the planner to compute the plan and visualize it.
    // The plan variable contains the movements that the robot will perform to move
    // from one point to another
    //moveit::planning_interface::MoveGroupInterface::Plan plan;

    // To start, we'll create an pointer that references the current robot's state.
    // RobotState is the object that contains all the current position/velocity/acceleration data.
    moveit::core::RobotStatePtr current_state = move_group.getCurrentState();

    // Next get the current set of joint values for the group.
    std::vector<double> joint_group_positions;
    current_state->copyJointGroupPositions(joint_model_group, joint_group_positions);

    // We lower the allowed maximum velocity and acceleration to 5% of their maximum.
    // The default values are 10% (0.1).
    // Set your preferred defaults in the joint_limits.yaml file of your robot's moveit_config
    // or set explicit factors in your code if you need your robot to move faster.
    move_group.setMaxVelocityScalingFactor(0.10);
    move_group.setMaxAccelerationScalingFactor(0.10);

    gripper_cmds_pub = nh_.advertise<std_msgs::String>("UR2Gripper", 1);
    gripper_feedback_sub = nh_.subscribe("Gripper2UR", 1, gripperStatusCallback);
}

void moveit_robot::move_robot(std::map<std::string, double> targetJoints){

    move_group.setStartState(*move_group.getCurrentState());

    move_group.setJointValueTarget(targetJoints);

    bool success = (move_group.plan(plan) == moveit::planning_interface::MoveItErrorCode::SUCCESS);
    ROS_INFO("Visualizing new move position plan (%.2f%% acheived)",success * 100.0);

    move_group.execute(plan);
}

void moveit_robot::open_gripper(){
    // Open Gripper
    gripper_msg.data = "release";
    while (gripper_state != "release_completed")
    {
        gripper_cmds_pub.publish(gripper_msg);
    }
    gripper_msg.data = "completion acknowledged";
    gripper_cmds_pub.publish(gripper_msg);
}

void moveit_robot::close_gripper(){
    // Close Gripper
    gripper_msg.data = "grasp";
    while (gripper_state != "grasp_completed")
    {
        gripper_cmds_pub.publish(gripper_msg);
    }
    gripper_msg.data = "completion acknowledged";
    gripper_cmds_pub.publish(gripper_msg);
}

void moveit_robot::z_move(double dist){
    //--Cartesian movement planning for straight down movement--//
    // dist is -ve down, +ve up in m

    geometry_msgs::Pose target_home = move_group.getCurrentPose().pose;

    geometry_msgs::Pose homeZPosition = move_group.getCurrentPose().pose;

    move_group.setStartState(*move_group.getCurrentState());

    // Vector to store the waypoints for the planning process
    std::vector<geometry_msgs::Pose> waypoints;
    // Stores the first target pose or waypoint
    geometry_msgs::Pose target_pose3 = target_home;
    // Decrements current X position by BACKWARD_MOVE*3
//        target_pose3.position.y = target_pose3.position.y - yHomePosition[k];
    target_pose3.position.z = target_pose3.position.z + dist;
    waypoints.push_back(target_pose3);

    // We want the Cartesian path to be interpolated at a resolution of 1 cm
    // which is why we will specify 0.01 as the max step in Cartesian
    // translation.  We will specify the jump threshold as 0.0, effectively disabling it.
    // Warning - disabling the jump threshold while operating real hardware can cause
    // large unpredictable motions of redundant joints and could be a safety issue
    moveit_msgs::RobotTrajectory trajectory;
    const double jump_threshold = 0.0;
    const double eef_step = 0.01;
    double fraction = move_group.computeCartesianPath(waypoints, eef_step, jump_threshold, trajectory, true);
    ROS_INFO_NAMED("tutorial", "Visualizing plan 4 (Cartesian path) (%.2f%% acheived)", fraction * 100.0);

    // Visualize the plan in RViz
    visual_tools.deleteAllMarkers();
    visual_tools.publishText(text_pose, "Cartesian Path", rvt::WHITE, rvt::XLARGE);
    visual_tools.publishPath(waypoints, rvt::LIME_GREEN, rvt::SMALL);
    for (std::size_t i = 0; i < waypoints.size(); ++i)
    visual_tools.publishAxisLabeled(waypoints[i], "pt" + std::to_string(i), rvt::SMALL);
    visual_tools.trigger();

    // Cartesian motions should often be slow, e.g. when approaching objects. The speed of cartesian
    // plans cannot currently be set through the maxVelocityScalingFactor, but requires you to time
    // the trajectory manually, as described [here](https://groups.google.com/forum/#!topic/moveit-users/MOoFxy2exT4).
    // Pull requests are welcome.

    // You can execute a trajectory like this.
    move_group.execute(trajectory);
}

void pick_up_object(moveit_robot &Robot, double down_move_dist = 0.05)
{
    // Robot moves down, grasps part and moves back to original position
    Robot.open_gripper();
    Robot.z_move(-down_move_dist);
    Robot.close_gripper();
    Robot.z_move(down_move_dist);
}

void set_down_object(moveit_robot &Robot, double down_move_dist = 0.05)
{
    // Robot moves down, grasps part and moves back to original position
    Robot.z_move(-down_move_dist);
    Robot.open_gripper();
    Robot.z_move(down_move_dist);
}

void home(std::map<std::string, double> &targetJoints, moveit_robot &Robot, std::map<std::string, jnt_angs> joint_positions)
{
    //Robot.move_group.setStartState(*Robot.move_group.getCurrentState());
    string bring_cmd = "home";
    targetJoints.clear();
    targetJoints["shoulder_pan_joint"] = joint_positions[bring_cmd].angles[0]*3.1416/180;	// (deg*PI/180)
    targetJoints["shoulder_lift_joint"] = joint_positions[bring_cmd].angles[1]*3.1416/180;
    targetJoints["elbow_joint"] = joint_positions[bring_cmd].angles[2]*3.1416/180;
    targetJoints["wrist_1_joint"] = joint_positions[bring_cmd].angles[3]*3.1416/180;
    targetJoints["wrist_2_joint"] = joint_positions[bring_cmd].angles[4]*3.1416/180;
    targetJoints["wrist_3_joint"] = joint_positions[bring_cmd].angles[5]*3.1416/180;

    Robot.move_robot(targetJoints);
}

void take_side(string bring_cmd, std::map<std::string, double> &targetJoints, moveit_robot &Robot, std::map<std::string, jnt_angs> joint_positions)
{
    //Robot.move_group.setStartState(*Robot.move_group.getCurrentState());
    // Move to position above side
    targetJoints.clear();
    targetJoints["shoulder_pan_joint"] = joint_positions[bring_cmd].angles[0]*3.1416/180;	// (deg*PI/180)
    targetJoints["shoulder_lift_joint"] = joint_positions[bring_cmd].angles[1]*3.1416/180;
    targetJoints["elbow_joint"] = joint_positions[bring_cmd].angles[2]*3.1416/180;
    targetJoints["wrist_1_joint"] = joint_positions[bring_cmd].angles[3]*3.1416/180;
    targetJoints["wrist_2_joint"] = joint_positions[bring_cmd].angles[4]*3.1416/180;
    targetJoints["wrist_3_joint"] = joint_positions[bring_cmd].angles[5]*3.1416/180;
    Robot.move_robot(targetJoints);

    // Move down, pick side up, move up
    pick_up_object(Robot, 0.05);

    //Robot.move_group.setStartState(*Robot.move_group.getCurrentState());
    // Move to user delivery position
    targetJoints.clear();
    targetJoints["shoulder_pan_joint"] = joint_positions["deliver_2_user"].angles[0]*3.1416/180;	// (deg*PI/180)
    targetJoints["shoulder_lift_joint"] = joint_positions["deliver_2_user"].angles[1]*3.1416/180;
    targetJoints["elbow_joint"] = joint_positions["deliver_2_user"].angles[2]*3.1416/180;
    targetJoints["wrist_1_joint"] = joint_positions["deliver_2_user"].angles[3]*3.1416/180;
    targetJoints["wrist_2_joint"] = joint_positions["deliver_2_user"].angles[4]*3.1416/180;
    targetJoints["wrist_3_joint"] = joint_positions["deliver_2_user"].angles[5]*3.1416/180;
    Robot.move_robot(targetJoints);

    // Move down, set down side, move up
    set_down_object(Robot, 0.05);

    //Robot.move_group.setStartState(*Robot.move_group.getCurrentState());
    // Return to home position
    home(targetJoints, Robot, joint_positions);
}

void take_box(std::map<std::string, double> &targetJoints, moveit_robot &Robot, std::map<std::string, jnt_angs> joint_positions)
{
    //Robot.move_group.setStartState(*Robot.move_group.getCurrentState());

    // Move robot to position above box
    string bring_cmd = "take_box";
    targetJoints.clear();
    targetJoints["shoulder_pan_joint"] = joint_positions[bring_cmd].angles[0]*3.1416/180;	// (deg*PI/180)
    targetJoints["shoulder_lift_joint"] = joint_positions[bring_cmd].angles[1]*3.1416/180;
    targetJoints["elbow_joint"] = joint_positions[bring_cmd].angles[2]*3.1416/180;
    targetJoints["wrist_1_joint"] = joint_positions[bring_cmd].angles[3]*3.1416/180;
    targetJoints["wrist_2_joint"] = joint_positions[bring_cmd].angles[4]*3.1416/180;
    targetJoints["wrist_3_joint"] = joint_positions[bring_cmd].angles[5]*3.1416/180;
    Robot.move_robot(targetJoints);

    // Move down, pick side up, move up
    pick_up_object(Robot, 0.05);

    // Move to position
    bring_cmd = "deliver_box";
    targetJoints.clear();
    targetJoints["shoulder_pan_joint"] = joint_positions[bring_cmd].angles[0]*3.1416/180;	// (deg*PI/180)
    targetJoints["shoulder_lift_joint"] = joint_positions[bring_cmd].angles[1]*3.1416/180;
    targetJoints["elbow_joint"] = joint_positions[bring_cmd].angles[2]*3.1416/180;
    targetJoints["wrist_1_joint"] = joint_positions[bring_cmd].angles[3]*3.1416/180;
    targetJoints["wrist_2_joint"] = joint_positions[bring_cmd].angles[4]*3.1416/180;
    targetJoints["wrist_3_joint"] = joint_positions[bring_cmd].angles[5]*3.1416/180;
    Robot.move_robot(targetJoints);

    // Move down, set down side, move up
    set_down_object(Robot, 0.05);

    // Return to home
    home(targetJoints, Robot, joint_positions);
}


int main(int argc, char** argv)
{
    // Set up ROS stuff
    ros::init(argc, argv, "hri_static_demo");
    ros::NodeHandle node_handle;
    ros::AsyncSpinner spinner(1);
    spinner.start();

    // High level move commands subscriber
	ros::Subscriber subRobotPosition = node_handle.subscribe("RobotMove", 1000, robotMoveCallback);

    // Robot object
    moveit_robot Robot(&node_handle);
    // Map to hold values to send to robot
    std::map<std::string, double> targetJoints;
    // Create map of high level joint positions
    std::map<std::string, jnt_angs> joint_positions = create_joint_pos();
    string last_obj_string = "";

    // Send robot to home position
    home(targetJoints, Robot, joint_positions);

    while( ros::ok() )
    {
        // wait position
        cout << "waiting for command" << endl;

            targetJoints.clear();

            // Ignore repeat requests
            if (objectString != last_obj_string)
            {
                last_obj_string = objectString;
                if(objectString=="bring_side_1" || objectString=="bring_side_2" || objectString=="bring_side_3" || objectString=="bring_side_4")
                {          
                    take_side(objectString, targetJoints, Robot, joint_positions);
                }
                else if( objectString == "take_box" )
                {            
                    take_box(targetJoints, Robot, joint_positions);
                }
                else
                {
                    home(targetJoints, Robot, joint_positions);
                }
            }
            
    }

    ros::shutdown();
    return 0;
}
