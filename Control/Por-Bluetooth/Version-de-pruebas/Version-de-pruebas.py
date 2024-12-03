import time
from serial import Serial
import pyautogui


class BluetoothController:
    def __init__(self, ports, baudrate=9600, timeout=0.01):
        """
        Controlador Bluetooth optimizado para conexiones rápidas.
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
        Lee datos si están disponibles y los devuelve como una cadena limpia.
        """
        if self.bluetooth and self.bluetooth.in_waiting > 0:
            try:
                data = self.bluetooth.readline().decode('utf-8').strip()
                return data
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
        Procesa un comando si está mapeado en COMMAND_MAP.
        """
        action = CommandProcessor.COMMAND_MAP.get(command)
        if action:
            pyautogui.press(action)
            print(f"Comando procesado: {command}")
        else:
            print(f"Comando desconocido: {command}")


class Logger:
    """
    Clase para registrar eventos y simplificar depuración.
    """
    @staticmethod
    def log(message, level="INFO"):
        levels = {"INFO": "[INFO]", "ERROR": "[ERROR]", "DEBUG": "[DEBUG]"}
        print(f"{levels.get(level, '[INFO]')} {message}")


def main():
    """
    Bucle principal para leer datos y procesar comandos.
    """
    ports = ['COM7']  # Cambia los puertos según tu sistema operativo
    bluetooth_controller = BluetoothController(ports=ports)

    try:
        while True:
            data = bluetooth_controller.read_data()
            if data:
                Logger.log(f"Datos recibidos: {data}", level="DEBUG")
                CommandProcessor.process_command(data)
            
            # Reducir el tiempo de espera para una respuesta más rápida
            time.sleep(0.005)
    except KeyboardInterrupt:
        Logger.log("Programa interrumpido por el usuario.", level="INFO")
    finally:
        bluetooth_controller.close_connection()


if __name__ == "__main__":
    main()
