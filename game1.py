#Import pygame module
import math
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
X = 0
Y = 1
playerPos = [320, 375]

#The number of pixles to move the player each loop
PlayerSpeed = 5

#The image for the player, it is loaded from the file 'dude.png'
Player = pygame.image.load("dude.png")
playerWidth = Player.get_width()
playerHeight = Player.get_height()

xMinMargin = 5
xMaxMargin = width - playerWidth
yMinMargin = 5
yMaxMargin = height - playerHeight

#Holds the current direction(s) the player is moving.  Set to no movement
#       left-a right-d up-w  down-s
keys = {K_a:0, K_d:0, K_w:0, K_s:0, }


#Main Game loop.  The game runs for ever.
while True:
    #Fill screen with black
    screen.fill((0,0,0))

    ##Rotate a copy of the player image to point to the mouse
    
    mousePos = pygame.mouse.get_pos()
    #Determine angle between player position and the mouse position
    xDist = mousePos[X] - playerPos[X] - playerWidth/2
    yDist = mousePos[Y] - playerPos[Y] - playerHeight/2
    rotationAngle = math.atan2(yDist, xDist)
    #Rotate image
    playerRotated = pygame.transform.rotate(Player, 360 - rotationAngle * 57.29)
    #Adjust the player position so the image is drawn in a consistent location
    rotatedRect = playerRotated.get_rect()
    playerPosAdjusted = [playerPos[X] - rotatedRect.width/2, playerPos[Y] - rotatedRect.height/2]
    
    #Place the rotated player image on screen
    screen.blit(playerRotated, playerPosAdjusted)

    #Loop over input to see if the keys w, s, a or d were pressed or released
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:    #A key was pressed
            keys[event.key] = PlayerSpeed
        elif event.type == pygame.KEYUP:    #A key was released
            keys[event.key] = 0
        elif event.type == pygame.QUIT:     #The user quit
            pygame.quit()

    #Update players position
    xUpdated = playerPos[X] - keys[K_a] + keys[K_d]
    yUpdated = playerPos[Y] - keys[K_w] + keys[K_s]
    if xMinMargin <= xUpdated <= xMaxMargin:
        playerPos[X] = xUpdated
    if yMinMargin <= yUpdated <= yMaxMargin:
        playerPos[Y] = yUpdated

    
    #Draw screen
    pygame.display.flip()

