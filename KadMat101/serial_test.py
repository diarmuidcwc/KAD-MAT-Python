import serial
import time

def main():
    ser = serial.Serial('/dev/ttyS1', 19200, timeout=1)
    for count in range(1000):
	character = chr(count%128)
        ser.write(character)
        time.sleep(1)

    ser.close()


if __name__ == '__main__':
    main()

