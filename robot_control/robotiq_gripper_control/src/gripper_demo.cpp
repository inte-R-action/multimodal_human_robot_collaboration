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
#include "robotiq_2f_gripper_control/Robotiq2FGripper_robot_output.h"
#include "robotiq_2f_gripper_control/Robotiq2FGripper_robot_input.h"
#include <unistd.h>
#include <map>

using namespace std;

string gripper_action = "";
string done_msg = "";
int gripperSpeed = 20;
int gripperForce = 25;
int gripperPosition = 255;


// global variable to hold the status of the gripper
robotiq_2f_gripper_control::Robotiq2FGripper_robot_input gripperStatus;

robotiq_2f_gripper_control::Robotiq2FGripper_robot_output outputControlValues;


// callback function to get the status signals from the gripper
void gripperStatusCallback(const robotiq_2f_gripper_control::Robotiq2FGripper_robot_input::ConstPtr& msg)
{
    gripperStatus = *msg;
    printf("grippercallbackmsg: gOBJ [%d]\n", msg->gOBJ);
/*
    if( msg->gOBJ == 0 )
        ROS_INFO("ROBOT FINGERS MOVING");
    else if( msg->gOBJ == 1 )
        ROS_INFO("ROBOT FINGERS STOPPED DUE TO CONTACT DETECTED WHILE OPENING");
    else if( msg->gOBJ == 2 )
        ROS_INFO("ROBOT FINGERS STOPPED DUE TO CONTACT DETECTED WHILE CLOSING");
    else if( msg->gOBJ == 3 )
        ROS_INFO("ROBOT FINGERS AT THE REQUESTED POSITION");
    else
        ROS_INFO("ROBOT FINGERS ERROR");
*/
}


class gripper_cls {
    public:

        ros::Publisher Robotiq2FGripperArgPub;
        ros::Subscriber robotStatusSub;

        void robotCommandStatusCallback(const std_msgs::String::ConstPtr& msg);
        gripper_cls(ros::NodeHandle* node_handle);


    private:
        ros::NodeHandle nh_; // we will need this, to pass between "main" and constructor

};


gripper_cls::gripper_cls(ros::NodeHandle* node_handle) : nh_(*node_handle){

    Robotiq2FGripperArgPub = nh_.advertise<robotiq_2f_gripper_control::Robotiq2FGripper_robot_output>("Robotiq2FGripperRobotOutput", 1);
    //robotStatusSub = nh_.subscribe("UR2Gripper", 1000, &gripper_cls::robotCommandStatusCallback);

}

// callback function to get the status from the tactile sensor
void gripper_cls::robotCommandStatusCallback(const std_msgs::String::ConstPtr& msg)
{

    gripper_action.clear();
    gripper_action = msg->data;

    if( gripper_action == "grasp" )
    {

        // close the gripper to the maximum value of rPR = 255
        // rGTO = 1 allows the robot to perform an action
        outputControlValues.rGTO = 1;
        outputControlValues.rSP = gripperSpeed;
        outputControlValues.rFR = gripperForce;
        outputControlValues.rPR = gripperPosition;

        Robotiq2FGripperArgPub.publish(outputControlValues);
        std::cout << "CLOSE GRIPPER" << std::endl; 

        // wait until the activation action is completed to continue with the next action
        while( gripperStatus.gOBJ != 3 && gripperStatus.gOBJ != 2 )
        {
            printf("IN PROGRESS: gOBJ [%d]\n", gripperStatus.gOBJ);
            usleep(100000);
        }
        
        done_msg = "grasp_completed";
        printf("COMPLETED: gOBJ [%d]\n", gripperStatus.gOBJ);

    }
    else if( gripper_action == "release" )
    {
        // open the gripper to the maximum value of rPR = 0
        // rGTO = 1 allows the robot to perform an action
        outputControlValues.rGTO = 1;
        outputControlValues.rSP = gripperSpeed;
        outputControlValues.rFR = gripperForce;
        outputControlValues.rPR = 0;

        Robotiq2FGripperArgPub.publish(outputControlValues);
        std::cout << "OPEN GRIPPER" << std::endl; 

        // wait until the activation action is completed to continue with the next action
        while( gripperStatus.gOBJ !=  3 && gripperStatus.gOBJ != 2  )
        {
            printf("IN PROGRESS: gOBJ [%d]\n", gripperStatus.gOBJ);
            usleep(100000);
        }

        done_msg = "release_completed";
        printf("COMPLETED: gOBJ [%d]\n", gripperStatus.gOBJ);        
        
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

    //robotiq_2f_gripper_control::Robotiq2FGripper_robot_output outputControlValues;

    gripper_cls Gripper(&node_handle);

    // connection of publisher and subscriber with the Robotiq controller from ROS Industrial
    //ros::Publisher Robotiq2FGripperArgPub = node_handle.advertise<robotiq_2f_gripper_control::Robotiq2FGripper_robot_output>("Robotiq2FGripperRobotOutput", 1);
    ros::Subscriber Robotiq2FGripperStatusPub = node_handle.subscribe("Robotiq2FGripperRobotInput", 1000, gripperStatusCallback);

    ros::Publisher gripperStatusPub = node_handle.advertise<std_msgs::String>("Gripper2UR", 5);
    //ros::Subscriber robotStatusSub = node_handle.subscribe("UR2Gripper", 1000, robotCommandStatusCallback);
    Gripper.robotStatusSub = node_handle.subscribe("UR2Gripper", 5, &gripper_cls::robotCommandStatusCallback, &Gripper);

    ros::spinOnce();
    loop_rate.sleep();


    printf("==================================================\n");
    // reset the robotic gripper (needed to activate the robot)
    outputControlValues.rACT = 0;
    outputControlValues.rGTO = 0;
    outputControlValues.rATR = 0;
    outputControlValues.rPR = 0;
    outputControlValues.rSP = 0;
    outputControlValues.rFR = 0;

    Gripper.Robotiq2FGripperArgPub.publish(outputControlValues);
    std::cout << "RESET GRIPPER" << std::endl;

    // give some time the gripper to reset
    sleep(3);


    // activate the robotic gripper
    outputControlValues.rACT = 1;
    outputControlValues.rGTO = 1;
    outputControlValues.rATR = 0;
    outputControlValues.rPR = 0;
    outputControlValues.rSP = 255;
    outputControlValues.rFR = 150;

    Gripper.Robotiq2FGripperArgPub.publish(outputControlValues);
    std::cout << "ACTIVATE GRIPPER" << std::endl; 

    // wait until the activation action is completed to continue with the next action
    while( gripperStatus.gSTA != 3 )
    {
        printf("IN PROGRESS: gSTA [%d]\n", gripperStatus.gSTA);
        usleep(100000);
    }

    printf("COMPLETED: gSTA [%d]\n", gripperStatus.gSTA);
    sleep(1);


    std_msgs::String msg;

    while( ros::ok() )
    {

        msg.data = "gripper_ready";
        gripperStatusPub.publish(msg);

        // set gripper to standby to clear the flags
        outputControlValues.rGTO = 0;

        Gripper.Robotiq2FGripperArgPub.publish(outputControlValues);
        std::cout << "STANDBY GRIPPER" << std::endl; 
        sleep(1);
        
        if (gripper_action == "grasp" || gripper_action == "release")
        {
            while (done_msg != "acknowledge received")
            {
                msg.data = done_msg;
                gripperStatusPub.publish(msg);
            }
        }
        
        //msg.data = "gripper_ready";
        //gripperStatusPub.publish(msg);
        
        //sleep(1);
    }

    ros::shutdown();

    return 0;
}