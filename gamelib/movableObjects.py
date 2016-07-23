# Sam Raisbeck
# Day 1 of Pyweek
import pygame
pygame.init()


class MovableObject(object):
    """ Generic movable object superclass """

    def __init__(self, image, x, y, speedX=0, speedY=0):
        if isinstance(image, str):
            self.image = pygame.image.load(image).convert_alpha()
        else:
            self.image = image.convert_alpha()
        self.x = x
        self.y = y
        self.w = self.image.get_width()
        self.h = self.image.get_height()
        self.speedX = speedX
        self.speedY = speedY
        self.visible = True
        self.collision = False

    def draw(self, surface, x, y):
        if self.visible:
            surface.blit(self.image, (x, y))

    def update(self):
        if self.visible:
            self.x += self.speedX
            self.y += self.speedY

    def dispose(self):
        self.visible = False

    def getRect(self):
        return pygame.Rect(self.x, self.y, self.w, self.h)

    

        
            
        
