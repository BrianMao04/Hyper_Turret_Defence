########################################
# File Name: Pyweek 18 Tower Defense
# Programmer: samraisbeck
# Date: May 14, 2014
# Description: Four shot turret
#####################################
from bullet import Bullet
from turret import Turret
from localvars import *
import mathHelper as m

class FourShotTurret(Turret):

    name = '4-Shot Turret'
    price = FOUR_SHOT_PRICE
    reward = FOUR_SHOT_REWARD
    description = 'Larger detection range, shooting from all 4 sides.'

    def __init__(self, x=0, y=0, r=250, speed=5):
        Turret.__init__(self, x, y, r)
        self.image = pygame.image.load(IMG_PATH_4TURRET).convert_alpha()
        self.speed = speed

    def shoot(self):
        for i in range(4):
            bullet = Bullet(IMG_PATH_BULLET, self.getRect().centerx,
                                     self.getRect().centery, 1)
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
                else:
                    bullet.speedX = -self.speed
                    bullet.speedY = 0

    def update(self, surface):
        self.centerX = self.getRect().centerx
        self.centerY = self.getRect().centery
        self.draw(surface)
        self.clearInvisibleBullets()
        if self.lockOn and self.test and self.canShoot:
            self.shoot()
            self.test = False
        for bullet in self.bullets:
            distance = m.distance((self.centerX, self.centerY),
                                  (bullet.x, bullet.y))
            bullet.draw(surface, bullet.x, bullet.y)
            bullet.update()
            if distance >= self.range * 1.5:
                self.bullets.remove(bullet)
        if len(self.bullets) == 0:
            self.test = True
                
                
                
    
    


    
    

