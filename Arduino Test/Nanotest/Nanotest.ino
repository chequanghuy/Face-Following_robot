#include <SoftwareSerial.h>
#include <Servo.h>
#define handle_center1 35
#define handle_center2 90
int data;
Servo s9, s10; // tạo 2 Object
void servo_init();
SoftwareSerial myser(3,2); //RX - TX

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  myser.begin(9600);
  servo_init();
}

void loop() {
  // put your main code here, to run repeatedly:
  if (myser.available() > 0){
    data = myser.read();
    Serial.println(data);
  }
  if(data>180) data=-(data-180);
  handle1(data);
}










void handle1(int8_t angle) {//up down
  if(angle<=-35) angle=-35;
  if(angle>=145) angle=140;
  int rc_angle = handle_center1 + angle;
  s9.write(rc_angle);
}
void handle2(int8_t angle) {//left right
  if(angle<=-90) angle=-90;
  if(angle>=90) angle=90;
  int rc_angle = handle_center2 + angle;
  s10.write(rc_angle);
}
void servo_init(){
  s9.attach(9);
  s10.attach(10);
  handle1(0);
  handle2(0); 
  delay(500);
}
