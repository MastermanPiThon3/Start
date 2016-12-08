#Import pygame module
import pygame
from pygame.locals import *

#Initialize the pygame
pygame.init()

####constants####
#Colors
GREEN = (0, 168, 42) 
ORANGE = (255, 102, 0) 
#Accessors
X = 0
Y = 1
W = 2
H = 3

####game variables####

#Player state       X   Y   W   H
player = { "Area":[10, 10, 20, 20], "Color":ORANGE, "Speed":10 }

#game window size
width = 640
height = 480

#game window
screen = pygame.display.set_mode([width, height])

#Holds the current direction(s) the player is moving.  Set to no movement
#       left-a right-d up-w  down-s
keys = { K_a:0, K_d:0, K_w:0, K_s:0 }

#keeps time for game
gameClock = pygame.time.Clock()

gameActive = True

#Main Game loop.  The game runs until the user quits
while gameActive:

    #Limit to 60 FPS
    gameClock.tick(60)

    #Fill screen with bg color
    screen.fill(GREEN)

    pygame.draw.rect(screen, player["Color"], player["Area"])
    
    #Draw arena (surface)
    pygame.display.update()

    ##Loop over input to see if the keys w, s, a or d were pressed or released
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:            #A key was pressed
            keys[event.key] = player["Speed"]
        elif event.type == pygame.KEYUP:            #A key was released
            keys[event.key] = 0
        elif event.type == pygame.QUIT:             #The user quit
            gameActive = False

    #Determine new player position based on keyboard input
    xMovement = keys[K_d] - keys[K_a]
    yMovement = keys[K_s] - keys[K_w]
    updatedX = player["Area"][X] + xMovement
    updatedY = player["Area"][Y] + yMovement

    #Update player position if new position is in bounds
    if updatedX >= 0 and updatedX + player["Area"][W] <= width:
        player["Area"][X] = updatedX
    if updatedY >= 0 and updatedY + player["Area"][H] <= height:
        player["Area"][Y] = updatedY
    

#end pygame
pygame.quit()
