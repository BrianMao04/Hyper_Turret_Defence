########################################
# File Name: Pyweek 18 Tower Defense (glueTurret.py)
# Programmer: samraisbeck
# Date: May 15, 2014
# Description: Slow down thing
#####################################
from localvars import *
from turret import Turret
from glueBullet import GlueBullet

class GlueTurret(Turret):
    price = STICKY_TURRET_PRICE
    name = "Sticky Turret"
    description = 'Fires glue bullets to slow down enemies.'
    def __init__(self, x=0, y=0, r=200):
        Turret.__init__(self, x, y, r)
        self.image = pygame.image.load(IMG_PATH_G_TURRET).convert_alpha()

    def shoot(self):
        if self.getShotTime() and self.canShoot:
            
            bullet = GlueBullet(IMG_PATH_G_BULLET, self.getRect().centerx, \
                            self.getRect().centery, 5)
            self.bullets.append(bullet)
            
        
        
        
        
        
        
