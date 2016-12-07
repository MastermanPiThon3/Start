import pygame
from pygame.locals import *
from MathFunctions import *

class Player:
    def __init__ (self, screen, imageLocation):
        self.Image = pygame.image.load(imageLocation).convert_alpha()
        self.Width = self.Image.get_width()
        self.Height = self.Image.get_height()
        self.Center = [self.Width/2.0, self.Height/2.0]
        self.Padding = self.Width/5
        self.Speed = 5
        self.Position = [40, 220]
        self.xMargin = self.Width/2
        self.yMargin = self.Height/2
        self.Health = 100
        self.Damage = 1

    def Move(self, arena, keys):
        #Update players position
        xUpdated = keys[K_d] - keys[K_a] + self.Position[X]
        yUpdated = keys[K_s] - keys[K_w] + self.Position[Y]
        if self.xMargin <= xUpdated <= arena.Display.get_width() - self.xMargin:
            self.Position[X] = xUpdated
        if self.yMargin <= yUpdated <= arena.Display.get_height() - self.yMargin:
            self.Position[Y] = yUpdated

    def RepositionOnScreenSizeChange(self, width, height):
        if self.Position[X] >= width - self.xMargin:
            self.Position[X] = width - self.xMargin
        if self.Position[Y] >= height - self.yMargin:
            self.Position[Y] = height - self.yMargin

    def Blit(self, arena, mousePosition):
        #Determine angle between player position and the mouse position
        rotationAngle = AngleBetween(mousePosition, self.Position, self.Center)
        arena.RotateAndBlit(self.Image, self.Position, rotationAngle)

    def Attack(self, victim):
        victim.Health -= self.Damage
        self.Health -= victim.Damage
        #return self.Damage

    def Alive(self):
        return self.Health > 0
