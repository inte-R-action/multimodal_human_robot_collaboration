/*
 *********************************************************************************
 * Author: Uriel Martinez-Hernandez
 * Email: u.martinez@bath.ac.uk
 * Date: 17-February-2020
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

#include "ros/ros.h"
#include <sstream>
#include <iostream>
#include <string.h>
#include "std_msgs/String.h"
#include "std_msgs/Int32.h"
#include <unistd.h>
#include <map>

using namespace std;

string gripper_action = "";
string done_msg = "";

// callback function to get the status from the tactile sensor
void robotCommandStatusCallback(const std_msgs::String::ConstPtr& msg)
{
    gripper_action.clear();
    gripper_action = msg->data;

    if( gripper_action == "grasp" )
    {
        // close the gripper to the maximum value of rPR = 255
        std::cout << "CLOSE GRIPPER" << std::endl; 

        // wait until the activation action is completed to continue with the next action
        printf("IN PROGRESS: grasp \n");
        sleep(3);
        printf("COMPLETED: grasp \n");
        done_msg = "grasp_completed";
    }
    else if( gripper_action == "release" )
    {
        // open the gripper to the maximum value of rPR = 0
        std::cout << "OPEN GRIPPER" << std::endl; 

        // wait until the activation action is completed to continue with the next action
        printf("IN PROGRESS: release \n");
        sleep(3);
        printf("COMPLETED: release \n");
        done_msg = "release_completed";
    }
    else if ( gripper_action == "completion acknowledged" )
    {
        printf("Acknowledge from UR received \n");
        done_msg = "acknowledge received";
    }
    else
    {
        // keep current configuration
    }
}

int main(int argc, char** argv)
{
    ros::init(argc, argv, "rq_gripper_2F140");

    ros::NodeHandle node_handle;

    ros::Rate loop_rate(10);
    ros::AsyncSpinner spinner(1);
    spinner.start();

    ros::Publisher gripperStatusPub = node_handle.advertise<std_msgs::String>("Gripper2UR", 1);
    ros::Subscriber robotStatusSub = node_handle.subscribe("UR2Gripper", 1, robotCommandStatusCallback);

    ros::spinOnce();
    loop_rate.sleep();

    std_msgs::String msg;

    while( ros::ok() )
    {
        
        if (gripper_action == "grasp" || gripper_action == "release")
        {
            while (done_msg != "acknowledge received")
            {
                msg.data = done_msg;
                gripperStatusPub.publish(msg);
            }
        }
        
        msg.data = "gripper_ready";
        gripperStatusPub.publish(msg);
        
        sleep(1);
    }

    ros::shutdown();

    return 0;
}