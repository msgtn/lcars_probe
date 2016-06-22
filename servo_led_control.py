import serial

a = serial.Serial('/dev/ttyACM0', 9600)
while(1):
    a.write(raw_input('Enter: '))