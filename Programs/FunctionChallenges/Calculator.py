#Calculator Program

def intro():
    print("Welcome to the calculator program!\n")
    dispFunctions()

def dispFunctions():
    getOp = int(input("Press 1 - to add numbers\nPress 2 - to subtract numbers\nPress 3 - to multiply numbers\nPress 4 - to divide numbers\n"))
    getNums(getOp)

def getNums(getOp):
    if getOp == 1:
        try:
            num1 = float(input("Please enter first number to add: "))
            num2 = float(input("Please enter second number to add: "))
        except ValueError:
            print("Please try again!")
            getNums(getOp)
        print("Your total is: ", add(num1,num2))
        anotherCal()
    elif getOp == 2:
        try:
            num1 = float(input("Please enter first number to subtract: "))
            num2 = float(input("Please enter second number to subtract: "))
        except ValueError:
            print("Please try again!")
            getNums(getOp)
        print("Your total is: ", subtract(num1,num2))
        anotherCal()
    elif getOp == 3:
        try:
            num1 = float(input("Please enter first number to multiply: "))
            num2 = float(input("Please enter second number to multiply: "))
        except ValueError:
            print("Please try again!")
            getNums(getOp)
        print("Your total is: ", multiply(num1,num2))
        anotherCal()
    elif getOp == 4:
        try:
            num1 = float(input("Please enter first number to divide: "))
            num2 = float(input("Please enter second number to divide: "))
        except ValueError:
            print("Please try again!")
            getNums(getOp)

        print("Your total is: ", divide(num1,num2))
        anotherCal()

    else:
        print("Please enter a valid number")
        dispFunctions()

def anotherCal():
    usrCal = str(input("Would you like to calculate another number?: "))
    while True:
        if usrCal.lower() == "yes" or usrCal.lower() == "no":
            break
        else:
            print("Try again")

    if usrCal.lower() == "yes":
        dispFunctions()
    elif usrCal.lower() == "no":
        print("Goodbye")

def multiply(num1,num2):
    return num1 * num2

def divide(num1,num2):
    return num1 / num2


def add(num1,num2):
    return num1 + num2

def subtract(num1,num2):
    return num1 - num2


intro()
