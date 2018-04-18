#This manages the game from the client side
import pygame
import socket
import random
import time
stepNum = 0
incorrectCount = 0
choice = ""

stepsForMaze = ["forward"] #Just a place holder
motorTimeForSteps = [1,1] #Just a place holder


mathQuestions = ["Whats 9+10?","Find the value of 3x+9=0","What is the factor of 3x^2+6x+3","","",""]
mathAnswers = ["21","3",]

scienceQuestions = [1,1]
scienceAnswers = [1,1]

englishQuestions = [1,1]
englishAnswers = [1,1]


gameFinished = False

def runGame():
    if gameFinished == False:
        return True
    else:
        return False

def intro():
    global choice
    print("Hello")
    time.sleep(.5)
    print("Welcome to MazeCraze")
    time.sleep(.5)
    print("You will need to answer questions in order to move the robot")
    time.sleep(.5)
    print("You have three topics to choose from:")
    print("Math")
    print("Science")
    print("English")
    while True:
        choice = str(input("Please enter a topic: "))
        print(choice)
        if choice == "science" or "math" or "english":
            break
        else:
            print()
            print("Please enter: \nMath\nScience\nEnglish")

    displayQuestion(mathQuestions,scienceQuestions,englishQuestions)

def displayQuestion(mathQuestions,scienceQuestions,englishQuestions):
    print()
    global choice
    randNum = random.randint(0,0)
    if choice == "science":
        question = scienceQuestions[randNum]
        answer = scienceAnswers[randNum]
    if choice == "math":
        question = mathQuestions[randNum]
        answer = mathAnswers[randNum]
    if choice == "english":
        question = englishQuestions[randNum]
        answer = englishAnswers[randNum]

    for x in range (0,5):
        b = "Your question is" + "." * x
        print(b, end="\r")
        time.sleep(1)
    print()
    userAnswer = str(input(question + ": "))
    validateQuestion(userAnswer,answer,incorrectCount)

def validateQuestion(userAnswer,answer,incorrectCount):
    #This will take the answer and return if its correct or not
    if userAnswer == answer:
        print("You are correct!")
        checkStep(stepsForMaze,motorTimeForSteps)
    else:
        print("Better luck next time!")
        incorrectCount += 1
        displayQuestion(mathQuestions,scienceQuestions,englishQuestions)


def checkStep(stepsForMaze,motorTimeForSteps):
    step = stepsForMaze[stepNum]
    time =  motorTimeForSteps[stepNum]
    sendMotorMethods(step,time,stepNum)

def sendMotorMethods(step,time,stepNum):
    UDP_IP = "192.168.1.30" #This is the ip of the Pi
    UDP_PORT = 5005 #This is the port it connects over
    address = UDP_IP, UDP_PORT
    sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
    sock.sendto(str(step).encode('utf-8'), address)
    sock.sendto(str(time).encode('utf-8'), address)

    displayQuestion(mathQuestions,scienceQuestions,englishQuestions)
intro()
