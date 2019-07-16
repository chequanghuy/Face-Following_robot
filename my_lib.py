import math
def distance(center, another_center):
    a = (center[0] - another_center[0])**2
    b = (center[1] - another_center[1])**2
    return math.sqrt(a+b)
