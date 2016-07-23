###########################
# Programmer: gamecube
# Date: May 11-18, 2014
# Filename: localvars.py
# Description: Local variables class
###########################
import pygame, os
from pygame.locals import *
pygame.font.init()

# -------------------- data folder ------------------------------------
def getDataFilepath(filename):
    """ (str) -> str
    Return the exact path of the given filename, but in the data folder rather than gamelib. """
    root = os.path.dirname(os.path.dirname(__file__))
    result = os.path.join(root, 'data', filename)
    return result

GAME_NAME = 'HYPERTURRET  by 101 Factorial Dev Team'

ORIGIN = 0, 0

RIGHT = 0
UP = 1
LEFT = 2
DOWN = 3
NODIR = 4
DEFAULT_VALUE = -999

BASIC_ANGLE_TURRET = 0
FOUR_SHOT_TURRET = 1

BASIC_ANGLE_REWARD = 10
FOUR_SHOT_REWARD = 10
FIRE_SHOT_REWARD = 10
LONG_SHOT_REWARD = 10
EIGHT_SHOT_REWARD = 10

BASIC_ANGLE_PRICE = 100
FOUR_SHOT_PRICE = 150
STICKY_TURRET_PRICE = 300
FIRE_SHOT_PRICE = 1300
LONG_SHOT_PRICE = 650
EIGHT_SHOT_PRICE = 1100 

SLOW_FPS = 30
SMOOTH_FPS = 60
UNL_FPS = 1000

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

WHITE = (255,255,255)
BLACK = (0,0,0)

LGREEN = (100,255,100)  # L means light
YELLOW =(255,255,0)
GREY = (200,200,200)
DGREY = (150,150,150)
ORANGE = (255,150,0)                  
PURPLE = (150,5,255)                   
LBLUE = (150,190,220)

#-----------------
#Text Fonts
#-----------------
genericfont1 = pygame.font.Font('freesansbold.ttf', 100)
genericfont2 = pygame.font.Font('freesansbold.ttf', 50)  
genericfont3 = pygame.font.Font('freesansbold.ttf', 110)
genericfont4 = pygame.font.Font('freesansbold.ttf', 70)

CREDITS_FONT = pygame.font.Font('freesansbold.ttf', 20)
titlefont1 = pygame.font.Font('freesansbold.ttf', 18)
titlefont2 = pygame.font.Font('freesansbold.ttf', 40)
titlefont3 = pygame.font.Font('freesansbold.ttf', 120)
titlefont4 = pygame.font.Font('freesansbold.ttf', 100)

EIGHT_BIT_FONT = pygame.font.Font(getDataFilepath('PressStart2P.ttf'), 15)
EIGHT_BIT_FONT_SMALL = pygame.font.Font(getDataFilepath('thin_pixel-7.ttf'), 24)

IMG_PATH_TOWER = getDataFilepath('tower.png')
IMG_PATH_ENEMY1 = getDataFilepath('enemy1.png')
IMG_PATH_ENEMY2 = getDataFilepath('enemy2.png')
IMG_PATH_ENEMY3 = getDataFilepath('enemy3.png')
IMG_PATH_ENEMY4 = getDataFilepath('enemy4.png')
IMG_PATH_ENEMY5 = getDataFilepath('enemy5.png')
IMG_PATH_TURRET = getDataFilepath('turret.png')
IMG_PATH_4TURRET = getDataFilepath('fourturret.png')
IMG_PATH_8TURRET = getDataFilepath('eightShotTurret.png')
IMG_PATH_BULLET = getDataFilepath('bullet.png')
IMG_PATH_PAUSE = getDataFilepath('pause.png')
IMG_PATH_START = getDataFilepath('start.png')
IMG_PATH_RETURN = getDataFilepath('return.png')


IMG_PATH_G_TURRET = getDataFilepath('glueTurret.png')
IMG_PATH_G_BULLET = getDataFilepath('glueBullet.png')
IMG_PATH_F_TURRET = getDataFilepath('fireTurret.png')
IMG_PATH_F_BULLET = getDataFilepath('fireBullet.png')
IMG_PATH_LR_TURRET = getDataFilepath('longRange.png')
IMG_PATH_LR_BULLET = getDataFilepath('bullet.png')
IMG_PATH_DIRT = getDataFilepath('road.png')
IMG_PATH_GRASS = getDataFilepath('grass.png')

IMG_PATH_LVL1 = getDataFilepath('lvl1screenshot.png')
IMG_PATH_LVL2 = getDataFilepath('lvl2screenshot.png')
IMG_PATH_LVL3 = getDataFilepath('lvl3screenshot.png')
IMG_PATH_LVL4 = getDataFilepath('lvl4screenshot.png')
IMG_PATH_LVL5 = getDataFilepath('lvl5screenshot.png')

SOUND_PATH_SHOT = getDataFilepath('shot.wav')
SOUND_PATH_EXPLOSION = getDataFilepath('explosion.wav')

