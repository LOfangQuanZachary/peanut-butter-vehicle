from cmath import cos, sin
import numpy as np
import RPi.GPIO as GPIO
import threading
import time
import serial
import bezier
totalDisplacemenX = 0
totalDisplacemenY = 0
totalDisplacementEnd = 0
i = 0
beginButton = 5
serialInput = ""
bezierPoints = []
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
        arr = accelVectorFunni()
        X = arr[0]
        Y = arr[1]
        Xdisplacement = pow(0.1, 2) * X
        Ydisplacement = pow(0.1, 2) * Y
        totalDisplacemenX = Xdisplacement + totalDisplacemenX
        totalDisplacemenY = Ydisplacement + totalDisplacemenY
        totalDisplacementEnd = np.sqrt(pow(totalDisplacementX, 2) + pow(totalDisplacemenY, 2))

def get_instructions_for_bezier():
    pass


def accelVectorFunni():
    pass
    
main()
def drivingLoop():
    for i in(len(bezierPoints)):
        totalDisplacemenX = 0
        totalDisplacemenY = 0
        drivingCode(i)
