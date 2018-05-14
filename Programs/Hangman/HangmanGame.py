#Plays Hangman Game
#import display_gameText
import secretWords
import convertToAsterisk
import vlc
import pygame

gameRunning = True
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

'''
pygame.init()
size = width, height = 720,480
pygame.font.init() #enables the font
myfont = pygame.font.SysFont('Comic Sans MS', 30)
screen = pygame.display.set_mode(size)
screen.fill(white)
pygame.display.set_caption('Hangman')
'''
def play_game():
    import Hangman
    #Hangman.intro_message_display("Welcome to Hangman! The goal is to complete the word within 6 guesses.")
    #Hangman.intro_message_display("Your secret word is...")
    while gameRunning == True:
        #Hangman.secretWord_display(convertToAsterisk.replace_with_asterisks(secretWord))
        #Hangman.enter_guess_display()
        '''
        Hangman.buttons_display()
        Hangman.select_button()
        '''

play_game()
