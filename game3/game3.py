#Import pygame module
import math
import pygame
from pygame.locals import *

from GameClasses import *

#Initialize the pygame
pygame.init()

####game variables####
#Color for background
GREEN = (0, 168, 42)

gameActive = True

#Create the Arena, holds the surface we are drawing the game on
arena = Arena(640, 480, GREEN)

#The player, holds the image and position of the player
player = Player(arena, "../images/dude.png")

#Holds arrows in flight
arrows = Arrows("../images/arrow.png")

#Holds the current direction(s) the player is moving.  Set to no movement
#       left-a right-d up-w  down-s
keys = {K_a:0, K_d:0, K_w:0, K_s:0, }


#Main Game loop.  The game runs for ever.
while gameActive:
    #Fill arena
    arena.Clear()
    player.MoveAndBlit(arena, pygame.mouse.get_pos(), keys)
    arrows.MoveAndBlit(arena)
    
    #Draw arena
    pygame.display.flip()

    ##Loop over input to see if the keys w, s, a or d were pressed or released
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:            #A key was pressed
            keys[event.key] = player.Speed
        elif event.type == pygame.KEYUP:            #A key was released
            keys[event.key] = 0
        elif event.type == pygame.MOUSEBUTTONDOWN:  #The mouse button was clicked
            arrows.AddArrow(pygame.mouse.get_pos(), player)
        elif event.type == pygame.QUIT:             #The user quit
            pygame.quit()
            gameActive = False            


