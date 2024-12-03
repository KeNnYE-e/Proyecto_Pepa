import time
from serial import Serial
import pyautogui


class BluetoothController:
    def __init__(self, ports, baudrate=38400, timeout=0.01):
        """
        Controlador Bluetooth optimizado para bajo consumo de CPU.
        Intenta conectar automáticamente a uno de los puertos proporcionados.
        """
        self.bluetooth = None
        for port in ports:
            try:
                self.bluetooth = Serial(port=port, baudrate=baudrate, timeout=timeout)
                print(f"Conexión establecida en {port}")
                break
            except Exception as e:
                print(f"No se pudo conectar en {port}: {e}")
        
        if not self.bluetooth:
            print("No se pudo establecer conexión en ninguno de los puertos.")
            exit()

    def read_data(self):
        """
        Lee datos si están disponibles y los devuelve como una cadena.
        """
        if self.bluetooth and self.bluetooth.in_waiting > 0:
            try:
                return self.bluetooth.readline().decode().strip()
            except Exception as e:
                print(f"Error al leer datos: {e}")
        return None

    def close_connection(self):
        """
        Cierra la conexión Bluetooth.
        """
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
        """
        Procesa un comando si está mapeado.
        """
        action = CommandProcessor.COMMAND_MAP.get(command)
        if action:
            pyautogui.press(action)
            print(f"Comando procesado: {command}")


def main():
    """
    Bucle principal para leer datos y procesar comandos.
    """
    # Lista de puertos disponibles. Agrega aquí los puertos que deseas probar.
    ports = ['COM7']

    # Inicializa el controlador Bluetooth con los puertos disponibles.
    bluetooth_controller = BluetoothController(ports=ports)

    try:
        while True:
            # Lee datos del Bluetooth
            data = bluetooth_controller.read_data()
            if data:
                CommandProcessor.process_command(data)
            
            # Espera para reducir la carga de la CPU
            time.sleep(0.01)  # Ajusta este valor según sea necesario
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario.")
    finally:
        bluetooth_controller.close_connection()


if __name__ == "__main__":
    main()
