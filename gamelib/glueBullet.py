########################################
# File Name: Pyweek 18 Tower Defense (glueBullet.py)
# Programmer: samraisbeck
# Date: May 15, 2014
# Description: Slow down thing
#####################################
from localvars import *
from bullet import Bullet

class GlueBullet(Bullet):
    def __init__(self, image, x, y, speed, damage=0, slowFactor=0.7):
        Bullet.__init__(self, image, x, y, speed, damage)
        self.slowFactor = slowFactor
        
