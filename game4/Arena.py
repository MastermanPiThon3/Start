import pygame
from pygame.locals import *

from MathFunctions import *

class Arena:
    def __init__(self, width, height, color):
        self.Display = pygame.display.set_mode((width, height))
        self.Width = width
        self.Height = height
        self.Color = color

    def Clear(self):
        self.Display.fill(self.Color)

    def RotateAndBlit(self, image, position, rotationAngle):
        imageRotated = pygame.transform.rotate(image, InDegrees(rotationAngle))
        rotatedRect = imageRotated.get_rect()
        positionAdjusted = [position[X]- rotatedRect.width/2,
                            position[Y] - rotatedRect.height/2]
        self.Display.blit(imageRotated, positionAdjusted)

    def InBounds(self, position, xPadding, yPadding):
        return xPadding <= position[X] <= (self.Width - xPadding) and yPadding <= position[Y] <= (self.Height - yPadding)

     



        
            
