
def sendDriveCommand(direction,methodTimeout,direction):
    if direction == 'forward':
        robotControlMethods.Forward(methodTimeout,direction)
        if robotControlMethods.Forward(methodTimeout,direction) == True:
            return True
    elif direction == 'backwards':
        robotControlMethods.Backward(methodTimeout,direction)
        if robotControlMethods.Backward(methodTimeout,direction) == True:
            return True
    elif direction == 'left':
        robotControlMethods.left(methodTimeout,direction)
        if robotControlMethods.left(methodTimeout,direction) == True:
            return True
    elif direction == 'right':
        robotControlMethods.right(methodTimeout,direction)
        if robotControlMethods.right(methodTimeout,direction) == True:
            return True
