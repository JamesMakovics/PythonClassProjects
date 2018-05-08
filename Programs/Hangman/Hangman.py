#Plays Hangman Game
import displayText
import secretWords
import convertToAsterisk
import vlc
import pygame

size = width, height = 1080,720
pygame.font.init() #enables the font
myfont = pygame.font.SysFont('Comic Sans MS', 30)
screen = pygame.display.set_mode(size)

def play_game():
    displayText.message_display("Welcome to Hangman!\nThe goal is to complete the word within 6 guesses.")

play_game()
