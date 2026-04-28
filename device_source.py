import serial
import time

class DeviceSource:
    """Класс источника питания"""

    def __init__(self, serial_port: serial.Serial):
        self.serial_port = serial_port

    def request_idn(self):
        """Возвращает строку IDN подключенного источника питания."""
        self.serial_port.write(b"*IDN?\n")
        if self.serial_port.is_open: 
            return self.serial_port.readline().decode('utf-8').strip()

    def connect(self):
        """Подключение устройства по указанному COM порту. Возвращает True в случае успеха."""
        try:
            #ser = serial.Serial(serial_port, 9600, timeout=1) #Open the serial port
            self.serial_port.open()
        except serial.SerialException: 
            return False
        except serial.SerialTimeoutException:
            return False
        else:
            return True

    def disconnect(self):
        """Очистить буферы и закрыть порт устройства"""
        if self.serial_port.is_open:
            self.serial_port.reset_input_buffer()
            self.serial_port.reset_output_buffer()
            self.serial_port.close()


if __name__ == '__main__':
    serial_port = serial.Serial()
    serial_port.port = "COM13"
    serial_port.baudrate = 9600
    serial_port.timeout = 1
    device = DeviceSource(serial_port)

    if device.connect():
        print("Подключено")
        print('ID: ', device.request_idn())
    else:
        print("Ошибка подключения")

    device.disconnect()