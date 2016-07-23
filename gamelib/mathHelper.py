import math

def floor(x=0.0):
    """ (float) -> int
    Convert a floating point number to an integer by rounding down always.
    """
    return int(math.floor(x))

def ceil(x=0.0):
    """ (float) -> int
    Convert a floating point number to an integer by rounding up always.
    """
    return int(math.ceil(x))

def isMultiple(x, y=2):
    """ (int, [int]) -> bool
    Return True if x is a multiple of y, False otherwise.
    """
    return x % y == 0 and x != 0

def isEven(x):
    """ (int) -> bool
    Return True if the given number is even, False otherwise.
    """
    return isMultiple(x)

def normalize(vector):
    """ (list-or-tuple) -> list
    Return a vector with the same direction but with magnitude 1.
    """
    result = vector[:]
    result = list(result)
    magnitude = math.sqrt(result[0] ** 2 + result[1] ** 2)
    result[0] /= magnitude
    result[1] /= magnitude
    return result

def deltaX(enemyX, turretX):
    return enemyX - turretX

def deltaY(enemyY, turretY):
    return turretY - enemyY

def distance((x1, y1), (x2, y2)):
    return math.sqrt((deltaX(x2, x1))**2 + deltaY(y2, y1)**2)

def getXandY(radius, angle):
    x = math.cos(math.radians(angle))*radius
    y = math.sin(math.radians(angle))*radius
    return x, -y

def getAngle(deltaX, deltaY):
    """Get delta x and delta y between enemy and turret
    to get your triangle"""
    if deltaX == 0:
        deltaX += 0.1
    raa = math.degrees(abs(math.atan(float(deltaY)/deltaX)))
    raa = round(raa, 3)
    if deltaY>=0 and deltaX>=0:
        return raa
    elif deltaX<0 and deltaY<0:
        return 180 + raa
    elif deltaX<0:
        return 180 - raa
    elif deltaY<0:
        return 360 - raa
    

    


