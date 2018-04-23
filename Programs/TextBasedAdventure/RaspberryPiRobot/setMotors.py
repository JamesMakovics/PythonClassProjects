import robotControllerMethods

def getDriveCommand(move):
    if move == 'Forward':
        robotControllerMethods.Forward()

    elif move == 'Backwards':
        robotControllerMethods.Backward()

    elif move == 'Left':
        robotControllerMethods.Left()

    elif move == 'Right':
        robotControllerMethods.Right()
