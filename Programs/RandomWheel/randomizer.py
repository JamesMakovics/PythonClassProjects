#Random Wheel program
import random, time, vlc

nameList = []

def namesInput(nameList):
    while True:
        checkName = input(str("Please enter a name or type 'done' to stop: "))
        if checkName == "done":
            print("Here are the names: ", nameList, "\n")
            break
        else:
            nameList.append(checkName)

def spin(nameList):
    if len(nameList) == 0:
        print("Invalid ammount of names")
    else:
        print("Generating names:")
        while True:
            randNum = random.randint(0,len(nameList) - 1)
            print(nameList[randNum])
            nameList.pop(randNum)
            if len(nameList) == 0:
                break
            else:
                pass

print("Welcome to random name spinner! \n")

namesInput(nameList)

spin(nameList)
