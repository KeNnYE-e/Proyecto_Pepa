#define JOYX A0
#define JOYY A1
#define BUTTON_A 2
#define BUTTON_B 3
#define BUTTON_C 4
#define BUTTON_D 5

const int TIME_DELAY = 150;
const int THRESHOLD = 100;

void setup() {
  pinMode(BUTTON_A, INPUT);
  pinMode(BUTTON_B, INPUT);
  pinMode(BUTTON_C, INPUT);
  pinMode(BUTTON_D, INPUT);

  Serial.begin(9600);  // Comunicación con HC-05
}

void loop() {
  int xValue = analogRead(JOYX);
  int yValue = analogRead(JOYY);

  // Movimientos del joystick
  checkJoystickMovement(xValue, yValue);

  // Botones
  checkButtonPress(BUTTON_A, "R");
  checkButtonPress(BUTTON_B, "T");
  checkButtonPress(BUTTON_C, "Y");
  checkButtonPress(BUTTON_D, "U");
}

void checkJoystickMovement(int xValue, int yValue) {
  if (xValue > (1023 - THRESHOLD)) {
    sendCommand("Right");
  } else if (xValue < THRESHOLD) {
    sendCommand("Left");
  }

  if (yValue > (1023 - THRESHOLD)) {
    sendCommand("Forward");
  } else if (yValue < THRESHOLD) {
    sendCommand("Back");
  }
}

void checkButtonPress(int buttonPin, const char* command) {
  if (digitalRead(buttonPin) == LOW) {
    sendCommand(command);
  }
}

void sendCommand(const char* command) {
  Serial.println(command);
  delay(TIME_DELAY);
}
