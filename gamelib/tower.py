###########################
# Programmer: gamecube
# Date: May 11-18, 2014
# Filename: towerclass.py
# Description: Tower class
###########################
from localvars import *
import pygame
from sound import Sound
pygame.init()

class Tower(object):
    def __init__(self, imagePath, x, y, hp=100):  
        self.image = pygame.image.load(imagePath)
        self.health = hp
        self.x = x
        self.y = y
        self.h = self.image.get_height()
        self.w = self.image.get_width()
        self.hitSound = Sound(SOUND_PATH_EXPLOSION, False)
        self.hitSound.set_volume(0.4)

    def getRect(self): 
        return pygame.Rect(self.x, self.y, self.w, self.h)

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def checkDestroyed(self):
        if self.health <= 0:
            self.x = DEFAULT_VALUE
            self.y = DEFAULT_VALUE
        
    def update(self, surface, enemy):
        if self.getRect().colliderect(enemy.getRect()):
            self.health -= 10
            self.hitSound.play()
            enemy.health = 0
            enemy.dispose()
            
        
        
        
        
