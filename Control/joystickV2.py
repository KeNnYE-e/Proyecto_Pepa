from serial import Serial
from time import sleep
import pyautogui

try:
    arduino = Serial(port='COM3', baudrate=9600, timeout=1)
    sleep(2)         
except Exception as e:
    print(f"Error connecting to Arduino: {e}")
    exit()

def process_data(data_str):
    # Mapa de los comandos recibidos desde Arduino a las teclas del teclado
    command_map = {
        "Right": "right",  # Movimiento joystick derecha
        "Left": "left",    # Movimiento joystick izquierda
        "Forward": "up",   # Movimiento joystick adelante
        "Back": "down",    # Movimiento joystick atrás
        "R": "r",          # Botón A
        "T": "t",          # Botón B
        "Y": "y",          # Botón C
        "U": "u",          # Botón D
    }

    if data_str in command_map:
        pyautogui.press(command_map[data_str])

while True:
    try:
        if arduino.in_waiting > 0:  
            data = arduino.readline().decode().strip()
            if data:
                process_data(data)
        else:
            sleep(0.1)  
    except Exception as e:
        print(f"Error processing data: {e}")
        break
