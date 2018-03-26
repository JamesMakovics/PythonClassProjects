import RPi.GPIO as GPIO, time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)

counter = 0

while counter  < 10:
    time.sleep(2)
    GPIO.output(17, True)
    time.sleep(2)
    GPIO.output(17, False)
    counter += 1
    time.sleep(2)

GPIO.cleanup()
