#This manages the game from the client side
import pygame
stepNum = 0

stepsForMaze = []
motorSpeedsForCorrectSteps[]

incorrectStepsForMaze = []
motorSpeedsForIncorrectSteps = []

mathQuestions = []
mathAnswers = []

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
    #This method will be completed later

def displayQuestion():
    #This method will take a question at random from the list and display it
    #This will send the send the answer for validation

def validateQuestion():
    #This will take the answer and return if its correct or not

def checkStep(stepsForMaze,incorrectStepsForMaze,motorSpeedsForCorrectSteps,motorSpeedsForIncorrectSteps):
    #This updates the step of how long the robot needs to run
    #This will hold a correct and incorrect method
    if validateQuestion() == True:
        return stepsForMaze[stepNum], motorSpeedsForCorrectSteps[stepNum]
    else:
        return incorrectStepsForMaze[stepNum], motorSpeedsForIncorrectSteps[stepNum]

def getStep():
    connectToPi.sendStep(validateQuestion()))
