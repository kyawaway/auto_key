#include <Servo.h>

Servo servo;
const int door_read_pin = 8;
int serial = 0;

void setup() {
  pinMode(door_read_pin,INPUT);
  Serial.begin(9600);

  servo.attach(9);
  servo.write(0);
  
}

void loop() { 
  
}