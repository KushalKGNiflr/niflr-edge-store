import serial

# configure the serial port
ser = serial.Serial('/dev/ttyt4', 9600) # replace with the appropriate port name and baud rate

while True:
    # read a line of data from the serial port
    data = ser.readline().decode('utf-8').rstrip()

    # print the received data
    print(data)
