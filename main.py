import serial
import device_source


if __name__ == '__main__':
    serial_port = serial.Serial()
    serial_port.port = "COM13"
    serial_port.baudrate = 9600
    serial_port.timeout = 1
    device = device_source.DeviceSource(serial_port)

    if device.connect():
        print("Подключено")
        print('ID: ', device.request_idn()) # Например, ITECH Ltd.,IT6513C,800637011797810002,0.41P-0.53P
    else:
        print("Ошибка подключения")

    device.disconnect()