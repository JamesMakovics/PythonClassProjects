'''
imports
'''
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
import socket
import runMotors
import robotControlMethods
'''
Setup of GPIO
'''

MotorLeftBackward = 17 #in pin 11 on RPI 3
MotorLeftForward = 27 #in pin 13 on RPI 3
MotorRightForward = 22 #in pin 15 on RPI 3
MotorRightBackward = 23 #in pin 16 on RPI 3

'''
Init the GPIO pins
'''
GPIO.setup(MotorLeftForward, GPIO.OUT)
GPIO.setup(MotorLeftBackward, GPIO.OUT)
GPIO.setup(MotorRightForward, GPIO.OUT)
GPIO.setup(MotorRightBackward, GPIO.OUT)

UDP_IP = "192.168.1.30"
UDP_PORT = 5005
address = UDP_IP,UDP_PORT
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
while True:
    step, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    time, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    time = int(time)
    step = step.decode(encoding='UTF-8',errors='strict')
    runMotors.getDriveCommand(step,time)
