########################################
# File Name: Pyweek 18 Tower Defense
# Programmer: tender
# Date: May 10, 2014
# Description: Turret, enemy and point objects
########################################

import pygame, os
from movableObjects import MovableObject
from localvars import *
from mathHelper import *


class Enemy(MovableObject):
    """
    Class for enemies
    """

    def __init__(self, image, x, y, direction=RIGHT, topSpeed=4, health=100):
        """
        initialize stuff
        """
        MovableObject.__init__(self, image, x, y)
        self.topSpeed = topSpeed
        self.nextTurn = None
        self.health = health
        self.savedSpeeds = []
        self.savedDirection = None
        self.active = False
        self.initialDistanceFromWorld = 0
        self.rotatedImages = [self.image, pygame.transform.rotate(self.image, 90),
                              pygame.transform.rotate(self.image, 180),
                              pygame.transform.rotate(self.image, 270)]
        if direction == RIGHT: self.startMovingRight()
        elif direction == LEFT: self.startMovingLeft()
        elif direction == UP: self.startMovingUp()
        else: self.startMovingDown()

    def startMovingLeft(self):
        self.speedX = -self.topSpeed
        self.speedY = 0
        self.direction = LEFT
        self.image = self.rotatedImages[2]

    def startMovingRight(self):
        self.speedX = self.topSpeed
        self.speedY = 0
        self.direction = RIGHT
        self.image = self.rotatedImages[0]

    def startMovingUp(self):
        self.speedX = 0
        self.speedY = -self.topSpeed
        self.direction = UP
        self.image = self.rotatedImages[1]

    def startMovingDown(self):
        self.speedX = 0
        self.speedY = self.topSpeed
        self.direction = DOWN
        self.image = self.rotatedImages[3]

    def stop(self):
        self.speedX = 0
        self.speedY = 0
        self.direction = NODIR

    def setNextIntersection(self, other):
        """ (tuple) -> None
        Save the next turn given a 3-tuple containing (x, y, newDirection).
        newDirection should be a 0-4 constant from localvars. """
        self.nextTurn = other

    def getNextIntersection(self):
        return self.nextTurn

    def getReducedRect(self, sensitivity=2):
        """ (None, [int]) -> Rect
        Return a Rect object representing the collision box. """
        return pygame.Rect(self.x + self.w / 2.0 - sensitivity,
                           self.y + self.h / 2.0 - sensitivity,
                           2 * sensitivity, 2 * sensitivity)

    def paused(self):
        """ (None) -> bool
        Return True if the enemy is paused, False otherwise. """
        return self.speedX == 0 and self.speedY == 0 and self.savedDirection is not None

    def pause(self):
        """ (None) -> None
        Pause the motion of the enemy. """
        if self.paused():
            return
        self.active = False
        self.savedSpeeds = self.speedX, self.speedY
        self.savedDirection = self.direction
        self.stop()

    def unpause(self):
        """ (None) -> None
        Unpause the motion of an enemy. Only safe to call after calling pause() first. """
        if not self.paused(): return
        self.active = True
        self.speedX, self.speedY = self.savedSpeeds
        self.direction = self.savedDirection
        self.savedSpeeds = []
        self.savedDirection = None

    def alive(self):
        """ (None) -> bool
        Return True if the enemy is on screen and visible, False otherwise. """
        return self.visible and -1000 <= self.x <= 2000 and -1000 <= self.y <= 2000

    def dispose(self):
        """ (None) -> None
        Render the enemy object invisible and unusable.
        """
        if self.health <= 0:
            self.stop()
            self.visible = False
            self.x = DEFAULT_VALUE
            self.y = DEFAULT_VALUE
        
    
