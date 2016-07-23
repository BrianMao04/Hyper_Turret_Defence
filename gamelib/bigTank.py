########################################
# File Name: Pyweek 18 Tower Defense
# Programmer: tender
# Date: May 10, 2014
# Description: huge tank that moves slow but lots
#              of health
########################################

import pygame, os
from enemy import Enemy
from localvars import *
from mathHelper import *


class HugeTank(Enemy):
    """
    inherits all traits from enemy class
    """
    def __init__(self, image, x, y, direction = RIGHT, topSpeed = 3, health = 500):
        """
        init data stuff
        """
        Enemy.__init__(self, image, x, y, direction, topSpeed, health)

    def getReducedRect(self, sensitivity=10):
        """ (None, [int]) -> Rect
        Overrides the super class getReducedRect() but with a different default sensitivity. """
        return Enemy.getReducedRect(self, sensitivity)
