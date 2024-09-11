#define joyx A0
#define joyy A1
#define button_a 2
#define button_b 3
#define button_c 4
#define button_d 5

int time_ = 150;
int threshold = 100;

void setup() 
{
  pinMode(button_a, INPUT);
  pinMode(button_b, INPUT);
  pinMode(button_c, INPUT);
  pinMode(button_d, INPUT);
  Serial.begin(9600);
}

void loop() 
{
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

  // Mapeo de los botones para responder preguntas
  // Botón A -> 'R'
  if (digitalRead(button_a) == LOW) {
    Serial.println("R");
    delay(time_);
  }

  // Botón B -> 'T'
  if (digitalRead(button_b) == LOW) {
    Serial.println("T");
    delay(time_);
  }

  // Botón C -> 'Y'
  if (digitalRead(button_c) == LOW) {
    Serial.println("Y");
    delay(time_);
  }

  // Botón D -> 'U'
  if (digitalRead(button_d) == LOW) {
    Serial.println("U");
    delay(time_);
  }
}
