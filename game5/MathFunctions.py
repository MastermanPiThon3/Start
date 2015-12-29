import math

X = 0
Y = 1

class Range:
    def __init__(self, minimum, maximum):
        self.Min = minimum
        self.Max = maximum

def AngleBetween(pos0, pos1, offset):
    pos1 = OffsetPosition(pos1, offset)
    xDist = pos0[X] - pos1[X]
    yDist = pos0[Y] - pos1[Y]
    return math.atan2(yDist, xDist)

def OffsetPosition(position, offset):
    return [position[X] + offset[X], position[Y] + offset[Y]]

def InDegrees(radians):
    return 360 - radians * 57.3

def OffsetDistance(position, distance, direction):
    movement = [math.cos(direction) * distance, math.sin(direction) * distance]
    return OffsetPosition(position, movement)        

def Intersects(pos0, pad0, pos1, pad1):
    ptotal = pad0 + pad1
    xIntersects = (pos0[X] - ptotal) <= pos1[X] <= (pos0[X] + ptotal)
    yIntersects = (pos0[Y] - ptotal) <= pos1[Y] <= (pos0[Y] + ptotal)
    return xIntersects and yIntersects
