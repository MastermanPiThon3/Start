#put in activation
import math
import random

import pygame
from pygame.locals import *


#Initialize the game
pygame.init()
width, height = 640, 480
screen=pygame.display.set_mode((width, height))
PlayerCoords = [320, 375]
keys = [False, False, False, False]

#Load Image
Player = pygame.image.load("dude.png")

while True:
    screen.fill((0,0,0))
    screen.blit(Player, PlayerCoords)

    #input wsad
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
                if event.key == K_a:
                    keys[0] = True
                elif event.key == K_d:
                    keys[1] = True
                elif event.key == K_w:
                    keys[2] = True
                elif event.key == K_s:
                    keys[3] = True
        if event.type == pygame.KEYUP:
                if event.key == K_a:
                    keys[0] = False
                elif event.key == K_d:
                    keys[1] = False
                elif event.key == K_w:
                    keys[2] = False
                elif event.key == K_s:
                    keys[3] = False
        if event.type == pygame.QUIT:
            pygame.quit()

    #Move 
    if keys[0]== True: 
        if PlayerCoords[0] >= 32:
            PlayerCoords[0] -= 5
    if keys[1] == True:
        if PlayerCoords[0] <= 585:
            PlayerCoords[0] += 5
    if keys[2] == True: 
        if PlayerCoords[1] >= 32:
            PlayerCoords[1] -= 5
    if keys[3] == True:
        if PlayerCoords[1] <= 420:
            PlayerCoords[1] += 5
    
    

    #refreshes screen
    pygame.display.flip()

