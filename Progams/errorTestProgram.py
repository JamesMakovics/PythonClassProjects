#Loading Screen
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops! That was not a number Try again!")

while True:
    try:
        strX = str(input("Please enter a yes or no: "))
        break
    except ValueError:
        print("Oops! That was not 'yes or no' Try again!")

while True:
    try:
        x = str(input("Please enter 'yes or no': "))
        if x.isdigit():
            print("Digit Found")
            continue
        else:
            break

    except ValueError:
        print("Oops! That was not 'yes or no' Try again!")
