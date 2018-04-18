
def getDriveCommand(step,time):
    if step == 'forward':
        robotControlMethods.Forward(time)

    elif step == 'backwards':
        robotControlMethods.Backward(time)

    elif step == 'left':
        robotControlMethods.left(time)

    elif step == 'right':
        robotControlMethods.right(time)
