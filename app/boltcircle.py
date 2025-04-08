import math
from typing import List, Tuple


def bolt_circle(diameter, num_holes):
    angle = 360 / num_holes
    coordinates = []
    for i in range(num_holes):
        x = diameter/2 * math.cos(math.radians(i*angle))
        y = diameter/2 * math.sin(math.radians(i*angle))
        coordinates.append((x, y))
    return coordinates
    return coordinates
