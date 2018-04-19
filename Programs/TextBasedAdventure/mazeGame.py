#This manages the game from the client side
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

stepsForMaze = ["forward","left"] #Just a place holder
motorTimeForSteps = [1,1] #Just a place holder


mathQuestions = ["Whats 9+10?","Find the value of 3x+9=0","Simplify: (x+4)*(2x+5) (Use '^' as an exponent)","What is 29²?","5(4x+11)+3(2x+4)=347\nx=?","What is 8³?","What is the units digit of 8 to the 97th?","2⁻³","1+1=?","46*12=?"]
mathAnswers = ["19","3","2x^2+13x+20","841","11","512","8","1/8","2","552"]

scienceQuestions = ["What is the closest star to our own sun?","Betelgeuse and Rigel are the two giant stars in which constellation?","In our solar system, which planet has the shortest day?","Which gland in the human body regulates metabolism?","What common kitchen item is made up of sodium and chlorine atoms?","What is the name for the specialized nerve cell that transmits information chemically and electrically throughout the body?","What is the name for the disc-shaped region of icy bodies that extends from Neptune to about 55 astronomical units from the Sun?","In our solar system which two planets are known as ice giants?","Penicillin was discovered in 1928 by which Scottish scientist?","Bronze is an alloy consisting primarily of what two elements?"]
scienceAnswers = ["Proxima Centauri","Orion","Jupiter","Thyroid","Salt","Neuron","The Kuiper Belt","Uranus and Neptune","Sir Alexander Fleming","Copper and Tin"]

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
    if userAnswer.lower() == answer.lower():
        print("You are correct!")
        checkStep(stepsForMaze,motorTimeForSteps)
    else:
        print("Better luck next time!")
        incorrectCount += 1
        displayQuestion(mathQuestions,scienceQuestions,englishQuestions)


def checkStep(stepsForMaze,motorTimeForSteps):
    global stepNum
    step = stepsForMaze[stepNum]
    time =  motorTimeForSteps[stepNum]
    sendMotorMethods(step,time)

def sendMotorMethods(step,time):
    global stepNum
    UDP_IP = "10.120.98.209" #This is the ip of the Pi
    UDP_PORT = 5005 #This is the port it connects over
    address = UDP_IP, UDP_PORT
    sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
    sock.sendto(str(step).encode('utf-8'), address)
    sock.sendto(str(time).encode('utf-8'), address)

    stepNum = stepNum + 1
    displayQuestion(mathQuestions,scienceQuestions,englishQuestions)
intro()
