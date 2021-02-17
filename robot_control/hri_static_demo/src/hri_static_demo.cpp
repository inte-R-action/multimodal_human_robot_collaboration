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

using namespace std;


string objectString = "";
bool robotMove = false;

void robotMoveCallback(const std_msgs::String::ConstPtr& msg)
{
//  ROS_INFO("I heard: [%s]", msg->data);

//  if( msg->data != "" )
//      robotMove = true;
//  else
//      robotMove = false;
 
 	objectString.clear();

    objectString = msg->data; 

    cout << "Robot move: " << robotMove << endl; 
    cout << "Object: " << objectString << endl;
}

struct jnt_angs{
    double angles[6];
};

std::map<std::string, jnt_angs> create_joint_pos(){
    std::map<std::string, jnt_angs> joint_positions;
    joint_positions["home"] = {-11.75, -83.80, 47.90, -125.0, -90.0, 0.26};
    joint_positions["bring_side_1"] = {-31.85, -43.48, 55.18, -103.14, -90.87, 0.26};
    joint_positions["bring_side_2"] = {-19.00, -43.48, 55.18, -103.14, -90.87, 0.26};
    joint_positions["bring_side_3"] = {-2.74, -43.48, 55.18, -103.14, -90.87, 0.26};
    joint_positions["bring_side_4"] = {12.00, -43.48, 55.18, -103.14, -90.87, 0.26};
    joint_positions["take_box"] = {46.68, -67.95, 108.8, -125.00, -90.0, 0.26};
    joint_positions["deliver_2_user"] = {46.68, -67.95, 108.8, -125.00, -90.0, 0.26};
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
        moveit::planning_interface::MoveGroupInterface::Plan plan;
        moveit::core::RobotStatePtr current_state;
        std::vector<double> joint_group_positions;

        moveit_robot();
        void move_robot(std::map<std::string, double> targetJoints);

};
moveit_robot::moveit_robot() : PLANNING_GROUP("manipulator"), move_group(moveit::planning_interface::MoveGroupInterface(PLANNING_GROUP)) {

    // Raw pointers are frequently used to refer to the planning group for improved performance.
    const robot_state::JointModelGroup* joint_model_group = move_group.getCurrentState()->getJointModelGroup(PLANNING_GROUP);

    // Visualization
    // ^^^^^^^^^^^^^
    // The package MoveItVisualTools provides many capabilties for visualizing objects, robots,
    // and trajectories in RViz as well as debugging tools such as step-by-step introspection of a script
    namespace rvt = rviz_visual_tools;
    moveit_visual_tools::MoveItVisualTools visual_tools("world");
    visual_tools.deleteAllMarkers();

    // Remote control is an introspection tool that allows users to step through a high level script
    // via buttons and keyboard shortcuts in RViz
    visual_tools.loadRemoteControl();

    // RViz provides many types of markers, in this demo we will use text, cylinders, and spheres
//    Eigen::Affine3d text_pose = Eigen::Affine3d::Identity();
    Eigen::Isometry3d text_pose = Eigen::Isometry3d::Identity();
    text_pose.translation().z() = 1.75;
    visual_tools.publishText(text_pose, "HRI Static Demo - v 0.1.0", rvt::WHITE, rvt::XLARGE);

    // Batch publishing is used to reduce the number of messages being sent to RViz for large visualizations
    visual_tools.trigger();

    // Getting Basic Information
    // ^^^^^^^^^^^^^^^^^^^^^^^^^
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
    moveit::planning_interface::MoveGroupInterface::Plan plan;

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
}

void moveit_robot::move_robot(std::map<std::string, double> targetJoints){
    move_group.setJointValueTarget(targetJoints);

    bool success = (move_group.plan(plan) == moveit::planning_interface::MoveItErrorCode::SUCCESS);
    ROS_INFO("Visualizing new move position plan (%.2f%% acheived)",success * 100.0);

    move_group.execute(plan);
}


void pick_up_side(std::map<std::string, double> &targetJoints, moveit_robot &Robot)
{
    double pick_ang_1[6] = {0.0, 20.0, -10.0, -20.0, 0.0, 0.0};
    // Open Gripper

    // Move down
    targetJoints["shoulder_pan_joint"] = targetJoints["shoulder_pan_joint"] + (pick_ang_1[0]*3.1416/180);	// (deg*PI/180)
    targetJoints["shoulder_lift_joint"] = targetJoints["shoulder_lift_joint"] + (pick_ang_1[1]*3.1416/180);
    targetJoints["elbow_joint"] = targetJoints["elbow_joint"] + (pick_ang_1[2]*3.1416/180);
    targetJoints["wrist_1_joint"] = targetJoints["wrist_1_joint"] + (pick_ang_1[3]*3.1416/180);
    targetJoints["wrist_2_joint"] = targetJoints["wrist_2_joint"] + (pick_ang_1[4]*3.1416/180);
    targetJoints["wrist_3_joint"] = targetJoints["wrist_3_joint"] + (pick_ang_1[5]*3.1416/180);
    Robot.move_robot(targetJoints);

    // Close Gripper

    // Move up
    targetJoints["shoulder_pan_joint"] = targetJoints["shoulder_pan_joint"] - (pick_ang_1[0]*3.1416/180);	// (deg*PI/180)
    targetJoints["shoulder_lift_joint"] = targetJoints["shoulder_lift_joint"] - (pick_ang_1[1]*3.1416/180);
    targetJoints["elbow_joint"] = targetJoints["elbow_joint"] - (pick_ang_1[2]*3.1416/180);
    targetJoints["wrist_1_joint"] = targetJoints["wrist_1_joint"] - (pick_ang_1[3]*3.1416/180);
    targetJoints["wrist_2_joint"] = targetJoints["wrist_2_joint"] - (pick_ang_1[4]*3.1416/180);
    targetJoints["wrist_3_joint"] = targetJoints["wrist_3_joint"] - (pick_ang_1[5]*3.1416/180);
    Robot.move_robot(targetJoints);
}

void home(std::map<std::string, double> &targetJoints, moveit_robot &Robot, std::map<std::string, jnt_angs> joint_positions)
{
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
    targetJoints.clear();
    targetJoints["shoulder_pan_joint"] = joint_positions[bring_cmd].angles[0]*3.1416/180;	// (deg*PI/180)
    targetJoints["shoulder_lift_joint"] = joint_positions[bring_cmd].angles[1]*3.1416/180;
    targetJoints["elbow_joint"] = joint_positions[bring_cmd].angles[2]*3.1416/180;
    targetJoints["wrist_1_joint"] = joint_positions[bring_cmd].angles[3]*3.1416/180;
    targetJoints["wrist_2_joint"] = joint_positions[bring_cmd].angles[4]*3.1416/180;
    targetJoints["wrist_3_joint"] = joint_positions[bring_cmd].angles[5]*3.1416/180;
    Robot.move_robot(targetJoints);

    pick_up_side(targetJoints, Robot);

    targetJoints.clear();
    targetJoints["shoulder_pan_joint"] = joint_positions["deliver_2_user"].angles[0]*3.1416/180;	// (deg*PI/180)
    targetJoints["shoulder_lift_joint"] = joint_positions["deliver_2_user"].angles[1]*3.1416/180;
    targetJoints["elbow_joint"] = joint_positions["deliver_2_user"].angles[2]*3.1416/180;
    targetJoints["wrist_1_joint"] = joint_positions["deliver_2_user"].angles[3]*3.1416/180;
    targetJoints["wrist_2_joint"] = joint_positions["deliver_2_user"].angles[4]*3.1416/180;
    targetJoints["wrist_3_joint"] = joint_positions["deliver_2_user"].angles[5]*3.1416/180;
    Robot.move_robot(targetJoints);

    // Open Gripper

    home(targetJoints, Robot, joint_positions);
}

void take_box(string bring_cmd, std::map<std::string, double> &targetJoints, moveit_robot &Robot, std::map<std::string, jnt_angs> joint_positions)
{
    targetJoints.clear();
    targetJoints["shoulder_pan_joint"] = joint_positions[bring_cmd].angles[0]*3.1416/180;	// (deg*PI/180)
    targetJoints["shoulder_lift_joint"] = joint_positions[bring_cmd].angles[1]*3.1416/180;
    targetJoints["elbow_joint"] = joint_positions[bring_cmd].angles[2]*3.1416/180;
    targetJoints["wrist_1_joint"] = joint_positions[bring_cmd].angles[3]*3.1416/180;
    targetJoints["wrist_2_joint"] = joint_positions[bring_cmd].angles[4]*3.1416/180;
    targetJoints["wrist_3_joint"] = joint_positions[bring_cmd].angles[5]*3.1416/180;

    Robot.move_robot(targetJoints);

    // Close Gripper
    // Move to position
    // Open Gripper
    
    home(targetJoints, Robot, joint_positions);
}


int main(int argc, char** argv)
{
    ros::init(argc, argv, "hri_static_demo");
    ros::NodeHandle node_handle;
    ros::AsyncSpinner spinner(1);
    spinner.start();


	ros::Subscriber subRobotPosition = node_handle.subscribe("RobotMove", 1000, robotMoveCallback);

    // Start the demo
    // ^^^^^^^^^^^^^^^^^^^^^^^^^
    // ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    // The following code moves the robot to a 'home' position
    // Begin

    moveit_robot Robot;
    std::map<std::string, double> targetJoints;
    std::map<std::string, jnt_angs> joint_positions = create_joint_pos();
    string last_obj_string = "";

    home(targetJoints, Robot, joint_positions);

    while( ros::ok() )
    {
    // wait position
        cout << "waiting for command" << endl;

            targetJoints.clear();

            if (objectString != last_obj_string)
            {
                last_obj_string = objectString;
                if(objectString=="bring_side_1" || objectString=="bring_side_2" || objectString=="bring_side_3" || objectString=="bring_side_4")
                {          
                    take_side(objectString, targetJoints, Robot, joint_positions);
                }
                else if( objectString == "take_box" )
                {            
                    take_box(objectString, targetJoints, Robot, joint_positions);
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
