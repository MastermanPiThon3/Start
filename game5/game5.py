#Import pygame module
import math
import pygame
from pygame.locals import *

#import game classes from other python files
from Player import *
from Arena import *
from Arrows import *
from BadGuys import *

#Initialize the pygame
pygame.init()

####game variables####
#Color for background
GREEN = (0, 168, 42)
#False if game quit
gameActive = True
#Create the Arena, holds the surface we are drawing the game on
arena = Arena(640, 480, GREEN)
#The player, holds the image and position of the player
player = Player(arena, "../images/dude.png")
#Holds arrows in flight
arrows = Arrows("../images/arrow.png")
#Holds bag guys on the arena
badGuys = BadGuys("../images", 42)
#Holds the current direction(s) the player is moving.  Set to no movement
#       left-a right-d up-w  down-s
keys = {K_a:0, K_d:0, K_w:0, K_s:0, K_f:0, K_ESCAPE:0 }

arena.StartGame()

#Main Game loop.  The game runs for ever.
while not arena.Status.TimeUp() and player.Alive() and gameActive:
    #Move the player, arrows and bad guys
    player.Move(arena, keys)
    arrows.Move(arena)
    badGuys.MoveAttack(arena, player, arrows)
    arena.Update(keys, player)
    #Fill arena (surface)
    arena.Clear(player)
    player.Blit(arena, pygame.mouse.get_pos())
    arrows.Blit(arena)
    badGuys.Blit(arena)
    
    #Draw arena (surface)
    pygame.display.flip()

    ##Loop over input to see if the keys w, s, a or d were pressed or released
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:            #A key was pressed
            keys[event.key] = player.Speed
        elif event.type == pygame.KEYUP:            #A key was released
            keys[event.key] = 0
        elif event.type == pygame.MOUSEBUTTONDOWN:  #The mouse button was clicked
            arrows.AddArrow(pygame.mouse.get_pos(), player)
            arena.Status.Fired += 1
        elif event.type == pygame.QUIT:             #The user quit
            pygame.quit()
            gameActive = False

    #limit game rate
    arena.Status.FrameLimiter()
    


arena.EndGame(player)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
        if event.type == pygame.KEYDOWN and (event.key == K_q or event.key == K_ESCAPE):
            pygame.quit()
