/*********************************************************************
 * Software License Agreement (BSD License)
 *
 *  Copyright (c) 2013, SRI International
 *  All rights reserved.
 *
 *  Redistribution and use in source and binary forms, with or without
 *  modification, are permitted provided that the following conditions
 *  are met:
 *
 *   * Redistributions of source code must retain the above copyright
 *     notice, this list of conditions and the following disclaimer.
 *   * Redistributions in binary form must reproduce the above
 *     copyright notice, this list of conditions and the following
 *     disclaimer in the documentation and/or other materials provided
 *     with the distribution.
 *   * Neither the name of SRI International nor the names of its
 *     contributors may be used to endorse or promote products derived
 *     from this software without specific prior written permission.
 *
 *  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 *  "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 *  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
 *  FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 *  COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
 *  INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
 *  BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
 *  LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
 *  CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 *  LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
 *  ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 *  POSSIBILITY OF SUCH DAMAGE.
 *********************************************************************/

/* Author: Sachin Chitta, Dave Coleman, Mike Lautman */

#include <moveit/move_group_interface/move_group_interface.h>
#include <moveit/planning_scene_interface/planning_scene_interface.h>

#include <moveit_msgs/DisplayRobotState.h>
#include <moveit_msgs/DisplayTrajectory.h>

#include <moveit_msgs/AttachedCollisionObject.h>
#include <moveit_msgs/CollisionObject.h>

#include <moveit_visual_tools/moveit_visual_tools.h>

#include <tf2_ros/transform_listener.h>
#include <geometry_msgs/TransformStamped.h>
#include <tf2_geometry_msgs/tf2_geometry_msgs.h>
#include <tf2_ros/static_transform_broadcaster.h>
#include "sam_custom_messages/Object.h"
#include "sam_custom_messages/object_state.h"

namespace rvt = rviz_visual_tools;

class ik_robot {
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

        ik_robot(ros::NodeHandle* node_handle);

        // Function definitions
        bool plan_to_pose(geometry_msgs::Pose pose);
        geometry_msgs::Pose transform_pose(geometry_msgs::Pose input_pose);

    private:
        ros::NodeHandle nh_;
};

ik_robot::ik_robot(ros::NodeHandle* node_handle) : nh_(*node_handle), PLANNING_GROUP("manipulator"), visual_tools("world"), move_group(moveit::planning_interface::MoveGroupInterface(PLANNING_GROUP)) {
    // Raw pointers are frequently used to refer to the planning group for improved performance.
    joint_model_group = move_group.getCurrentState()->getJointModelGroup(PLANNING_GROUP);

    visual_tools.deleteAllMarkers();

    // Remote control is an introspection tool that allows users to step through a high level script
    // via buttons and keyboard shortcuts in RViz
    visual_tools.loadRemoteControl();

    // RViz provides many types of markers, in this demo we will use text, cylinders, and spheres
    //Eigen::Affine3d text_pose = Eigen::Affine3d::Identity();
    //Eigen::Isometry3d 
    text_pose = Eigen::Isometry3d::Identity();
    text_pose.translation().z() = 1.75;
    visual_tools.publishText(text_pose, "IK Testing", rvt::WHITE, rvt::XLARGE);

    // Batch publishing is used to reduce the number of messages being sent to RViz for large visualizations
    visual_tools.trigger();

    // Getting Basic Information
    // ^^^^^^^^^^^^^^^^^^^^^^^^^
    //
    // We can print the name of the reference frame for this robot.
    ROS_INFO_NAMED("IK Robot", "Planning frame: %s", move_group.getPlanningFrame().c_str());

    // We can also print the name of the end-effector link for this group.
    ROS_INFO_NAMED("IK Robot", "End effector link: %s", move_group.getEndEffectorLink().c_str());

    // We can get a list of all the groups in the robot:
    ROS_INFO_NAMED("IK Robot", "Available Planning Groups:");
    std::copy(move_group.getJointModelGroupNames().begin(), move_group.getJointModelGroupNames().end(), std::ostream_iterator<std::string>(std::cout, ", "));

    // Start the demo
    // ^^^^^^^^^^^^^^^^^^^^^^^^^
    visual_tools.prompt("Press 'next' in the RvizVisualToolsGui window to start the demo");

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

    // Add collision objects
    // ^^^^^^^^^^^^^^^^^^^^^^^^^^

    ros::Publisher planning_scene_diff_publisher = nh_.advertise<moveit_msgs::PlanningScene>("planning_scene", 1);
    ros::WallDuration sleep_t(0.5);
    while (planning_scene_diff_publisher.getNumSubscribers() < 1)
    {
        sleep_t.sleep();
    }
    visual_tools.prompt("Press 'next' in the RvizVisualToolsGui window to start adding objects");

    moveit_msgs::PlanningScene planning_scene;
    //planning_scene.robot_state.attached_collision_objects.clear();
    //planning_scene.world.collision_objects.clear();
    //planning_scene_diff_publisher.publish(planning_scene);
    std::vector<std::string> object_ids;
    object_ids.push_back("gripper");
    object_ids.push_back("camera");
    object_ids.push_back("ground");
    planning_scene_interface.removeCollisionObjects(object_ids);

    std::vector<moveit_msgs::CollisionObject> collision_objects;
    //geometry_msgs::PoseStamped current_pose = move_group.getCurrentPose();

    // Add gripper object to robot
    moveit_msgs::AttachedCollisionObject gripper_object;
    gripper_object.link_name = "ee_link";
    gripper_object.object.header.frame_id = "ee_link";
    gripper_object.object.id = "gripper";
    shape_msgs::SolidPrimitive gripper_primitive;
    gripper_primitive.type = gripper_primitive.BOX;
    gripper_primitive.dimensions.resize(3);
    gripper_primitive.dimensions[0] = 0.17;
    gripper_primitive.dimensions[1] = 0.12;
    gripper_primitive.dimensions[2] = 0.1;

    geometry_msgs::Pose gripper_pose;
    gripper_pose.orientation.w = 0.0;
    gripper_pose.position.x = gripper_primitive.dimensions[0]/2;
    gripper_pose.position.y = 0.0;
    gripper_pose.position.z = 0.0;

    gripper_object.object.primitives.push_back(gripper_primitive);
    gripper_object.object.primitive_poses.push_back(gripper_pose);
    gripper_object.object.operation = gripper_object.object.ADD;

    //gripper_object.touch_links = std::vector<std::string>{ "ee_link"};
    
    //planning_scene.world.collision_objects.push_back(gripper_object.object);
    planning_scene.is_diff = true;
    //planning_scene_diff_publisher.publish(planning_scene);

    /* First, define the REMOVE object message*/
    //moveit_msgs::CollisionObject remove_gripper;
    //remove_gripper.id = "gripper";
    //remove_gripper.header.frame_id = "base_link";
    //remove_gripper.operation = remove_gripper.REMOVE;

    /* Carry out the REMOVE + ATTACH operation */
    ROS_INFO("Attaching the gripper to the robot");
    //planning_scene.world.collision_objects.clear();
    //planning_scene.world.collision_objects.push_back(remove_gripper);
    planning_scene.robot_state.attached_collision_objects.push_back(gripper_object);
    //planning_scene_diff_publisher.publish(planning_scene);
    
    // Add camera object to robot
    moveit_msgs::AttachedCollisionObject camera_object;
    camera_object.link_name = "ee_link";
    camera_object.object.header.frame_id = "ee_link";
    camera_object.object.id = "camera";
    shape_msgs::SolidPrimitive camera_primitive;
    camera_primitive.type = camera_primitive.BOX;
    camera_primitive.dimensions.resize(3);
    camera_primitive.dimensions[0] = 0.02;
    camera_primitive.dimensions[1] = 0.15;
    camera_primitive.dimensions[2] = 0.07;

    geometry_msgs::Pose camera_pose;
    camera_pose.orientation.w = 0.0;
    camera_pose.position.x = 0.07;
    camera_pose.position.y = 0.0;
    camera_pose.position.z = (camera_primitive.dimensions[2]+gripper_primitive.dimensions[2])/2;

    camera_object.object.primitives.push_back(camera_primitive);
    camera_object.object.primitive_poses.push_back(camera_pose);
    camera_object.object.operation = camera_object.object.ADD;

    //camera_object.touch_links = std::vector<std::string>{ "ee_link", "gripper"};
    
    //planning_scene.world.collision_objects.push_back(camera_object.object);
    planning_scene.is_diff = true;
    //planning_scene_diff_publisher.publish(planning_scene);

    /* First, define the REMOVE object message*/
    //moveit_msgs::CollisionObject remove_camera;
    //remove_camera.id = "camera";
    //remove_camera.header.frame_id = "base_link";
    //remove_camera.operation = remove_camera.REMOVE;

    /* Carry out the REMOVE + ATTACH operation */
    ROS_INFO("Attaching the camera to the robot");
    //planning_scene.world.collision_objects.clear();
    //planning_scene.world.collision_objects.push_back(remove_camera);
    planning_scene.robot_state.attached_collision_objects.push_back(camera_object);
    planning_scene_diff_publisher.publish(planning_scene);
    visual_tools.prompt("Press 'next' in the RvizVisualToolsGui window to once the collision object appears in RViz");

    //collision_objects.push_back(camera_object);

    //ROS_INFO_NAMED("tutorial", "Attach the camera to the robot");
    //move_group.attachObject(camera_object.id);

    // Add ground plane object to robot
    moveit_msgs::CollisionObject ground_object;
    ground_object.header.frame_id = move_group.getPlanningFrame();
    ground_object.id = "ground";
    shape_msgs::SolidPrimitive ground_primitive;
    ground_primitive.type = ground_primitive.BOX;
    ground_primitive.dimensions.resize(3);
    ground_primitive.dimensions[0] = 2;
    ground_primitive.dimensions[1] = 2;
    ground_primitive.dimensions[2] = 0.01;

    geometry_msgs::Pose ground_pose;
    ground_pose.orientation.w = 1.0;
    ground_pose.position.x = 0.0;
    ground_pose.position.y = 0.0;
    ground_pose.position.z = -ground_primitive.dimensions[2];

    ground_object.primitives.push_back(ground_primitive);
    ground_object.primitive_poses.push_back(ground_pose);
    ground_object.operation = ground_object.ADD;

    collision_objects.push_back(ground_object);

    ROS_INFO_NAMED("tutorial", "Add ground into the world");
    planning_scene_interface.addCollisionObjects(collision_objects);
    visual_tools.publishText(text_pose, "Add object", rvt::WHITE, rvt::XLARGE);
    visual_tools.trigger();
    visual_tools.prompt("Press 'next' in the RvizVisualToolsGui window to once the collision object appears in RViz");

}

bool ik_robot::plan_to_pose(geometry_msgs::Pose pose){
    bool success = false;
    move_group.setPoseTarget(pose);

    success = (move_group.plan(plan) == moveit::planning_interface::MoveItErrorCode::SUCCESS);

    ROS_INFO_NAMED("IK Robot", "Visualizing plan 1 (pose goal) %s", success ? "" : "FAILED");

    // Visualizing plans
    // ^^^^^^^^^^^^^^^^^
    // We can also visualize the plan as a line with markers in RViz.
    ROS_INFO_NAMED("IK Robot", "Visualizing plan 1 as trajectory line");
    visual_tools.publishAxisLabeled(pose, "pose1");
    visual_tools.publishText(text_pose, "Pose Goal", rvt::WHITE, rvt::XLARGE);
    visual_tools.publishTrajectoryLine(plan.trajectory_, joint_model_group);
    visual_tools.trigger();
    visual_tools.prompt("Press 'next' in the RvizVisualToolsGui window to continue the demo");
    return success;
}

geometry_msgs::Pose ik_robot::transform_pose(geometry_msgs::Pose input_pose){

  tf2_ros::Buffer tfBuffer;
  tf2_ros::TransformListener tfListener(tfBuffer);
  geometry_msgs::Pose output_pose;
  geometry_msgs::TransformStamped transform;

  while (true){
    try{
      transform = tfBuffer.lookupTransform("camera_frame", "world",
                                 ros::Time(0));
    
      ROS_INFO("%s", transform.child_frame_id.c_str());
      ROS_INFO("%f", transform.transform.translation.x);
      ROS_INFO("%f", transform.transform.translation.y);
      ROS_INFO("%f", transform.transform.translation.z);
      ROS_INFO("%f", transform.transform.rotation.x);
      ROS_INFO("%f", transform.transform.rotation.y);
      ROS_INFO("%f", transform.transform.rotation.z);
      ROS_INFO("%f", transform.transform.rotation.w);

      tf2::doTransform(input_pose, output_pose, transform);

      ROS_INFO_STREAM("Input pose: \n" << input_pose);
      ROS_INFO_STREAM("Output pose: \n" << output_pose);

      return output_pose;
    }
    catch (tf2::TransformException &ex) {
      ROS_ERROR("%s",ex.what());
      ros::Duration(1.0).sleep();
    }
  }
}

bool setup_camera_transform(){
  static tf2_ros::StaticTransformBroadcaster static_broadcaster;
  geometry_msgs::TransformStamped static_transformStamped;

  static_transformStamped.header.stamp = ros::Time::now();
  static_transformStamped.header.frame_id = "ee_link";
  static_transformStamped.child_frame_id = "camera_frame";
  static_transformStamped.transform.translation.x = 5;
  static_transformStamped.transform.translation.y = 10;
  static_transformStamped.transform.translation.z = 15;
  //tf2::Quaternion quat;
  //quat.setRPY(atof(argv[5]), atof(argv[6]), atof(argv[7]));
  static_transformStamped.transform.rotation.x = 0;//quat.x();
  static_transformStamped.transform.rotation.y = 0;//quat.y();
  static_transformStamped.transform.rotation.z = 0;//quat.z();
  static_transformStamped.transform.rotation.w = 0;//quat.w();
  static_broadcaster.sendTransform(static_transformStamped);
}


int main(int argc, char** argv)
{
    ros::init(argc, argv, "ik_robot");
    ros::NodeHandle node_handle;
    ros::AsyncSpinner spinner(1);
    spinner.start();

    setup_camera_transform();

    ik_robot Robot(&node_handle);

    //sam_custom_messages::object_state block_state;
    //block_state = ros::topic::waitForMessage<sam_custom_messages::object_state>("/ObjectStates", ros::Duration(1));
    //geometry_msgs::Pose pose_base_obj = Robot.transform_pose(block_state.Pose);

    geometry_msgs::Pose pose_cam_obj;
    pose_cam_obj.orientation.w = 1.0;
    pose_cam_obj.position.x = 0.3;
    pose_cam_obj.position.y = 0.2;
    pose_cam_obj.position.z = 0.6;

    geometry_msgs::Pose pose_base_obj = Robot.transform_pose(pose_cam_obj);

    geometry_msgs::Pose target_pose1;
    target_pose1.orientation.x = pose_base_obj.orientation.x;
    target_pose1.orientation.y = pose_base_obj.orientation.y;
    target_pose1.orientation.z = pose_base_obj.orientation.z;
    target_pose1.orientation.w = pose_base_obj.orientation.w;
    target_pose1.position.x = pose_base_obj.position.x;
    target_pose1.position.y = pose_base_obj.position.y;
    target_pose1.position.z = 0.11;
    bool success = Robot.plan_to_pose(target_pose1);

  // Moving to a pose goal
  // ^^^^^^^^^^^^^^^^^^^^^
  //
  // Moving to a pose goal is similar to the step above
  // except we now use the move() function. Note that
  // the pose goal we had set earlier is still active
  // and so the robot will try to move to that goal. We will
  // not use that function in this tutorial since it is
  // a blocking function and requires a controller to be active
  // and report success on execution of a trajectory.

  /* Uncomment below line when working with a real robot */
  //Robot.move_group.move();

}
