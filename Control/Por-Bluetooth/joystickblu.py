from serial import Serial
from serial.tools import list_ports
from time import sleep
import pyautogui


class BluetoothController:
    def __init__(self, baudrate=38400, timeout=1):
        self.bluetooth = None
        self.port = self.auto_detect_port()
        if self.port is None:
            print("No se encontró un módulo Bluetooth HC-05.")
            exit()
        try:
            self.bluetooth = Serial(port=self.port, baudrate=baudrate, timeout=timeout)
            sleep(2)  # Esperar para estabilizar la conexión
            print(f"Conexión establecida en {self.port}")
        except Exception as e:
            print(f"Error al conectar con el módulo Bluetooth HC-05 en {self.port}: {e}")
            exit()

    @staticmethod
    def auto_detect_port():
        """Detecta automáticamente el puerto COM del módulo Bluetooth HC-05."""
        print("Buscando puerto del módulo Bluetooth HC-05...")
        ports = list_ports.comports()
        for port in ports:
            if "HC-05" in port.description or "Bluetooth" in port.description:
                print(f"Módulo Bluetooth encontrado en {port.device}")
                return port.device
        print("No se encontró un módulo Bluetooth HC-05.")
        return None

    def read_data(self):
        if self.bluetooth and self.bluetooth.in_waiting > 0:
            try:
                data = self.bluetooth.readline().decode().strip()
                return data
            except Exception as e:
                print(f"Error al leer datos: {e}")
        return None

    def close_connection(self):
        if self.bluetooth:
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
    bluetooth_controller = BluetoothController()  # No se especifica puerto explícito

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
