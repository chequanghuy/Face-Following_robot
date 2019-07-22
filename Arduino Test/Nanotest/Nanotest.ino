#include <SoftwareSerial.h>

SoftwareSerial myser(3,2); //RX - TX

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  myser.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (myser.available() > 0){
    int data = myser.read();
    Serial.println(data);
  }
}
