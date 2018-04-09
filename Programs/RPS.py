#Rock Paper Scissors

import random
import time

computer_score = 0
player_score = 0

choice_list = ["Rock","Paper","Scissors"]

def instructions():
    print("To enter a choice you need to type either:")
    print("rock or 'r'")
    print("paper or 'p'")
    print("scissors or 's'")

def userChoice():
    instructions()
    userInput = str(input("Enter your choice: "))
    userInput = userInput.lower()
    if userInput == 'rock' or userInput == 'r':
        return choice_list[0]
    elif userInput == 'paper' or userInput == 'p':
        return choice_list[1]
    elif userInput == 'scissors' or userInput == 's':
        return choice_list[2]
    else:
        print("Please try again!")
        userChoice()

def randomChoice():
    random_number = random.randint(0,2)
    return choice_list[random_number]

def compareChoices(computer_score,player_score,userChoice,randomChoice):
    if userChoice() == randomChoice():
        print("Its a tie")
    elif userChoice() == choice_list[0] and randomChoice() == choice_list[1]:
        print()
        print("Paper beats Rock!")
        print()
        print("The computer won this round!")
        computer_score += 1
    elif userChoice() == choice_list[1] and randomChoice() == choice_list[2]:
        print()
        print("Scissors beats Paper!")
        print()
        print("The computer won this round!")
        computer_score += 1
    elif userChoice() == choice_list[2] and randomChoice() == choice_list[0]:
        print()
        print("Rock beats Scissors")
        print()
        print("The computer won this round!")
        computer_score += 1
    elif userChoice() == choice_list[1] and randomChoice == choice_list[0]:
        print()
        print("Paper beats Rock!")
        print()
        print("You won this round!")
        player_score += 1
    elif userChoice() == choice_list[2] and randomChoice() == choice_list[1]:
        print()
        print("Scissors beats Paper!")
        print()
        print("You won this round!")
        player_score += 1
    elif userChoice() == choice_list[0] and randomChoice() == choice_list[2]:
        print()
        print("Rock beats Scissors")
        print()
        print("You won this round!")
        player_score += 1
    else:
        print()
        print("Error! Could not compare results!")

def determineWinner(computer_score,player_score):
    if player_score < computer_score:
        print("The Computer won better luck next time!")
    else:
        print("You win see you next time!")

print("Welcome to Rock, Paper, Scissors!")
while player_score + computer_score < 3:
    userChoice()
    randomChoice()
    compareChoices(computer_score,player_score,userChoice,randomChoice)

determineWinner(computer_score,player_score)
