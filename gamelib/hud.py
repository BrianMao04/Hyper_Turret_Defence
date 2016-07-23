###########################
# Programmer: kendev55
# Date: May 11-18, 2014
# Filename: hud.py
# Description: Heads-up display sidebar class
###########################
import pygame
from pygame.locals import *
from localvars import *
from mathHelper import *
from graphicButton import GraphicButton


class HUD(object):

    def __init__(self, rectBounds, colour, *turrets):
        """ (Rect, tuple-of-int) -> HUD
        Instantiate HUD sidebar with given boundaries and RGB background colour. """
        if isinstance(rectBounds, pygame.Rect):
            self.rect = rectBounds
        else:
            self.rect = pygame.Rect(rectBounds)
        self.left = self.rect.left
        self.right = self.rect.right
        self.top = self.rect.y
        self.bottom = self.rect.y + self.rect.h
        self.width = self.rect.width

        self.bgrdColour = colour
        self.textColour = self.getComplementary(self.bgrdColour)
        self.font = EIGHT_BIT_FONT
        self.font2 = EIGHT_BIT_FONT_SMALL
        self.spacing = 25
        self.blipSize = 50

        self.health = None
        self.money = None
        self.waveNum = None
        self.textItems = []
        self.turrets = list(turrets)
        self.turrets.sort(key=lambda x: x.price)
        self.turretImages = []
        self.turretRects = []
        self.configureImages()

        pauseX = self.left + self.spacing
        pauseY = self.bottom - 2 * self.spacing
        startX = pauseX
        startY = self.bottom - 4 * self.spacing
        self.pauseButton = GraphicButton(IMG_PATH_PAUSE, pauseX, pauseY)
        self.startButton = GraphicButton(IMG_PATH_START, startX, startY)

    @staticmethod
    def getComplementary(colour):
        """ (tuple-of-int) -> tuple-of-int
        Return a new RGB colour tuple with the complementary colour. """
        return 255 - colour[0], 255 - colour[1], 255 - colour[2]

    def drawText(self, surface, text='', left=0, top=0):
        """ (Surface, [str], [int], [int]) -> None
        Draw text onto the Surface with the given co-ordinates. """
        fontSurf = self.font.render(str(text), True, self.textColour)
        fontRect = fontSurf.get_rect()
        fontRect.top = top
        fontRect.left = left
        surface.blit(fontSurf, fontRect)

    def drawParagraph(self, surface, text='', left=0, top=0, w=0):
        words = text.split()
        paragraph = []
        height = floor(self.font.size(text)[1] * 1.5)
        numRows = ceil(self.font2.size(text)[0] / float(w))
        for row in xrange(numRows + 5):
            paragraph.append([word for word in words if self.font.size(' '.join(words[:words.index(word) + 1]))[0] < w])
            del words[:len(paragraph[row])]
            paragraph[row] = ' '.join(paragraph[row])
            self.drawText(surface, paragraph[row], left, top + height * row)

    def configureImages(self):
        """ (None) -> None
        Load image blips for each turret. """
        for i in xrange(len(self.turrets)):
            image = self.turrets[i].image
            image = pygame.transform.scale(image, [self.blipSize] * 2)
            try:
                self.turretImages[i] = image.convert_alpha()
            except IndexError:
                self.turretImages.append(image.convert_alpha())

    def configureRect(self, i, x, y):
        """ (int, int, int) -> None
        Save Rect boundaries for the given turret image index and top left co-ordinates.  """
        if len(self.turretRects) == len(self.turrets):
            return
        rect = self.turretImages[i].get_rect()
        rect.topleft = x, y
        self.turretRects.append(rect)

    def update(self, health, money, wave):
        """ (int, int, int, Turret-objects) -> None
        Update sidebar HUD with the given values. """
        self.health = 'Health:' + str(health)
        self.money = '$' + str(money)
        self.waveNum = 'Wave ' + str(wave)
        self.textItems = [self.health, self.money, self.waveNum]

    def draw(self, surface):
        """ (Surface) -> None
        Draw the HUD sidebar onto the given surface. """
        pygame.draw.rect(surface, self.bgrdColour, self.rect)
        y = self.spacing
        if self.textItems:
            for string in self.textItems:
                self.drawText(surface, text=string, left=self.left + self.spacing, top=y)
                y += self.spacing
        turretsInRow = floor(float(self.width - 4 * self.spacing) / self.blipSize)
        if self.turretImages:
            x = self.spacing + self.left
            for i in xrange(len(self.turretImages)):
                surface.blit(self.turretImages[i], (x, y))
                self.configureRect(i, x, y)
                x += self.blipSize + self.spacing // 2
                if isMultiple(i+1, turretsInRow):
                    x = self.spacing + self.left
                    y += self.blipSize + self.spacing
        index = self.highlighted()
        y += 3 * self.spacing
        if index >= 0:
            pygame.draw.rect(surface, self.textColour, self.turretRects[index], 2)
            self.drawText(surface, text=self.turrets[index].name, left=self.spacing + self.left, top=y)
            y += self.spacing
            self.drawText(surface, text='$' + str(self.turrets[index].price), left=self.spacing + self.left, top=y)
            y += 2 * self.spacing
            self.drawParagraph(surface, self.turrets[index].description, self.spacing // 2 + self.left, y,
                               self.width - self.spacing)
        self.startButton.update()
        self.pauseButton.update()
        self.startButton.draw(surface)
        self.pauseButton.draw(surface)

    def shouldPause(self):
        """ (None) -> bool
        Return True if the pause button is pressed, False otherwise. """
        return self.pauseButton.pressed()

    def shouldStart(self):
        """ (None) -> bool
        Return True if the start button is pressed, False otherwise. """
        return self.startButton.pressed()

    def highlighted(self):
        """ (None) -> int
        Return the index of the currently highlighted turret, or -1 if there
        is no mouse collision. """
        result = -1
        mouseX, mouseY = pygame.mouse.get_pos()
        if self.turretImages:
            for rect in self.turretRects:
                if rect.collidepoint(mouseX, mouseY):
                    result = self.turretRects.index(rect)
        return result