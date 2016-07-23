########################################
# File Name: Pyweek 18 Tower Defense
# Programmer: samraisbeck
# Date: May 10, 2014
# Description: Turret, enemy and point objects
#####################################

from turret import Turret
from bullet import Bullet
from localvars import *

class LongRange(Turret):
    """
    a turret that shoots long range but weak and slow
    """

    name = "Long Range Turret"
    price = LONG_SHOT_PRICE
    reward = LONG_SHOT_REWARD
    description = 'Big detection radius for long-range shooting.'

    def __init__(self, x=0, y=0, r=400):
        Turret.__init__(self, x, y, r)
        self.image = pygame.image.load(IMG_PATH_LR_TURRET).convert_alpha()
        self.shotDelay = 1000

    def shoot(self):
        if self.getShotTime() and self.canShoot:
            bullet = Bullet(IMG_PATH_LR_BULLET, self.getRect().centerx,
                            self.getRect().centery, 30, damage=25)
            self.bullets.append(bullet)
        
        
    
