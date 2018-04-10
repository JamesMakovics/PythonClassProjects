import pygame

pygame.init()
pygame.mixer.init()
sounds = pygame.mixer.Sound("C:/Users/zjmakovi/Documents/GitHub/PythonClassProjects/Programs/soundFiles/THE SHEEV SPIN.mp3")
sounds.play() #Plays sound
#import winsound This import uses only .wav files

#winsound.PlaySound('C:/Users/zjmakovi/OneDrive for Business/CompSci/Python Class/THE SHEEV SPIN.mp3', winsound.SND_FILENAME)
