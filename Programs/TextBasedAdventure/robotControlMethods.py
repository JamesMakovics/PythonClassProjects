#This manages the Pi from the server side

def init(): #sets all the motors to off
    GPIO.output(MotorLeftForward, False)
    GPIO.output(MotorRightForward, False)
    GPIO.output(MotorLeftBackward, False)
    GPIO.output(MotorRightBackward, False)

def Forward(time):#makes the robot go forward
    GPIO.output(MotorLeftForward, True)
    GPIO.output(MotorRightForward, True)
    GPIO.output(MotorLeftBackward, False)
    GPIO.output(MotorRightBackward, False)
    time.sleep(time)
    Stop()

def Backward(time):#makes the robot go backwards
    GPIO.output(MotorLeftForward, False)
    GPIO.output(MotorRightForward, False)
    GPIO.output(MotorLeftBackward, True)
    GPIO.output(MotorRightBackward, True)
    time.sleep(time)
    Stop()

def Right(time):#makes the robot go left
    GPIO.output(MotorLeftForward, True)
    GPIO.output(MotorRightForward, False)
    GPIO.output(MotorLeftBackward, False)
    GPIO.output(MotorRightBackward, False)
    time.sleep(time)
    Stop()

def Left(time):#makes the robot go right
    GPIO.output(MotorLeftForward, False)
    GPIO.output(MotorRightForward, True)
    GPIO.output(MotorLeftBackward, False)
    GPIO.output(MotorRightBackward, False)
    time.sleep(time)
    Stop()

def Stop():#makes the robot motors stop
    GPIO.output(MotorLeftForward, False)
    GPIO.output(MotorRightForward, False)
    GPIO.output(MotorLeftBackward, False)
    GPIO.output(MotorRightBackward, False)
    isFinished()

def isFinished():
    return True
