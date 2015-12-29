import math

X = 0
Y = 1

def AngleBetween(pos0, pos1, offset):
    pos1 = OffsetPosition(pos1, offset)
    xDist = pos0[X] - pos1[X]
    yDist = pos0[Y] - pos1[Y]
    return math.atan2(yDist, xDist)

def OffsetPosition(position, offset):
    return [position[X] + offset[X], position[Y] + offset[Y]]

def InDegrees(radians):
    return 360 - radians * 57.3
