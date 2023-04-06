#include <ros.h>
#include <std_msgs/String.h>

#define HAMMER_PIN 7
#define ALLEN_PIN 6
#define SCREW_PIN 5

bool hammer_value;
bool allen_value;
bool screw_value;

char msg_data[15];

ros::NodeHandle node_handle;

std_msgs::String sensor_msg;

ros::Publisher sensor_publisher("ToolStatus", &sensor_msg);

void setup()
{
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(HAMMER_PIN, INPUT_PULLUP);
  pinMode(ALLEN_PIN, INPUT_PULLUP);
  pinMode(SCREW_PIN, INPUT_PULLUP);
  
  node_handle.initNode();
  node_handle.advertise(sensor_publisher);
}

void loop()
{ 
  hammer_value = digitalRead(HAMMER_PIN);
  allen_value = digitalRead(ALLEN_PIN);
  screw_value = digitalRead(SCREW_PIN);

  if (( hammer_value ) || ( allen_value ) || ( screw_value )){
    digitalWrite(LED_BUILTIN, HIGH); 
  } else {
    digitalWrite(LED_BUILTIN, LOW);
  }

  sprintf(msg_data,"hammer_%i",hammer_value);
  sensor_msg.data = msg_data;
  sensor_publisher.publish( &sensor_msg );
 
  sprintf(msg_data,"allenkey_%i",allen_value);
  sensor_msg.data = msg_data;
  sensor_publisher.publish( &sensor_msg );
 
  sprintf(msg_data,"screwdriver_%i",screw_value);
  sensor_msg.data = msg_data;
  sensor_publisher.publish( &sensor_msg );
  
  node_handle.spinOnce();
  
  delay(100);
}
