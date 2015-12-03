#Import pygame module
import pygame
from pygame.locals import *

#Initialize the pygame
pygame.init()

####game variables####
width = 640     # width of game screen
height = 480    # height of screen

#Create the screen
screen=pygame.display.set_mode((width, height))

#Holds the current position of the player.  Set the start position of the player
PlayerCoords = [320, 375]

#Holds the current direction(s) the player is moving.  Set to no movement
#       left-a right-d up-w  down-s
keys = [False, False, False, False]

#Represents the player in the game and holds the image.  The image is loaded from the file 'dude.png'
Player = pygame.image.load("dude.png")



#Main Game loop.  The game runs for ever.
while True:
    #Fill screen with black
    screen.fill((0,0,0))
    #Place the player on screen
    screen.blit(Player, PlayerCoords)

    #Loop over input to see if the keys w, s, a or d were pressed or released
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:    #A key was pressed
                if event.key == K_a:
                    keys[0] = True
                elif event.key == K_d:
                    keys[1] = True
                elif event.key == K_w:
                    keys[2] = True
                elif event.key == K_s:
                    keys[3] = True
        if event.type == pygame.KEYUP:      #A key was released
                if event.key == K_a:
                    keys[0] = False
                elif event.key == K_d:
                    keys[1] = False
                elif event.key == K_w:
                    keys[2] = False
                elif event.key == K_s:
                    keys[3] = False
        if event.type == pygame.QUIT:       #The user quit
            pygame.quit()

    #Update players position 
    if keys[0]== True: 
        if PlayerCoords[0] >= 5:
            PlayerCoords[0] -= 5
    if keys[1] == True:
        if PlayerCoords[0] <= 570:
            PlayerCoords[0] += 5
    if keys[2] == True: 
        if PlayerCoords[1] >= 5:
            PlayerCoords[1] -= 5
    if keys[3] == True:
        if PlayerCoords[1] <= 430:
            PlayerCoords[1] += 5
    
    #Draw screen
    pygame.display.flip()

