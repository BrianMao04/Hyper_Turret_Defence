# Sam Raisbeck
# Day 3 of Pyweek (Monday)

from movableObjects import MovableObject
import mathHelper as m
from enemy import Enemy
import pygame
pygame.init()


class Bullet(MovableObject):

    def __init__(self, image, x, y, speed, damage=50):
        MovableObject.__init__(self, image, x, y)
        self.speed = speed
        self.damagePotential = damage
        
    def getSpeed(self, (x, y)):
        magnitude = m.normalize((x, y))
        self.speedX = magnitude[0]*self.speed
        self.speedY = magnitude[1]*self.speed

    # Inherits the update() method from MovableObject superclass.
    # This will increment the x and y values by the speed.
        

                                                                          
        
        

    
        
        
        
        
