import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

'''
Set GPIO pins in BCM mode on Raspberry Pi 3
'''
MotorLeftForward = 17 #in pin 11 on RPI 3
MotorLeftBackward = 27 #in pin 13 on RPI 3
MotorRightForward = 22 #in pin 15 on RPI 3
MotorRightBackward = 23 #in pin 16 on RPI 3
'''
Init the GPIO pins
'''
GPIO.setup(MotorLeftForward, GPIO.OUT)
GPIO.setup(MotorLeftBackward, GPIO.OUT)
GPIO.setup(MotorRightForward, GPIO.OUT)
GPIO.setup(MotorRightBackward, GPIO.OUT)

'''
Runs motor test for left motor
'''
print("Testing motor")
GPIO.output(MotorLeftForward, True)#Sets left forwards motor to true/on
GPIO.output(MotorLeftBackward, False)#Sets left backwards motor to false/off

time.sleep(2)#Waits for 2 seconds

'''
Stops the test
'''
print("Stopping Test")
GPIO.output(MotorLeftForward, False)#Turns left motor off

'''
Shuts down the pins and allows for re-init of pins next run
'''
GPIO.cleanup()
