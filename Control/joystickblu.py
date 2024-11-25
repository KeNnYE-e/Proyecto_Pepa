from serial import Serial
from time import sleep
import pyautogui


class BluetoothController:
    def __init__(self, port, baudrate=38400, timeout=1):
        try:
            self.bluetooth = Serial(port=port, baudrate=baudrate, timeout=timeout)
            sleep(2)  # Esperar para estabilizar la conexión
            print(f"Conexión establecida en {port}")
        except Exception as e:
            print(f"Error al conectar con el módulo Bluetooth HC-05: {e}")
            exit()

    def read_data(self):
        if self.bluetooth.in_waiting > 0:
            try:
                data = self.bluetooth.readline().decode().strip()
                return data
            except Exception as e:
                print(f"Error al leer datos: {e}")
        return None

    def close_connection(self):
        self.bluetooth.close()
        print("Conexión Bluetooth cerrada.")


class CommandProcessor:
    COMMAND_MAP = {
        "Right": "right",   # Movimiento joystick derecha
        "Left": "left",     # Movimiento joystick izquierda
        "Forward": "up",    # Movimiento joystick adelante
        "Back": "down",     # Movimiento joystick atrás
        "R": "r",           # Botón A
        "T": "t",           # Botón B
        "Y": "y",           # Botón C
        "U": "u",           # Botón D
    }

    @staticmethod
    def process_command(command):
        if command in CommandProcessor.COMMAND_MAP:
            pyautogui.press(CommandProcessor.COMMAND_MAP[command])
            print(f"Comando procesado: {command}")


def main():
    bluetooth_controller = BluetoothController(port='COM7')

    try:
        while True:
            data = bluetooth_controller.read_data()
            if data:
                print(f"Dato recibido: {data}")  # Debug para observar los datos recibidos
                CommandProcessor.process_command(data)
            else:
                sleep(0.1)  # Reducir uso de CPU
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario.")
    finally:
        bluetooth_controller.close_connection()


if __name__ == "__main__":
    main()
