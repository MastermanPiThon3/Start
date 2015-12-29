import random
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

    def InBounds(self, position, xPadding, yPadding):
        return xPadding <= position[X] <= (self.Width - xPadding) or yPadding <= position[Y] <= (self.Height - yPadding)

class Player:
    def __init__ (self, screen, imageLocation):
        self.Image = pygame.image.load(imageLocation)
        self.Width = self.Image.get_width()
        self.Height = self.Image.get_height()
        self.Center = [self.Width/2.0, self.Height/2.0]
        self.Padding = self.Width/4
        self.Speed = 5
        self.Position = [40, 220]
        self.xMargin = Range(self.Width/2, screen.Width - self.Width/2)
        self.yMargin = Range(self.Height/2, screen.Height - self.Height/2)
        self.Health = 100
        self.Damage = 5

    def MoveAndBlit(self, arena, mousePosition, keys):
        #Update players position
        xUpdated = keys[K_d] - keys[K_a] + self.Position[X]
        yUpdated = keys[K_s] - keys[K_w] + self.Position[Y]
        if self.xMargin.Min <= xUpdated <= self.xMargin.Max:
            self.Position[X] = xUpdated
        if self.yMargin.Min <= yUpdated <= self.yMargin.Max:
            self.Position[Y] = yUpdated

        #Determine angle between player position and the mouse position
        rotationAngle = AngleBetween(mousePosition, self.Position, self.Center)
        arena.RotateAndBlit(self.Image, self.Position, rotationAngle)

    def Attack(self, victim):
        self.Health -= victim.Damage
        return self.Damage

    def Alive(self):
        return self.Health > 0
     

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
        self.Health = 0
        return self.Damage

    def Alive(self):
        return self.Health > 0
    

class Arrows:
    def __init__ (self, imageLocation):
        self.Image = pygame.image.load(imageLocation)
        self.Active = []
        self.Speed = 10;
        self.Padding = self.Image.get_width()/4

    ##Update each arrows position and place a rotated arrow image on the screen
    def MoveAndBlit(self, arena):
        index = 0
        for a in self.Active:
            a.Move(self.Speed)
            if not arena.InBounds(a.Position, 0, 0):
                self.Active.pop(index)
            ++index
            arena.RotateAndBlit(self.Image, a.Position, a.Direction)

    def AddArrow(self, mousePosition, player):
        self.Active.append(Arrow(mousePosition, player))

class BadGuy:
    def __init__(self, player, startPosition):
        self.Position = startPosition
        self.Direction = AngleBetween(player.Position, startPosition, [0,0])
        self.ImageIndex = 0
        self.Health = 25
        self.Damage = 5

    def Move(self, position, speed):
        self.Direction = AngleBetween(position, self.Position, [0,0])
        self.Position = OffsetDistance(self.Position, speed, self.Direction)
        self.ImageIndex += 1

    def Attack(self, victim):
        self.Health -= victim.Damage
        return self.Damage

    def Alive(self):
        return self.Health > 0

class BadGuys:
    def __init__(self, imageDirectory, spawnDelay):
        self.Images = []
        for i in range(0,3):
            self.Images.append(pygame.image.load(imageDirectory + "/badguy" + str(i) + ".png"))
        #self.Images.append(pygame.image.load(imageDirectory + "/badguy1.png"))
        #self.Images.append(pygame.image.load(imageDirectory + "/badguy2.png"))
        #self.Images.append(pygame.image.load(imageDirectory + "/badguy3.png"))
        self.SpawnDelay = spawnDelay
        self.TimeToSpawn = 10
        self.Active = []
        self.Speed = 3
        self.Width = self.Images[0].get_width()
        self.Height = self.Images[0].get_height()
        self.Padding = self.Width/4

    def MoveAttackBlit(self, arena, player, arrows):
        self.Move(arena, player)
        self.Attack(player, arrows)
        self.Blit(arena)

    def Move(self, arena, player):
        if (0 >= self.TimeToSpawn):
            self.Spawn(arena, player)
            self.TimeToSpawn = self.SpawnDelay

        #print "Move ", len(self.Active)
        for b in self.Active:
            b.Move(player.Position, self.Speed)
            if not arena.InBounds(b.Position, self.Padding, self.Padding):
                b.Health = 0

        self.TimeToSpawn -= 1 

    def Spawn(self, arena, player):
        spawnPosition = [arena.Width, random.randint(20, arena.Height - 20)]
        #print "Spawn ", spawnPosition
        self.Active.append(BadGuy(player, spawnPosition))

    def Attack(self, player, arrows):
        bIndex = 0
        #print "Attack ", len(self.Active)
        for b in self.Active:
            if not b.Alive():
                continue
            for a in arrows.Active:
                if not a.Alive():
                    continue
                if Intersects (b.Position, self.Padding, a.Position, arrows.Padding):
                    b.Health -= a.Attack(b)
                    break

            if not b.Alive():
                continue
                                        
            if Intersects(b.Position, self.Padding, player.Position, player.Padding):
                print "Health: ", player.Health
                b.Health -= player.Attack(b)

        self.Active = filter(lambda bg: bg.Alive(), self.Active)
        arrows.Active = filter(lambda ar: ar.Alive(), arrows.Active)


    def Blit(self, arena):
        #print "Blit"
        for b in self.Active:
            #print "Drawing BG ", b.Position
            #print "image Index ", b.ImageIndex % 3
            arena.RotateAndBlit(self.Images[b.ImageIndex % 3], b.Position, b.Direction)

        
            
