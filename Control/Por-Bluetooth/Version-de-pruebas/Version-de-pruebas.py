import time
from serial import Serial
import pyautogui


class BluetoothController:
    def __init__(self, ports, baudrate=9600, timeout=0.01):
        """
        Inicializa la conexión Bluetooth con el primer puerto disponible.
        """
        self.bluetooth = next(
            (Serial(port, baudrate, timeout=timeout) for port in ports if self._try_port(port, baudrate, timeout)), 
            None
        )
        if not self.bluetooth:
            raise ConnectionError("No se pudo establecer conexión en ningún puerto.")

    @staticmethod
    def _try_port(port, baudrate, timeout):
        """
        Intenta abrir un puerto y devuelve True si tiene éxito.
        """
        try:
            Serial(port, baudrate, timeout=timeout).close()
            return True
        except:
            return False

    def read_data(self):
        """
        Devuelve datos recibidos, o None si no hay datos disponibles.
        """
        if self.bluetooth and self.bluetooth.in_waiting:
            try:
                return self.bluetooth.readline().decode('utf-8').strip()
            except Exception as e:
                print(f"Error al leer datos: {e}")
        return None

    def close(self):
        """
        Cierra la conexión Bluetooth.
        """
        if self.bluetooth:
            self.bluetooth.close()
            print("Conexión cerrada.")


class CommandProcessor:
    COMMAND_MAP = {
        "Right": "right", "Left": "left", "Forward": "up", "Back": "down",
        "R": "r", "T": "t", "Y": "y", "U": "u"
    }

    @classmethod
    def process(cls, command):
        """
        Procesa un comando según el mapa de comandos.
        """
        action = cls.COMMAND_MAP.get(command)
        if action:
            pyautogui.press(action)
            print(f"Comando procesado: {command}")
        else:
            print(f"Comando desconocido: {command}")


def main():
    """
    Bucle principal para manejar la conexión y los comandos.
    """
    ports = ['COM7']  # Ajustar según el sistema operativo
    try:
        controller = BluetoothController(ports)
        print("Bluetooth listo.")
        while True:
            if data := controller.read_data():
                CommandProcessor.process(data)
            time.sleep(0.01)
    except (ConnectionError, KeyboardInterrupt) as e:
        print(f"Finalizando: {e}")
    finally:
        controller.close()


if __name__ == "__main__":
    main()
