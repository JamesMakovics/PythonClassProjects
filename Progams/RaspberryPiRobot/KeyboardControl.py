#Simple Keyboard control through the console
'''
imports
'''
import curses
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
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

#Get the curses window, turn off echoing of keyboard to screen, turn on
#instant (no waiting) key response,  and use special values for cursor keys

screen = curses.initscr()
curses.noecho()
curses.cbreak()
srceen.keypad(True)

try:
    while True:
        char = screen.getch()
        if char == ord('q'): #Quits the program
            break
        elif char == curses.KEY_UP: #Moves Robot forward
            GPIO.output(MotorLeftForward, True)
            GPIO.output(MotorRightForward, True)
            GPIO.output(MotorLeftBackward, False)
            GPIO.output(MotorRightBackward, False)
            print("UP")
        elif char == curses.KEY_DOWN:
            GPIO.output(MotorLeftForward, False)
            GPIO.output(MotorRightForward, False)
            GPIO.output(MotorLeftBackward, True)
            GPIO.output(MotorRightBackward, True)
            print("DOWN")
        elif char == curses.KEY_LEFT:
            GPIO.output(MotorLeftForward, True)
            GPIO.output(MotorRightForward, False)
            GPIO.output(MotorLeftBackward, False)
            GPIO.output(MotorRightBackward, False)
            print("LEFT")
        elif char == curses.KEY_RIGHT:
            GPIO.output(MotorLeftForward, False)
            GPIO.output(MotorRightForward, True)
            GPIO.output(MotorLeftBackward, False)
            GPIO.output(MotorRightBackward, False)
            print("RIGHT")
        elif char == ord('s'):
            GPIO.output(MotorLeftForward, False)
            GPIO.output(MotorRightForward, False)
            GPIO.output(MotorLeftBackward, False)
            GPIO.output(MotorRightBackward, False)
            print("STOP")
finally:
    #Close down curses properly,inc turn echo back on!
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
    GPIO.cleanup()
