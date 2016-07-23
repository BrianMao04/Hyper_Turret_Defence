###########################
# Programmer: samraisbeck
# Date: May 11-18, 2014
# Filename: fireTurret.py
# Description: A strong turret
###########################
from turret import Turret
from bullet import Bullet
from localvars import *

class FireTurret(Turret):
    """
    A one shot kill turret
    """

    name = 'Fire Turret'
    price = FIRE_SHOT_PRICE
    reward = FIRE_SHOT_REWARD
    description = 'Shoots fireballs for extra damage, but planes are immune.'
    def __init__(self, x=0, y=0, r=200):
        Turret.__init__(self, x, y, r)
        self.image = pygame.image.load(IMG_PATH_F_TURRET).convert_alpha()
        self.shotDelay = 700

    def shoot(self):
        if self.getShotTime():
            bullet = Bullet(IMG_PATH_F_BULLET, self.getRect().centerx,
                                self.getRect().centery, 11, damage=200)
            self.bullets.append(bullet)
    
        
