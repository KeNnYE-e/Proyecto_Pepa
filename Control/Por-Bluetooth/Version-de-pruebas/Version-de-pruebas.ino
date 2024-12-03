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
  // Configurar pines de botones como entradas con resistencias pull-up internas
  pinMode(BUTTON_A, INPUT_PULLUP);
  pinMode(BUTTON_B, INPUT_PULLUP);
  pinMode(BUTTON_C, INPUT_PULLUP);
  pinMode(BUTTON_D, INPUT_PULLUP);

  // Configurar pines del joystick como entradas
  pinMode(JOYX, INPUT);
  pinMode(JOYY, INPUT);

  // Inicializar comunicación serial
  Serial.begin(9600);
}

void loop() {
  unsigned long currentMillis = millis();

  // Comprobar si ha pasado suficiente tiempo desde la última acción
  if (currentMillis - lastActionTime >= ACTION_INTERVAL) {
    lastActionTime = currentMillis;

    // Leer valores del joystick
    int xValue = analogRead(JOYX);
    int yValue = analogRead(JOYY);

    // Enviar comandos según el movimiento del joystick
    processJoystick(xValue, yValue);

    // Enviar comandos según los botones presionados
    processButtons();
  }
}

// Procesar movimientos del joystick
void processJoystick(int xValue, int yValue) {
  if (xValue > (678 - THRESHOLD)) {
    Serial.println("Right");
  } else if (xValue < THRESHOLD) {
    Serial.println("Left");
  }

  if (yValue > (678 - THRESHOLD)) {
    Serial.println("Forward");
  } else if (yValue < THRESHOLD) {
    Serial.println("Back");
  }
}

// Procesar pulsaciones de los botones
void processButtons() {
  if (digitalRead(BUTTON_A) == LOW) {
    Serial.println("R"); // Botón A
  }
  if (digitalRead(BUTTON_B) == LOW) {
    Serial.println("T"); // Botón B
  }
  if (digitalRead(BUTTON_C) == LOW) {
    Serial.println("Y"); // Botón C
  }
  if (digitalRead(BUTTON_D) == LOW) {
    Serial.println("U"); // Botón D
  }
}
