#include <Servo.h>
#define srv_pin 9
#define trns_pin 7

Servo servo;
int pos = 0;
bool trns_state = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(trns_pin, OUTPUT);
  digitalWrite(trns_pin, trns_state);
  servo.attach(srv_pin);
}

void loop() {
  for(pos = 0; pos <= 180; pos += 1) // goes from 0 degrees to 180 degrees 
  {                                  // in steps of 1 degree'
    if (Serial.available()) {
      while (Serial.available()) {
        Serial.read();
      }
      digitalWrite(trns_pin, !digitalRead(trns_pin));
      Serial.println(digitalRead(trns_pin));
//      digitalWrite(trns_pin, !trns_state);
//      trns_state = !trns_state;
//      Serial.println(trns_state);
    }
    servo.write(pos);              // tell servo to go to position in variable 'pos' 
    delay(15);                       // waits 15ms for the servo to reach the position 
  }
//  Serial.println(180);
  for(pos = 180; pos>=0; pos-=1)     // goes from 180 degrees to 0 degrees 
  {                   
    if (Serial.available()) {
      while (Serial.available()) {
        Serial.read();
      }
      digitalWrite(trns_pin, !digitalRead(trns_pin));
      Serial.println(digitalRead(trns_pin));
//      digitalWrite(trns_pin, !trns_state);
//      trns_state = !trns_state;
//      Serial.println(trns_state);
    }              
    servo.write(pos);              // tell servo to go to position in variable 'pos' 
    delay(15);                       // waits 15ms for the servo to reach the position 
  } 
//  Serial.println(0);
}
