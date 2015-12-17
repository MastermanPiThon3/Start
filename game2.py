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

#Color for background
GREEN = (0, 168, 42)

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
playerOffset = [playerWidth/2, playerHeight/2]

#The image for the arrow
arrow = pygame.image.load("arrow.png")
#Holds direction and current position of arrows in flight
#0 holds arrow direction, 1 holds current position of arrow
DIRECTION = 0
POSITION  = 1
arrows = []
arrowSpeed = 10
arrowOffset = [playerWidth - 15, playerHeight - 15]

xMinMargin = 5
xMaxMargin = width - playerWidth
yMinMargin = 5
yMaxMargin = height - playerHeight

#Holds the current direction(s) the player is moving.  Set to no movement
#       left-a right-d up-w  down-s
keys = {K_a:0, K_d:0, K_w:0, K_s:0, }

def AngleBetween(pos0, pos1, offset):
    pos1 = OffsetPosition(pos1, offset)
    xDist = pos0[X] - pos1[X]
    yDist = pos0[Y] - pos1[Y]
    return math.atan2(yDist, xDist)

def OffsetPosition(position, offset):
    return [position[X] + offset[X], position[Y] + offset[Y]]

def InDegrees(radians):
    return 360 - radians * 57.3

def RotateAndBlit(screen, image, position, rotationAngle):
    imageRotated = pygame.transform.rotate(image, InDegrees(rotationAngle))
    rotatedRect = imageRotated.get_rect()
    positionAdjusted = [position[X] - rotatedRect.width/2, position[Y] - rotatedRect.height/2]
    screen.blit(imageRotated, positionAdjusted)
    


#Main Game loop.  The game runs for ever.
while True:
    #Fill screen with black
    screen.fill(GREEN)

    ##Rotate a copy of the player image to point to the mouse and place on screen
    mousePos = pygame.mouse.get_pos()
    #Determine angle between player position and the mouse position
    rotationAngle = AngleBetween(mousePos, playerPos, playerOffset)
    #Rotate image
    RotateAndBlit(screen, Player, playerPos, rotationAngle)

    ##Update each arrows position and place a rotated arrow image on the screen
    index = 0
    for a in arrows:
        movement = [math.cos(a[DIRECTION]) * arrowSpeed, math.sin(a[DIRECTION]) * arrowSpeed]
        updatedPosition = OffsetPosition(a[POSITION], movement)
        if 0 <= updatedPosition[X] >= width or 0 <= updatedPosition[Y] >= height:
            arrows.pop(index)
        else:
            a[POSITION] = updatedPosition
        ++index
        RotateAndBlit(screen, arrow, a[POSITION], a[DIRECTION])

    ##Loop over input to see if the keys w, s, a or d were pressed or released
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:            #A key was pressed
            keys[event.key] = PlayerSpeed
        elif event.type == pygame.KEYUP:            #A key was released
            keys[event.key] = 0
        elif event.type == pygame.MOUSEBUTTONDOWN:  #The mouse button was clicked
            arrowDirection = AngleBetween(pygame.mouse.get_pos(), playerPos, playerOffset)

            cosAngle = math.cos(arrowDirection)
            sinAngle = math.sin(arrowDirection)
            adjustedArrowOffset = [playerPos[X] + cosAngle * 32.0 - sinAngle * 10.0,
                                   playerPos[Y] + sinAngle * 32.0 + cosAngle * 10.0]

            arrows.append([arrowDirection, adjustedArrowOffset])
        elif event.type == pygame.QUIT:             #The user quit
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

