import pygame
from pygame.locals import *

from MathFunctions import *
from Stats import *

class Arena:
    def __init__(self, width, height, color):
        displayInfo = pygame.display.Info()
        self.FullScreenSize = [displayInfo.current_w, displayInfo.current_h]
        self.Width = width
        self.Height = height
        self.WindowedSize = [self.Width, self.Height]
        self.Color = color
        self.MakeWindowed()
        self.Status = Stats((0,0,0), color)

    def Clear(self, player):
        self.Display.fill(self.Color)
        self.Status.Blit(self, player.Health)    

    def RotateAndBlit(self, image, position, rotationAngle):
        imageRotated = pygame.transform.rotate(image, InDegrees(rotationAngle))
        rotatedRect = imageRotated.get_rect()
        positionAdjusted = [position[X]- rotatedRect.width/2,
                            position[Y] - rotatedRect.height/2]
        self.Blit(imageRotated, positionAdjusted)

    def Blit(self, image, position):
        self.Display.blit(image, position)

    def InBounds(self, position, xPadding, yPadding):
        return xPadding <= position[X] <= (self.Width - xPadding) and yPadding <= position[Y] <= (self.Height - yPadding)

    def StartGame(self):
        self.Status.StartTime = pygame.time.get_ticks()


    def EndGame(self, player):
        font = pygame.font.Font(None, 84)
        endText = "You Win!"
        textColor = (0, 168, 42)
        if not player.Alive():
            endText = "You Loose!"
            textColor = (255, 0 ,0)

        endImage = font.render(endText, True, textColor, (0, 0, 0))
        endPosition = [self.Width/2 - endImage.get_width()/2, self.Height/2 - endImage.get_height()/2]
        self.Display.fill((0,0,0))
        self.Display.blit(endImage, endPosition)
        pygame.display.flip()

    def MakeFullScreen(self):
        self.Display = pygame.display.set_mode(self.FullScreenSize, pygame.FULLSCREEN)
        self.Width = self.Display.get_width()
        self.Height = self.Display.get_height()
        
    def MakeWindowed(self):
        self.Display = pygame.display.set_mode(self.WindowedSize)
        self.Width = self.Display.get_width()
        self.Height = self.Display.get_height()


    def Update(self, keys, player):
        if keys[K_f] > 0:
            self.MakeFullScreen()

        if keys[K_ESCAPE] > 0:
            self.MakeWindowed()
            player.RepositionOnScreenSizeChange(self.Width, self.Height)

            
