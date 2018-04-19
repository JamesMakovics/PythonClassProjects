#This manages the game from the client side
import sys
import pygame
import socket
import random
import time
import vlc

smellsLikeTeenSpirit = vlc.MediaPlayer("C:/Users/zjmakovi/OneDrive for Business/CompSci/Python Class/Smells Like Teen Spirit 8bit.mp3")
smellsLikeTeenSpirit.play()
stepNum = 0
incorrectCount = 0
choice = ""

stepsForMaze = ["forward","left","right","backwards","forward","forward","backwards","left","right"] #Just a place holder
motorTimeForSteps = [1,1,1,1,1,1,1,1,1,1] #Just a place holder


mathQuestions = ["Whats 9+10?","Find the value of 3x+9=0","Simplify: (x+4)*(2x+5) (Use '^' as an exponent)","What is 29²?","5(4x+11)+3(2x+4)=347\nx=?","What is 8³?","What is the units digit of 8 to the 97th?","2⁻³","1+1=?","46*12=?"]
mathAnswers = ["19","3","2x^2+13x+20","841","11","512","8","1/8","2","552"]

scienceQuestions = ["What is the closest star to our own sun?","Betelgeuse and Rigel are the two giant stars in which constellation?","In our solar system, which planet has the shortest day?","Which gland in the human body regulates metabolism?","What common kitchen item is made up of sodium and chlorine atoms?","What is the name for the specialized nerve cell that transmits information chemically and electrically throughout the body?","What is the name for the disc-shaped region of icy bodies that extends from Neptune to about 55 astronomical units from the Sun?","In our solar system which two planets are known as ice giants?","Penicillin was discovered in 1928 by which Scottish scientist?","Bronze is an alloy consisting primarily of what two elements?"]
scienceAnswers = ["Proxima Centauri","Orion","Jupiter","Thyroid","Salt","Neuron","The Kuiper Belt","Uranus and Neptune","Sir Alexander Fleming","Copper and Tin"]

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
    print("You only have 5 guesses!")
    time.sleep(.5)
    print("You have two topics to choose from:")
    print("Math")
    print("Science")
    while True:
        choice = str(input("Please enter a topic: "))
        print(choice)
        if choice == "science" or choice == "math":
            break
        else:
            print()
            print("Please enter: \nMath\nScience")

    displayQuestion(mathQuestions,scienceQuestions)

def displayQuestion(mathQuestions,scienceQuestions):
    print()
    global choice
    global gameFinished
    global incorrectCount
    if gameFinished == True or incorrectCount == 5:
        gameover()
    randNum = random.randint(0,9)
    if choice == "science":
        question = scienceQuestions[randNum]
        answer = scienceAnswers[randNum]
    if choice == "math":
        question = mathQuestions[randNum]
        answer = mathAnswers[randNum]

    for x in range (0,5):
        b = "Your question is" + "." * x
        print(b, end="\r")
        time.sleep(1)
    print()
    userAnswer = str(input(question + ": "))
    validateQuestion(userAnswer,answer)

def validateQuestion(userAnswer,answer):
    #This will take the answer and return if its correct or not
    global incorrectCount
    if userAnswer.lower() == answer.lower():
        print("You are correct!")
        checkStep(stepsForMaze,motorTimeForSteps)
    else:
        print("Better luck next time!")
        incorrectCount += 1
        displayQuestion(mathQuestions,scienceQuestions)


def checkStep(stepsForMaze,motorTimeForSteps):
    global stepNum
    step = stepsForMaze[stepNum]
    time =  motorTimeForSteps[stepNum]
    sendMotorMethods(step,time)

def sendMotorMethods(step,time):
    global stepNum
    global gameFinished
    global stepsForMaze
    UDP_IP = "10.120.98.209" #This is the ip of the Pi
    UDP_PORT = 5005 #This is the port it connects over
    address = UDP_IP, UDP_PORT
    sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
    sock.sendto(str(step).encode('utf-8'), address)
    sock.sendto(str(time).encode('utf-8'), address)

    stepNum = stepNum + 1
    if stepNum == len(stepsForMaze):
        gameFinished = True

    displayQuestion(mathQuestions,scienceQuestions)

def gameover():
    global gameFinished
    global incorrectCount
    if gameFinished == True and incorrectCount < 5:
        print("Congratulations you have beaten the maze!")
        sys.exit()
    else:
        print("Sorry you have reached 5 incorrect answers. Goodbye.")
        sys.exit()
intro()
