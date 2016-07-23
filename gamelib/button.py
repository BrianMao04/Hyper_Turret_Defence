import pygame
from localvars import *

class Button(object):
    """ An on-screen Pygame-based button. """
    
    def __init__(self, text, x, y, w=100, h=40, middle=False, colouron=(0,0,0), colouroff=(5,5,255)):
        self.text = text                                        # caption
        if middle:                                              # center the button at the given co-ordinates
            x -= w // 2                                         # if the user requests this
            y -= h // 2
        self.rect = pygame.Rect(x, y, w, h)                     # Rect bounds
        self.colour_on = colouron                               # active colour
        self.colour_off = colouroff                             # inactive colour
        self.pressed = False                                    
        self.hovering = False                                   # mouse-over flag
        self.font = pygame.font.Font('freesansbold.ttf', 32)    # Font object
        self.font_surf = None                                   # font Surface
        self.font_rect = None                                   # font Rect bounds
        self.init_text()                                        # initialize text

    def init_text(self):
        # must be called before using the button to initialize the text Rect and Surface
        self.font_surf = self.font.render(self.text, True, self.colour_on)
        self.font_rect = self.font_surf.get_rect()
        self.font_rect.centerx = (self.rect.left + self.rect.right) / 2
        self.font_rect.centery = (self.rect.top + self.rect.bottom) / 2

    def update(self, events):
        # determine if the mouse cursor is hovering or clicking the button
        self.hovering = self.rect.collidepoint(pygame.mouse.get_pos())
        self.pressed = False
        for event in events:
            if event.type == MOUSEBUTTONUP and self.hovering:
                self.pressed = True

    def draw(self, surface):
        # draw a button as a rectangle with text; also update the font Surface
        if self.hovering:
            pygame.draw.rect(surface, self.colour_on, self.rect, 2)
            self.font_surf = self.font.render(self.text, True, self.colour_on)
        else:
            pygame.draw.rect(surface, self.colour_off, self.rect, 2)
            self.font_surf = self.font.render(self.text, True, self.colour_off)
        # blit the text onto the game window
        surface.blit(self.font_surf, self.font_rect)
