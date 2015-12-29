import pygame
from pygame.locals import *

from MathFunctions import *

class Arena:
    def __init__(self, width, height, color):
        self.Display = pygame.display.set_mode((width, height))
        self.Width = width
        self.Height = height
        self.Color = color

    def Clear(self, ):
        self.Display.fill(self.Color)

    def RotateAndBlit(self, image, position, rotationAngle):
        imageRotated = pygame.transform.rotate(image, InDegrees(rotationAngle))
        rotatedRect = imageRotated.get_rect()
        positionAdjusted = [position[X]- rotatedRect.width/2,
                            position[Y] - rotatedRect.height/2]
        self.Display.blit(imageRotated, positionAdjusted)

class Range:
    def __init__(self, minimum, maximum):
        self.Min = minimum
        self.Max = maximum

class Player:
    def __init__ (self, screen, imageLocation):
        self.Image = pygame.image.load(imageLocation)
        self.Width = self.Image.get_width()
        self.Height = self.Image.get_height()
        self.Center = [self.Width/2.0, self.Height/2.0]
        self.BowTip = [self.Width - 15, self.Height - 15]
        self.Speed = 5
        self.Position = [40, 220]
        self.xMargin = Range(self.Width/2, screen.Width - self.Width/2)
        self.yMargin = Range(self.Height/2, screen.Height - self.Height/2)

    def MoveAndBlit(self, arena, mousePosition, keys):
        #Update players position
        xUpdated = keys[K_d] - keys[K_a] + self.Position[X]
        yUpdated = keys[K_s] - keys[K_w] + self.Position[Y]
        if self.xMargin.Min <= xUpdated <= self.xMargin.Max:
            self.Position[X] = xUpdated
        if self.yMargin.Min <= yUpdated <= self.yMargin.Max:
            self.Position[Y] = yUpdated

        ##Rotate a copy of the player image to point to the mouse and place on screen
        #Determine angle between player position and the mouse position
        rotationAngle = AngleBetween(mousePosition, self.Position, self.Center)
        #Rotate image
        arena.RotateAndBlit(self.Image, self.Position, rotationAngle)
     

class Arrow:
    def __init__ (self, mousePosition, player):
        self.Direction = AngleBetween(mousePosition, player.Position, player.Center)
        cosAngle = math.cos(self.Direction)
        sinAngle = math.sin(self.Direction)
        self.Position = [player.Position[X] + cosAngle * 32.0 - sinAngle * 10.0,
                         player.Position[Y] + sinAngle * 32.0 + cosAngle * 10.0]
        
    

class Arrows:
    def __init__ (self, imageLocation):
        self.Image = pygame.image.load(imageLocation)
        self.Active = []
        self.Speed = 10;

    ##Update each arrows position and place a rotated arrow image on the screen
    def MoveAndBlit(self, arena):
        index = 0
        for a in self.Active:
            movement = [math.cos(a.Direction) * self.Speed, math.sin(a.Direction) * self.Speed]
            updatedPosition = OffsetPosition(a.Position, movement)
            if 0 <= updatedPosition[X] >= arena.Width or 0 <= updatedPosition[Y] >= arena.Height:
                self.Active.pop(index)
            else:
                a.Position = updatedPosition
            ++index
            arena.RotateAndBlit(self.Image, a.Position, a.Direction)

    def AddArrow(self, mousePosition, player):
        self.Active.append(Arrow(mousePosition, player))
