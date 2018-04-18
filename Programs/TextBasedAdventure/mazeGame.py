#This manages the game from the client side
import pygame
import socket
stepNum = 0

stepsForMaze = []
motorTimeForCorrectSteps[]

incorrectStepsForMaze = []
motorTimeForIncorrectSteps = []

mathQuestions = ["Whats 9+10?","Find the value of 3x+9=0","What is the factor of 3x^2+6x+3","","",""]
mathAnswers = [21,3,]

scienceQuestions = []
scienceAnswers = []

englishQuestions = []
englishAnswers = []


gameFinished = False

def runGame():
    if gameFinished == False:
        return True
    else:
        return False

def intro():
    print("Hello")
    print("Welcome to MazeCraze")
    print("You will need to answer questions in order to move the robot")
    print("You have three topics to choose from:")
    print("Math")
    print("Science")
    print("English")
    choice = str(input("Please enter a topic: "))
    choice = choice.lower()
    if choice == "science":
        displayQuestion()
    elif choice == "math":
        displayQuestion()
    elif choice == "english":
        displayQuestion()

def displayQuestion():
    #This method will take a question at random from the list and display it
    #This will send the send the answer for validation

def validateQuestion():
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

def sendMotorMethods():
UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.sendto(step,time)

data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes

if data == True:
    displayQuestion()
