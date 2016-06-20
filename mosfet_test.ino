#define led_pin 7

void setup() {
  Serial.begin(9600);
  pinMode(led_pin, OUTPUT);
  digitalWrite(led_pin, LOW);
}

void loop() {
  if (Serial.available()) {
    char c = Serial.read();
    while(Serial.available() > 0) {
      Serial.read();
    }
    // p turns it on
    if (c == 112) {
      digitalWrite(led_pin, HIGH);
    // ; turns it off
    } else if (c == 59) {
      digitalWrite(led_pin, LOW);
    // anything else turns it off
    } else {
      digitalWrite(led_pin, LOW);
    }
  }
}
