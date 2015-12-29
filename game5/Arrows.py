import pygame
from pygame.locals import *
from MathFunctions import *

class Arrow:
    def __init__ (self, destination, player):
        self.Direction = AngleBetween(destination, player.Position, player.Center)
        cosAngle = math.cos(self.Direction)
        sinAngle = math.sin(self.Direction)
        self.Position = [player.Position[X] + cosAngle * 32.0 - sinAngle * 10.0,
                         player.Position[Y] + sinAngle * 32.0 + cosAngle * 10.0]
        self.Health = 5
        self.Damage = 25

    def Move(self, speed):
        self.Position = OffsetDistance(self.Position, speed, self.Direction)

    def Attack(self, victim):
        victim.Health -= self.Damage
        self.Health = 0
        #return self.Damage

    def Alive(self):
        return self.Health > 0

    def Kill(self):
        self.Health = 0
    

class Arrows:
    def __init__ (self, imageLocation):
        self.Image = pygame.image.load(imageLocation).convert_alpha()
        self.Active = []
        self.Speed = 10;
        self.Padding = self.Image.get_width()/5

    ##Update each arrows position and place a rotated arrow image on the screen
    def Move(self, arena):
        for a in self.Active:
            a.Move(self.Speed)
            if not arena.InBounds(a.Position, 0, 0):
                a.Kill()

        self.Active = filter(lambda ar: ar.Alive(), self.Active)

    def Blit(self, arena):
        for a in self.Active:
            arena.RotateAndBlit(self.Image, a.Position, a.Direction)

    def AddArrow(self, mousePosition, player):
        self.Active.append(Arrow(mousePosition, player))
