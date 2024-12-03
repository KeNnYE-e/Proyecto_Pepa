#include <EEPROM.h>

#define joyx A0
#define joyy A1
#define button_a 2
#define button_b 3
#define button_c 4
#define button_d 5

int time_ = 150;
int threshold = 100;

void setup() {
  pinMode(button_a, INPUT_PULLUP); // Configura botones con resistencia pull-up interna
  pinMode(button_b, INPUT_PULLUP);
  pinMode(button_c, INPUT_PULLUP);
  pinMode(button_d, INPUT_PULLUP);
  
  Serial.begin(9600); // Comunicación con el módulo HC-05
}

void loop() {
  int xValue = analogRead(joyx);
  int yValue = analogRead(joyy);

  // Movimientos del joystick
  if (xValue > (1023 - threshold)) {
    Serial.println("Right");
    delay(time_);
  } else if (xValue < threshold) {
    Serial.println("Left");
    delay(time_);
  }

  if (yValue > (1023 - threshold)) {
    Serial.println("Forward");
    delay(time_);
  } else if (yValue < threshold) {
    Serial.println("Back");
    delay(time_);
  }

  // Mapeo de los botones
  if (digitalRead(button_a) == LOW) { // Botón A
    Serial.println("R");
    delay(time_);
  }

  if (digitalRead(button_b) == LOW) { // Botón B
    Serial.println("T");
    delay(time_);
  }

  if (digitalRead(button_c) == LOW) { // Botón C
    Serial.println("Y");
    delay(time_);
  }

  if (digitalRead(button_d) == LOW) { // Botón D
    Serial.println("U");
    delay(time_);
  }
}
