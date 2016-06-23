#include <Servo.h>

#define led_pin_1 8
#define led_pin_2 9
#define led_pin_3 10
#define led_pin_4 11
#define led_pin_5 12

#define srv_pin_fr 2
#define srv_pin_fl 3
#define srv_pin_br 4
#define srv_pin_bl 5
#define srv_pin_sp 6

#define srv_trns_fr 22
#define srv_trns_fl 24
#define srv_trns_br 26
#define srv_trns_bl 28
#define srv_trns_sp 30

#define fr_close 105
#define fr_open  175
#define fl_close 170
#define fl_open  100
#define br_close 170
#define br_open  100
#define bl_close 105
#define bl_open  175
#define sp_cw    180
#define sp_ccw   0
#define sp_stop  95

Servo servo_fr;
Servo servo_fl;
Servo servo_br;
Servo servo_bl;
Servo servo_sp;

void setup() {
  Serial.begin(9600);
  for (int i = led_pin_1; i <= led_pin_5; i++) {
    pinMode(i, OUTPUT);
    digitalWrite(i, LOW);
  }
  for (int i = srv_trns_fr; i <= srv_trns_sp; i+=2) {
    pinMode(i, OUTPUT);
    digitalWrite(i, LOW);
  }
  servo_fr.attach(srv_pin_fr);
  servo_fl.attach(srv_pin_fl);
  servo_br.attach(srv_pin_br);
  servo_bl.attach(srv_pin_bl);
  servo_sp.attach(srv_pin_sp);
  
  servo_fr.write(fr_close);
  servo_fl.write(fl_close);
  servo_br.write(br_close);
  servo_bl.write(bl_close);
  
  delay(500);
  
  for (int i = srv_trns_fr; i <= srv_trns_sp; i+=2) {
    digitalWrite(i, HIGH);
  }
}

void loop() {
  if (Serial.available()) {
    char c = Serial.read();
    while(Serial.available() > 0) {
      Serial.read();
    }
    if (c == 'q') {
      digitalWrite(led_pin_1, HIGH);
    } else if (c == 'a') {
      digitalWrite(led_pin_1, LOW);
    } else if (c == 'w') {
      digitalWrite(led_pin_2, HIGH);
    } else if (c == 's') {
      digitalWrite(led_pin_2, LOW);
    } else if (c == 'e') {
      digitalWrite(led_pin_3, HIGH);
    } else if (c == 'd') {
      digitalWrite(led_pin_3, LOW);
    } else if (c == 'r') {
      digitalWrite(led_pin_4, HIGH);
    } else if (c == 'f') {
      digitalWrite(led_pin_4, LOW);
    } else if (c == 't') {
      digitalWrite(led_pin_5, HIGH);
    } else if (c == 'g') {
      digitalWrite(led_pin_5, LOW);
    } else if (c == 'i') {
      servo_fr.write(fr_open);
    } else if (c == 'k') {
      servo_fr.write(fr_close);
    } else if (c == 'o') {
      servo_fl.write(fl_open);
    } else if (c == 'l') {
      servo_fl.write(fl_close);
    } else if (c == 'p') {
      servo_br.write(br_open);
    } else if (c == ';') {
      servo_br.write(br_close);
    } else if (c == '[') {
      servo_bl.write(bl_open);
    } else if (c == '\'') {
      servo_bl.write(bl_close);
    } else if (c == 'z') {
      servo_sp.write(sp_cw);
    } else if (c == 'x') {
      servo_sp.write(sp_stop);
    } else if (c == 'c') {
      servo_sp.write(sp_ccw);
    }
  }
}
