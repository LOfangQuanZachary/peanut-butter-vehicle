from cmath import cos, sin
import string
import numpy as np
import RPi.GPIO as GPIO
import time
import serial
import bezier
from pygame import clock
SpeedX = 0
SpeedY = 0
totalDisplacemenX = 0
totalDisplacemenY = 0
totalDisplacementEnd = 0
speedX = 0
speedY = 0
i = 0
beginButton = 5
serialInput = ""
bezierPoints = []
framedelay = 0.1
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
    GPIO.cleanup()
    serialTransmission("Begin")
    bezierPoints = get_instructions_for_bezier()
    while serialTransmission("") != "StartingRun":
        time.sleep(0.01)
#shut down code
def shutDown():
    serialTransmission("kill")
#main body of code
def main():
    setUpCode()
    drivingCode()
def drivingCode():
    while totalDisplacementEnd != bezierPoints[i][1]:
        clock.tick()
        arr = accelVectorFunni()
        X = arr[0]
        Y = arr[1] 
        Xdisplacement = pow(framedelay, 2) * X + (speedX * framedelay)
        Ydisplacement = pow(framedelay, 2) * Y + (speedY * framedelay)
        speedX = speedX + (X * framedelay)
        speedY = speedY + (Y * framedelay)
        totalDisplacemenX = Xdisplacement + totalDisplacemenX
        totalDisplacemenY = Ydisplacement + totalDisplacemenY
        totalDisplacementEnd = np.sqrt(pow(totalDisplacemenX, 2) + pow(totalDisplacemenY, 2))
        serialTransmission(string("50" + "50" + bezierPoints[i][0]))
def get_instructions_for_bezier():
    pass


def accelVectorFunni():
    pass
    
main()
def drivingLoop():
    SpeedX = 0
    SpeedY = 0
    for i in(len(bezierPoints)):
        totalDisplacemenX = 0
        totalDisplacemenY = 0
        drivingCode(i)
