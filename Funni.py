import RPi.GPIO as GPIO
import threading
import time
import serial
beginButton = 5
serialInput = ""
#start of serial transmission setup
if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.reset_input_buffer()
#Serial read/write function
def serialTransmission(toTransmit):
    #function will return any inputs
    if serial.in_waiting > 0:
        serialInput = ser.readline().decode("utf-8").rstrip()
    else:
        serialInput = ""
    if toTransmit != "":
        ser.write(toTransmit + "/n".encode("utf-8"))
    ser.reset_input_buffer()
    return serialInput
#setUp and initialization code
def setUpCode():
    GPIO.pinMode(5, GPIO.OUTPUT)
    GPIO.cleanup()
    serialTransmission("Begin")
    while serialTransmission("") != "StartingRun":
        time.sleep(0.01)
#self driving functions
def selfDrivingCode(gyroAngle, currentMotorSpeedA, currentMotorSpeedB):
    pass
#shut down code
def shutDown():
    serialTransmission("kill")
#main body of code
def main():
    setUpCode()
main()

