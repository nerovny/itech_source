import serial
import time


def device_request_idn(ser):
    """Request the device ID on the 'ser' port"""
    ser.write(b"*IDN?\n")
    if ser.is_open:
        byte_str = ser.readline()
    return byte_str.decode('utf-8').strip()


if __name__ == '__main__':
    ser = serial.Serial('COM13', 9600, timeout=1) #Open the serial port
    if ser.is_open:
        print('Port:', ser.name)
    print('Device ID: ', device_request_idn(ser)) #Get the device ID

    ser.reset_input_buffer()
    time.sleep(0.1)
    ser.reset_output_buffer()
    time.sleep(0.1)
    ser.close()