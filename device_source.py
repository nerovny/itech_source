# Класс источника питания, подключенного через COM порт
#
import serial
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