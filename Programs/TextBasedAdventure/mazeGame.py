#This manages the game from the client side
import pygame
import socket
import random
stepNum = 0

stepsForMaze = [1,1]
motorTimeForCorrectSteps = [1,1]

incorrectStepsForMaze = [1,1]
motorTimeForIncorrectSteps = [1,1]

mathQuestions = ["Whats 9+10?","Find the value of 3x+9=0","What is the factor of 3x^2+6x+3","","",""]
mathAnswers = [21,3,]

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
        choice = choice.lower()
        if choice != "science" or "math" or "english":
            print("Please enter: \nMath\nScience\nEnglish")
        else:
            False
    displayQuestion(choice,mathQuestions,scienceQuestions,englishQuestions)

def displayQuestion(choice,mathQuestions,scienceQuestions,englishQuestions):
    if choice == "science":
        question = scienceQuestions[random.randint(0,26)]
    if choice == "math":
        question = mathQuestions[random.randint(0,26)]
    if choice == "english":
        question = englishQuestions[random.randint(0,26)]

    for x in range (0,5):
        b = "Your question is" + "." * x
        print (b, end="\r")
        time.sleep(1)
    print(question)

#def validateQuestion():
    #This will take the answer and return if its correct or not

def checkStep(stepsForMaze,incorrectStepsForMaze,motorTimeForCorrectSteps,motorTimeForIncorrectSteps):
    #This updates the step of how long the robot needs to run
    #This will hold a correct and incorrect method
    if validateQuestion() == True:
        step = stepsForMaze[stepNum]
        time =  motorTimeForCorrectSteps[stepNum]
        sendMotorMethods()
    else:
        step = incorrectStepsForMaze[stepNum]
        time = motorTimeForIncorrectSteps[stepNum]
        sendMotorMethods()

def sendMotorMethods(step,time):
    UDP_IP = "127.0.0.1"
    UDP_PORT = 5005

    sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
    sock.sendto(step)
    sock.sendto(time)
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes

    if data == "Finished":
        displayQuestion()
