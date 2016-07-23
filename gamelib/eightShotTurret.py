#######################################
# File Name: Pyweek 18 Tower Defense
# Programmer: samraisbeck
# Date: May 17, 2014
# Description: Four shot turret
#####################################
from localvars import *
from fourShotTurret import FourShotTurret
import mathHelper as m
from bullet import Bullet


class EightShotTurret(FourShotTurret):

    name = '8-Shot Turret'
    price = EIGHT_SHOT_PRICE
    reward = EIGHT_SHOT_REWARD
    description = 'Shoots from all 4 sides and corners, a huge upgrade to the 4-shot.'

    def __init__(self, x=0, y=0, r=200, speed=4):
        FourShotTurret.__init__(self, x, y, r, speed)
        self.image = pygame.image.load(IMG_PATH_8TURRET).convert_alpha()

    def shoot(self):
        if not self.canShoot:
            return
        for i in range(8):
            bullet = Bullet(IMG_PATH_BULLET, self.getRect().centerx,
                                     self.getRect().centery, 1, damage=20)
            bullet.x -= bullet.w/2
            bullet.y -= bullet.h/2
            self.bullets.append(bullet)
            for bullet in self.bullets:
                if self.bullets.index(bullet) == 0:
                    bullet.speedX = 0
                    bullet.speedY = -self.speed
                elif self.bullets.index(bullet) == 1:
                    bullet.speedX = self.speed
                    bullet.speedY = 0
                elif self.bullets.index(bullet) == 2:
                    bullet.speedX = 0
                    bullet.speedY = self.speed
                elif self.bullets.index(bullet) == 3:
                    bullet.speedX = -self.speed
                    bullet.speedY = 0
                elif self.bullets.index(bullet) == 4:
                    bullet.speedX = float(self.speed)
                    bullet.speedY = -float(self.speed)
                elif self.bullets.index(bullet) == 5:
                    bullet.speedX = float(self.speed)
                    bullet.speedY = float(self.speed)
                elif self.bullets.index(bullet) == 6:
                    bullet.speedX = -float(self.speed)
                    bullet.speedY = float(self.speed)
                else:
                    bullet.speedX = -float(self.speed)
                    bullet.speedY = -float(self.speed)

    
            
