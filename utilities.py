import math
import random


def randColor():
    r, g, b = random.randrange(0, 255), random.randrange(
        0, 255), random.randrange(0, 255)
    return r, g, b


def pythTheorem(x1, y1, x2, y2):
    return math.hypot(x1-x2, y1-y2)
