#include <EEPROM.h>
#include <LowPower.h>

#define JOYX A0
#define JOYY A1
#define BUTTON_A 2
#define BUTTON_B 3
#define BUTTON_C 4
#define BUTTON_D 5

const int THRESHOLD = 100;       // Umbral para detectar movimiento
const int ACTION_INTERVAL = 150; // Intervalo entre envíos (ms)

unsigned long lastActionTime = 0; // Marca de tiempo de la última acción

void setup() {
  // Configurar botones como entradas con pull-up
  int buttonPins[] = {BUTTON_A, BUTTON_B, BUTTON_C, BUTTON_D};
  for (int i = 0; i < 4; i++) {
    pinMode(buttonPins[i], INPUT_PULLUP);
  }

  Serial.begin(9600); // Inicializar comunicación serial
}

void loop() {
  if (millis() - lastActionTime >= ACTION_INTERVAL) {
    lastActionTime = millis();
    processJoystick();
    processButtons();
  }
}

// Procesar movimientos del joystick
void processJoystick() {
  int xValue = analogRead(JOYX);
  int yValue = analogRead(JOYY);

  if (xValue > 678 - THRESHOLD) Serial.println("Right");
  else if (xValue < THRESHOLD) Serial.println("Left");

  if (yValue > 678 - THRESHOLD) Serial.println("Forward");
  else if (yValue < THRESHOLD) Serial.println("Back");
}

// Procesar pulsaciones de los botones
void processButtons() {
  char commands[] = {'R', 'T', 'Y', 'U'};
  int buttonPins[] = {BUTTON_A, BUTTON_B, BUTTON_C, BUTTON_D};

  for (int i = 0; i < 4; i++) {
    if (digitalRead(buttonPins[i]) == LOW) {
      Serial.println(commands[i]);
    }
  }
}
