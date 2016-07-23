###########################
# Programmer: kendev55
# Date: May 11-18, 2014
# Filename: graphicButton.py
# Description: Graphical button class
###########################
import pygame
from localvars import *


class GraphicButton(object):
    """ A graphical Pygame-based button. """

    def __init__(self, image, x, y):
        """ (Surface, int, int) -> GraphicButton
        Instantiates a graphical button object. """
        if isinstance(image, str):
            self.image = pygame.image.load(image).convert_alpha()
        else:
            self.image = image.convert_alpha()
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = x, y
        self.visible = True

    def update(self):
        pass

    def pressed(self):
        """ (None) -> bool
        Return True if the button is clicked, False otherwise. """
        if not self.visible:
            return False
        return pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos())

    def draw(self, surface):
        """ (Surface) -> None
        Blit the graphical button onto the given Surface. """
        if self.visible:
            surface.blit(self.image, self.rect)

    def dispose(self):
        """ (None) -> None
        Render the button invisible and unusable. """
        self.visible = False

    def getRect(self):
        """ (None) -> Rect
        Return a Rect representing the boundaries of the button image. """
        return self.rect
        
