import serial,time

def open_key():
    ser = serial.Serial('COM6',9600)
    ser.write(b"1")

def get_status():
    ser = serial.Serial('COM6',9600)
    key_status = ser.read()
    return key_status

