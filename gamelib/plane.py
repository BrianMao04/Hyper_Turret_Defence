########################################
# File Name: Pyweek 18 Tower Defense
# Programmer: tender
# Date: May 10, 2014
# Description: a plane enemy that zooms at cost of
#              health and stuff
########################################

import pygame, os
from enemy import Enemy
from localvars import *
from mathHelper import *


class Plane(Enemy):
    """
    Inherits all traits from enemy
    """

    def __init__(self, image, x, y, direction = RIGHT, topSpeed = 5, health = 50):
        """
        initialize stuff
        """
        Enemy.__init__(self, image, x, y, direction, topSpeed, health)
        self.originalTopSpeed = topSpeed
        self.lastTurbo = 0
        self.currentTurbo = 0
        self.turboDelay = 3000
        self.turboTime = 700
    
    def getTurboTime(self):
        """
        Speed up plane for short time after 5 seconds
        """
        self.currentTurbo = pygame.time.get_ticks()
        if self.currentTurbo - self.lastTurbo >= self.turboDelay:
            self.lastTurbo += ceil(0.02 * (self.currentTurbo - self.lastTurbo))
            return True
        return False

    def getReducedRect(self, sensitivity=10):
        """ (None, [int]) -> Rect
        Overrides the super class getReducedRect() but with a different default sensitivity. """
        return Enemy.getReducedRect(self, sensitivity)

    def update(self):
        if self.visible:
            self.x += self.speedX
            self.y += self.speedY

        if self.getTurboTime():
            self.topSpeed = self.originalTopSpeed * 2
        else:
            self.topSpeed = self.originalTopSpeed
