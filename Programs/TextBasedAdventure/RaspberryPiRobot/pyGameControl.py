#simple contr...............................................................................................................................................................................................................................................................................................................ol using pygame

'''
imports
'''
import pygame
import socket

pygame.init()
screen = pygame.display.set_mode((480,320))
pygame.display.set_caption("Robot Driverstation")
print('Welcome to the test Driverstation')
print("Controls:")
print("Up Arrow -> moves robot forward")
print("Down Arrow -> moves robot backward")
print("Left Arrow -> moves robot left")
print("Right Arrow -> moves robot right")
UDP_IP = "10.120.100.0" #This is the ip of the Pi School ip: 10.120.98.209
UDP_PORT = 5005 #This is the port it connects over
address = UDP_IP, UDP_PORT
sock = socket.socket(socket.AF_INET, # Internet
                 socket.SOCK_DGRAM) # UDP

try:
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                GPIO.cleanup()
                pygame.display.quit()
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: #Quits the program
                    break
                elif event.key == pygame.K_UP: #Moves Robot forward
                    move = "Forward"
                    sock.sendto(str(move).encode('utf-8'), address)
                elif event.key == pygame.K_DOWN: #Moves Robot Backwards
                    move = "Backward"
                    sock.sendto(str(move).encode('utf-8'), address)
                elif event.key == pygame.K_LEFT:
                    move = "Right"
                    sock.sendto(str(move).encode('utf-8'), address)
                elif event.key == pygame.K_RIGHT:
                    move = "Left"
                    sock.sendto(str(move).encode('utf-8'), address)
            else:
                move = "Stop"
                sock.sendto(str(move).encode('utf-8'), address)
finally:
    GPIO.cleanup()
