import robotControlMethods

def getDriveCommand(step,time):
    if step == 'forward':
        robotControlMethods.Forward(time)

    elif step == 'backwards':
        robotControlMethods.Backward(time)

    elif step == 'left':
        robotControlMethods.Left(time)

    elif step == 'right':
        robotControlMethods.Right(time)
