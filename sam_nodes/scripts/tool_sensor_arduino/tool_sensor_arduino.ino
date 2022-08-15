#include <ros.h>
#include <std_msgs/String.h>

#define HAMMER_PIN 5
#define ALLEN_PIN 6
#define SCREW_PIN 7

bool hammer_value;
bool allen_value;
bool screw_value;

String hammer_msg;
String allen_msg;
String screw_msg;

ros::NodeHandle node_handle;

std_msgs::String sensor_msg;

ros::Publisher sensor_publisher("ToolStatus", &sensor_msg, 10);

void setup()
{
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(HAMMER_PIN, INPUT_PULLUP);
  pinMode(ALLEN_PIN, INPUT_PULLUP);
  pinMode(SCREW_PIN, INPUT_PULLUP);

  Serial.begin(9600);
  
  node_handle.initNode();
  node_handle.advertise(sensor_publisher);
}

void loop()
{ 
  hammer_value = !digitalRead(HAMMER_PIN);
  allen_value = !digitalRead(ALLEN_PIN);
  screw_value = !digitalRead(SCREW_PIN);

  hammer_msg = "hammer_" + String(hammer_value);
  allen_msg = "allen_" + String(allen_value);
  screw_msg = "screw_" + String(screw_value);

  if (( hammer_value ) || ( allen_value ) || ( screw_value )){
    digitalWrite(LED_BUILTIN, HIGH); 
  } else {
    digitalWrite(LED_BUILTIN, LOW);
  }

  Serial.print( hammer_msg );
  Serial.print( "  " );
  Serial.print( allen_msg );
  Serial.print( "  " );
  Serial.println( screw_msg );

  sensor_msg.data = hammer_msg;
  sensor_publisher.publish( &sensor_msg );
  sensor_msg.data = allen_msg;
  sensor_publisher.publish( &sensor_msg );
  sensor_msg.data = screw_msg;
  sensor_publisher.publish( &sensor_msg );
  
  node_handle.spinOnce();
  
  delay(100);
}
