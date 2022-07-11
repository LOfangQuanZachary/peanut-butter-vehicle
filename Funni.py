import RPi.GPIO as GPIO
import threading
import time
import serial
beginButton = 5
serialInput = ""
def setUpCode():
    GPIO.pinMode(5, GPIO.OUTPUT)
    if __name__ == '__main__':
        ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
        ser.reset_input_buffer()
    GPIO.cleanup()
def selfDrivingCode(gyroAngle, currentMotorSpeedA, currentMotorSpeedB):
    pass
def serialTransmission(toTransmit):
    #function will return any inputs
    if serial.in_waiting > 0:
        serialInput = serial.readline().decode("utf-8").rstrip()
    else:
        serianInput = ""
    serial.write(toTransmit + "/n".encode("utf-8"))
    return serialInput

def main():
    setUpCode()

