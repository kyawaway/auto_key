#include <Servo.h>

Servo servo;
const int door_read_pin = 8;
int door_status = 0;

void setup() {
  pinMode(door_read_pin,INPUT);
  Serial.begin(9600);

  servo.attach(9);
  servo.write(0);
  
}



void loop() {
  byte var;
  var = Serial.read();
  switch(var){
    case '0':
      servo.write(0);
      Serial.write(0);
      delay(10000);
      
      break;
    case '1':
      servo.write(90);
      Serial.write(1);
      
      break;
    default:
      break;
  }

  int door_digital_read = digitalRead(door_read_pin);

  if(door_digital_read > 0){
    delay(100);
    Serial.print(1);
    servo.write(90);
    delay(100);
  }else{
    Serial.print(0);
    servo.write(0);
    delay(100);
  }

  
