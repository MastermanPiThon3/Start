import random
import pygame
from pygame.locals import *
from MathFunctions import *


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
            image = pygame.image.load(imageDirectory + "/badguy" + str(i) + ".png")
            self.Images.append(pygame.transform.flip(image, True, False))
        self.SpawnDelay = spawnDelay
        self.TimeToSpawn = 10
        self.Active = []
        self.Speed = 3
        self.Width = self.Images[0].get_width()
        self.Height = self.Images[0].get_height()
        self.Center = [self.Width/2, self.Height/2]
        self.Padding = self.Width/5

    def MoveAttack(self, arena, player, arrows):
        self.Move(arena, player)
        self.Attack(player, arrows)

    def Move(self, arena, player):
        if (0 >= self.TimeToSpawn):
            self.Spawn(arena, player)
            self.TimeToSpawn = self.SpawnDelay

        #print "Move ", len(self.Active)
        for b in self.Active:
            b.Move(player.Position, self.Speed)
            if not arena.InBounds(b.Position, 0, self.Padding):
                b.Health = 0

        self.Active = filter(lambda bg: bg.Alive(), self.Active)

        self.TimeToSpawn -= 1 

    def Spawn(self, arena, player):
        spawnPosition = [arena.Width - 20, random.randint(20, arena.Height - 20)]
        #print "Spawn ", spawnPosition
        self.Active.append(BadGuy(player, spawnPosition))

    def Attack(self, player, arrows):
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
                #print "Health: ", player.Health
                b.Health -= player.Attack(b)

        self.Active = filter(lambda bg: bg.Alive(), self.Active)
        arrows.Active = filter(lambda ar: ar.Alive(), arrows.Active)


    def Blit(self, arena):
        #print "Blit"
        for b in self.Active:
            #print "Drawing BG ", b.Position
            #print "image Index ", b.ImageIndex % 3
            arena.RotateAndBlit(self.Images[b.ImageIndex % 3], b.Position, b.Direction)
