########################################
# File Name: Pyweek 18 Tower Defense
# Programmer: tender
# Date: May 10, 2014
# Description: Turret, enemy and point objects
#####################################
import pygame
import mathHelper as m
from localvars import *
from bullet import Bullet

class Turret(object):
    """
    a standard gun turret that protects the tower
    """

    name = 'Basic Angle Turret'
    price = BASIC_ANGLE_PRICE
    reward = BASIC_ANGLE_REWARD
    description = 'Simple spinning turret with a decent range.'
    
    def __init__(self, x=0, y=0, r=200):
        """ ([int], [int], [int]) -> Turret
        Instantiate a Turret object with the given x, y co-ordinates and range.
        """
        self.image = pygame.image.load(IMG_PATH_TURRET).convert_alpha()   
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x = x
        self.y = y
        self.range = r
        self.angle = 0
        self.bullets = []
        self.lockOn = False
        self.Rect = self.getRect()
        self.test = True
        self.highlighted = True
        self.canShoot = False
        self.lastShot = 0
        self.currentShot = 0
        self.shotDelay = 500
        self.indexCount = 0
        self.rotatedImage = None
        self.rotatedCoords = None
        self.centerX = DEFAULT_VALUE
        self.centerY = DEFAULT_VALUE

    def clearInvisibleBullets(self):
        """ (None) -> None
        Remove nonvisible bullets from the list. """
        result = []
        for bullet in self.bullets:
            if bullet.visible:
                result.append(bullet)
        self.bullets = result[:]

    def getShotTime(self):
        self.currentShot = pygame.time.get_ticks()
        if self.currentShot - self.lastShot >= self.shotDelay:
            self.lastShot = self.currentShot
            return True
        return False

    def update(self, surface):
        self.centerX = self.getRect().centerx
        self.centerY = self.getRect().centery
        self.clearInvisibleBullets()
        self.draw(surface)
        if self.lockOn and self.canShoot:
            self.shoot()
            for bullet in self.bullets:
                if bullet.speedX == 0:
                    bullet.getSpeed(m.getXandY(self.range, self.angle)) 
                bullet.draw(surface, bullet.x, bullet.y) 
                bullet.update()
        
    def getRect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def rotated(self, image, angle):
        """ (Surface, int) -> Surface
        Return the given Surface rotated by the given number of degrees counter-clockwise."""
        originalRect = self.getRect()
        self.rotatedImage = pygame.transform.rotate(image, angle)
        rotatedRect = self.rotatedImage.get_rect()
        rotatedRect.center = originalRect.center
        return rotatedRect

    def draw(self, surface):
        """
        blit a turret on the game window
        """
        self.rotatedCoords = self.rotated(self.image, self.angle)
        if self.highlighted:
            x = self.getRect().centerx
            y = self.getRect().centery
            pygame.draw.circle(surface, BLACK, (x, y), self.range, 1)
        surface.blit(self.rotatedImage, self.rotatedCoords)

    def checkLockOn(self, x, y):
        """
        Checks if the turret and enemy are in range
        """
        if m.distance((self.x, self.y), (x, y)) <= self.range:
            self.lockOn = True
            return True
        else:
            self.lockOn = False
            return False

    def shoot(self):
        if self.getShotTime() and self.canShoot:
            bullet = Bullet(IMG_PATH_BULLET, self.getRect().centerx,
                            self.getRect().centery, 11)
            self.bullets.append(bullet)
