import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

Motor1A = 17
Motor1B = 27

GPIO.setup(Motor1A, GPIO.OUT)
GPIO.setup(Motor1B, GPIO.OUT)

print("Testing motor")
GPIO.output(Motor1A, True)#Sets right motor to true/on
GPIO.output(Motor1B, False)#Sets left motor to false/off

time.sleep(2)#Waits for 2 seconds

print("Stopping Test")
GPIO.output(Motor1A, False)#Turns right motor off

GPIO.cleanup()
