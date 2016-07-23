###########################
# Programmer: kendev55
# Date: May 11-18, 2014
# Filename: game.py
# Description: Tower defense Game class
###########################
import copy, random
from localvars import *
from mathHelper import *
from hud import HUD
from tower import Tower
from enemy import Enemy
from turret import Turret
from plane import Plane
from fourShotTurret import FourShotTurret
from glueTurret import GlueTurret
from fireTurret import FireTurret
from longRange import LongRange
from eightShotTurret import EightShotTurret
from menu import Menu
from sound import Sound
from bigTank import HugeTank

class Game(object):

    modes = ['Waiting', 'In Play']

    def __init__(self, fps=60, fullscreen=False):
        """ (int, int, int, bool) -> Game
        Instantiate Game object with expected properties of a tower defense game. """
        pygame.init()
        
        # Parameter-based properties
        self.fps = fps
        self.fullscreen = fullscreen

        # Determine width and height
        self.screenW = pygame.display.list_modes()[0][0]
        self.screenH = pygame.display.list_modes()[0][1]
        if not self.fullscreen:
            self.screenW = floor(0.8 * self.screenW)
            self.screenH = floor(0.8 * self.screenH)

        # Display and framerate properties
        self.caption = GAME_NAME + ' - Left Mouse Button to select/place turret, drag by moving the mouse'
        self.displaySurf = None
        if self.fullscreen:
            self.flags = FULLSCREEN | DOUBLEBUF | HWACCEL
        else:
            self.flags = DOUBLEBUF | HWACCEL
        self.fpsClock = pygame.time.Clock()
        self.initializeDisplay()

        # Define and reset gameplay properties and objects
        self.money, self.wave, self.turrets, self.enemies, self.intersections, \
                    self.measuredFPS, self.tower, self.mode = [None] * 8
        self.reset()

        # HUD object 
        hudSize = 300
        hudRect = pygame.Rect(self.screenW - hudSize, 0, hudSize, self.screenH)
        hudColour = GREY
        self.hud = HUD(hudRect, hudColour, Turret(), FourShotTurret(), GlueTurret(),
                       FireTurret(), LongRange(), EightShotTurret())

        # Collision-related properties
        self.pathRects = []

        # Level appearance and elements
        self.intersectionSurface = pygame.Surface(self.displaySurf.get_size(), SRCALPHA | RLEACCEL, 32).convert_alpha()
        self.pathColour = ORANGE
        self.grassColour = LGREEN
        self.pathWidth = 50

        # Mouse and events
        self.mouseX, self.mouseY = 0, 0
        self.clicking = False
        self.dragging = False
        self.events = []

        # Health increment
        self.healthIncrement = 1

        # Menu object
        self.menu = Menu()

        # Background
        self.background = pygame.image.load(getDataFilepath(IMG_PATH_GRASS)).convert()
        self.pathImage = pygame.image.load(getDataFilepath(IMG_PATH_DIRT)).convert()

        # Sounds
        self.backgroundMusic = Sound(getDataFilepath('retro.wav'), True)
        self.hitSound = Sound(SOUND_PATH_SHOT, False)

        self.inPlay = True

    def reset(self, money=200, wave=1):
        """ ([int], [int]) -> None
        Reset money, wave number, and other similar game world properties. """
        self.money = money
        self.wave = wave
        self.turrets = []
        self.intersections = []
        self.enemies = []
        self.tower = Tower(IMG_PATH_TOWER, self.screenW / 2, self.screenH / 2)
        self.mode = self.modes[0]

    def incrementEnemyHealth(self, increment):
        for enemy in self.enemies:
            enemy.health *= increment

    def generateEnemies(self, x=1, separation=70):
        """ ([int], [int]) -> None
        Generate "x" number of enemies with the given separation for the tower defense game. """

        # Return immediately if there are no intersections loaded.
        if not self.intersections:
            print('WARNING: Enemies not loaded! Intersections must be loaded first.')
            return

        # Clear the list of enemies to start with.
        self.enemies = []

        # Gather information and create temporary variables.
        firstTurnX = self.intersections[0][0]
        firstTurnY = self.intersections[0][1]
        secondTurnX = self.intersections[1][0]
        secondTurnY = self.intersections[1][1]
        gap = x * separation
        xlist = []
        ylist = []
        direction = NODIR

        # Determine the starting direction and co-ordinate lists for the enemies.
        if firstTurnX == secondTurnX and firstTurnY > secondTurnY:
            xlist = [firstTurnX]
            ylist = xrange(firstTurnY, firstTurnY + gap, separation)
            direction = UP
        elif firstTurnX == secondTurnX:
            xlist = [firstTurnX]
            ylist = xrange(firstTurnY - gap, firstTurnY, separation)
            direction = DOWN
        elif firstTurnY == secondTurnY and firstTurnX > secondTurnX:
            xlist = xrange(firstTurnX, firstTurnX + gap, separation)
            ylist = [firstTurnY]
            direction = LEFT
        elif firstTurnY == secondTurnY:
            xlist = xrange(firstTurnX - gap, firstTurnX, separation)
            ylist = [firstTurnY]
            direction = RIGHT

        # Create enemies with the information determined above.
        w = Enemy(IMG_PATH_ENEMY1, 0, 0).w
        h = Enemy(IMG_PATH_ENEMY1, 0, 0).h
        assigned = False
        for x in xlist:
            for y in ylist:
                enemyType = random.randint(1, 5)
                if enemyType == 2 and not assigned:
                    self.enemies.append(Enemy(IMG_PATH_ENEMY2, x - w // 2, y - h // 2, direction, 3, 200))
                    assigned = True
                elif enemyType == 3 and not assigned and self.wave >= 2:
                    self.enemies.append(Enemy(IMG_PATH_ENEMY3, x - w // 2, y - h // 2, direction, 2, 300))
                    assigned = True
                elif enemyType == 4 and not assigned and self.wave >= 2:
                    self.enemies.append(Plane(IMG_PATH_ENEMY4, x - w // 2, y - h // 2, direction, 6, 100))
                    assigned = True
                elif enemyType == 5 and not assigned and self.wave >= 10:
                    self.enemies.append(HugeTank(IMG_PATH_ENEMY5, x - w // 2, y - h // 2, direction, 2, 500))
                    assigned = True
                else:
                    self.enemies.append(Enemy(IMG_PATH_ENEMY1, x - w // 2, y - h // 2, direction, health=100))
                    assigned = True
                self.enemies[-1].setNextIntersection(self.intersections[0])
                self.enemies[-1].initialDistanceFromWorld = distance((self.enemies[-1].x, self.enemies[-1].y),
                                                                     (firstTurnX, firstTurnY))
                assigned = False

        if self.wave % 5 == 0:
            self.healthIncrement += 1
        self.incrementEnemyHealth(self.healthIncrement)
        # Sort the list of enemies in terms of ascending distance away from the initial intersection.
        self.enemies.sort(key=lambda x: x.initialDistanceFromWorld)

    def makeStrSubstitutions(self, string):
        """ (str) -> str
        Return the input string but with human-readable keywords
        exchanged for co-ordinates and directions. """
        substitutions = {'RIGHT': RIGHT, 'LEFT': LEFT, 'UP': UP, 'DOWN': DOWN, 'WIDTH': self.hud.left,
                         'HEIGHT': self.screenH}
        result = string[:]
        for word in string.split():
            if word in substitutions:
                result = result.replace(word, str(substitutions[word]))
        return result

    def stretchIntersections(self):
        """ (None) -> None
        Stretch or compress intersection co-ordinates as necessary to fit them to screen. """
        # Return immediately if there are no intersections
        if not self.intersections:
            return
        # Gather info about the needed scaling for horizontal and vertical co-ordinates of each intersection
        temp = self.intersections[:]
        temp.sort(key=lambda x: x[0])
        horizontalStretch = (self.screenW - self.hud.width) / float(temp[-1][0] + self.pathWidth // 2)
        temp = self.intersections[:]
        temp.sort(key=lambda x: x[1])
        verticalStretch = self.screenH / float(temp[-1][1] + self.pathWidth)
        # Make it happen and leave the intersection direction intact
        for i in xrange(len(self.intersections)):
            self.intersections[i] = ceil(self.intersections[i][0] * horizontalStretch), \
                                    ceil(self.intersections[i][1] * verticalStretch), self.intersections[i][2]
        self.tower.x *= horizontalStretch
        self.tower.y *= verticalStretch

    def loadIntersections(self, filename):
        """ (None) -> tuple
        Load the saved intersections from file based on the current wave.
        Return the loaded intersection 3-tuples. """
        self.intersections = []
        data = open(getDataFilepath(filename), 'r')
        for line in data:
            intersection = self.makeStrSubstitutions(line).split()
            intersection = int(intersection[0]), int(intersection[1]), int(intersection[2])
            self.intersections.append(intersection)
        self.stretchIntersections()
        return self.intersections

    def loadTowerLoc(self, filename):
        """ (None) -> None
        Load the co-ordinates of the tower to defend. """
        data = open(getDataFilepath(filename), 'r').read().split()
        x = int(self.makeStrSubstitutions(data[-3]))
        y = int(self.makeStrSubstitutions(data[-2]))
        self.tower.x, self.tower.y = x - self.tower.w // 2, y - self.tower.h // 2
        newRect = self.tower.getRect().clamp(pygame.Rect(0, 0, self.screenW - self.hud.width, self.screenH))
        self.tower.x = newRect.x
        self.tower.y = newRect.y

    def incrementWave(self):
        """ (None) -> None
        Set up the level for the next wave. """
        self.wave += 1
        self.generateEnemies(4 * self.wave)
        for turret in self.turrets:
            turret.bullets = []
            turret.angle = 0

    def drawText(self, text, x=0, y=0):
        """ (str, [int], [int]) -> None
        Draw the given string such that the text matches up with the given top-left co-ordinates.
        Acts as a wrapper for the HUD drawText(). """
        self.hud.drawText(self.displaySurf, text=text, left=x, top=y)

    def handleAI(self):
        """ (None) -> None
        Force the enemies to turn at each intersection. """
        if not self.enemies or not self.intersections:
            return
        for enemy in self.enemies:
            nextTurn = enemy.getNextIntersection()            
            if not enemy.getReducedRect().collidepoint(nextTurn[0:2]):
                continue
            if nextTurn[-1] == LEFT: enemy.startMovingLeft()   
            elif nextTurn[-1] == RIGHT: enemy.startMovingRight()
            elif nextTurn[-1] == UP: enemy.startMovingUp()
            elif nextTurn[-1] == DOWN: enemy.startMovingDown()
            else: enemy.stop()
            intersectionIndex = self.intersections.index(nextTurn)  
            if intersectionIndex + 1 < len(self.intersections):  
                enemy.setNextIntersection(self.intersections[intersectionIndex + 1])
                
    def drawIntersections(self, surface):
        """ (Surface) -> None
        Draw a sequence of paths joining all of the intersections onto the given surface.
        Update the list of path Rect objects for collision detection. """
        if not self.intersections:
            return
        points, intersectionRects, joinRects, result = [], [], [], []
        half = floor(self.pathWidth / 2.0)
        for intersection in self.intersections:
            points.append((intersection[0], intersection[1]))
        for point in points:
            intersectionRects.append(pygame.Rect(point[0] - half, point[1] - half, 2 * half, 2 * half))
        for i in xrange(len(points) - 1):
            result.append(intersectionRects[i].union(intersectionRects[i + 1]))
            surface.blit(self.pathImage, (result[-1].x, result[-1].y), result[-1])
        self.pathRects = result

    def onPath(self, other):
        """ (int, int) -> bool
        Return True if the x and y co-ordinates represent a spot on the paths, False otherwise. """
        result = False
        if not self.pathRects:
            return result
        for rect in self.pathRects:
            if (isinstance(other, tuple) and rect.collidepoint(other)) or rect.colliderect(other):
                result = True
        return result

    def onGrass(self, other):
        """ (int, int) -> bool
        Return True if the x and y co-ordinates represent a spot on the grass, False otherwise. """
        return not self.onPath(other)

    def hoveringSidebar(self):
        """ (None) -> bool
        Return True if the mouse is hovering over the HUD sidebar, False otherwise. """
        return self.mouseX >= self.hud.left
        
    def initializeDisplay(self):
        """ (None) -> Surface
        Initialize the display Surface and update the caption and display settings. Only call once in __init__. """
        self.displaySurf = pygame.display.set_mode((self.screenW, self.screenH), self.flags)
        pygame.display.set_caption(self.caption)
        return self.displaySurf

    def redrawAndProceedTick(self):
        """ (None) -> None
        Redraw the screen, and delay to enforce the FPS. Call on every update. """
        pygame.display.flip()
        self.fpsClock.tick_busy_loop(self.fps)
        self.measuredFPS = self.fpsClock.get_fps()

    def terminate(self):
        """ (None) -> None
        Set the game to exit as soon as possible. """
        print('Game closing...')
        self.inPlay = False

    def handleQuitEvents(self, events):
        """ (list-of-Events) -> None
        Exit the game if Escape is pressed or if the close button is used. """
        for event in events:
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                self.terminate()

    def updateState(self):
        """ (None) -> None
        Update the state of the game based on the user selection on the sidebar. """
        if self.hud.shouldPause():
            self.backgroundMusic.pause()
            if self.menu.drawPauseMenu(self.displaySurf):
                self.__init__(self.fps, self.fullscreen)
                self.execute()
            self.menu.drawPauseMenu(self.displaySurf)
            self.backgroundMusic.play(-1)
        if self.hud.shouldStart():
            self.mode = self.modes[1]
        self.canRun()

    def updateEnemies(self):
        """ (None) -> None
        Update and draw all enemies and the central tower. """
        levelComplete = True
        for enemy in self.enemies:
            if self.mode == self.modes[0]:
                enemy.pause()
            elif self.mode == self.modes[1]:
                enemy.unpause()
            if enemy.alive():
                levelComplete = False
            enemy.update()

            self.tower.update(self.displaySurf, enemy)
            enemy.draw(self.displaySurf, enemy.x, enemy.y)
        if levelComplete and self.mode == self.modes[1]:
            self.mode = self.modes[0]
            self.incrementWave()

    def enemyIndex(self, enemy):
        try:
            return self.enemies.index(enemy)
        except IndexError:
            print('WARNING: Tried to access nonexistent enemy.')
            return 0

    @staticmethod
    def inRange(enemy, turret):
        """ (Enemy, Turret) -> None
        Return True if the enemy is in range of the given turret, False
        otherwise. """
        return distance(enemy.getRect().center, turret.getRect().center) < turret.range and enemy.active

    def setTarget(self, enemy, turret):
        """ (Enemy, Turret) -> None
        Lock onto a new enemy with the given turret. """
        if not isinstance(turret, FourShotTurret) and turret.canShoot:
            turret.angle = getAngle(deltaX(enemy.x, turret.x), deltaY(enemy.y, turret.y))
        turret.lockOn = True

    def provideReward(self, turret):
        """ (None, Turret) -> None
        Provide the player with a reward for each kill. """
        self.money += turret.reward

    def updateTurrets(self):
        """ (None) -> None
        Update and draw all turrets and bullets. """
        for turret in self.turrets:
            # Check if the turret is highlighted
            turret.highlighted = False
            if turret.getRect().collidepoint(self.mouseX, self.mouseY):
                turret.highlighted = True
                
            # Check for lock-on with enemies
            foundTarget = False
            for enemy in self.enemies:
                if self.inRange(enemy, turret):
                    self.setTarget(enemy, turret)
                    foundTarget = True
                    break
            if not foundTarget:
                turret.lockOn = False
                turret.bullets = []
                
            # Update and draw the turret
            turret.update(self.displaySurf)
            
            # Check for bullet collision with enemies
            for bullet in turret.bullets:
                for enemy in self.enemies:
                    bulletEnemyCollision = bullet.getRect().colliderect(enemy.getRect())
                    if bulletEnemyCollision and not isinstance(turret, FourShotTurret):
                        self.hitSound.play()
                        bullet.dispose()
                        turret.test = True
                        if not isinstance(turret, GlueTurret) or \
                                (isinstance(enemy, Plane) and not isinstance(turret, FireTurret)):
                            enemy.health -= bullet.damagePotential
                        else:
                            enemy.topSpeed *= bullet.slowFactor
                        enemy.dispose()
                        if enemy.health <= 0:
                            self.provideReward(turret)             
                    elif bulletEnemyCollision:
                        self.hitSound.play()
                        enemy.health -= bullet.damagePotential
                        enemy.dispose()
                        bullet.dispose()
                        if enemy.health <= 0:
                            self.provideReward(turret)

    def updateHud(self):
        """ (None) -> None
        Update and draw the HUD sidebar. """
        self.hud.update(self.tower.health, self.money, self.wave)
        self.hud.draw(self.displaySurf)

    def updateInputs(self):
        """ (None) -> None
        Get keyboard and mouse status and check for quit events. """
        self.mouseX, self.mouseY = pygame.mouse.get_pos()
        self.clicking = pygame.mouse.get_pressed()[0]
        self.events = pygame.event.get()
        self.handleQuitEvents(self.events)

    def addTurret(self, index):
        """ (int) -> None
        Add a turret with the given index to the list of turrets. """
        newTurret = copy.copy(self.hud.turrets[index])
        newTurret.x = DEFAULT_VALUE
        newTurret.y = DEFAULT_VALUE
        self.turrets.append(newTurret)

    def handleDragging(self):
        """ (None) -> None
        Facilitate dragging of turrets from the HUD sidebar to the game field. """
        overlapping = False
        index = self.hud.highlighted()
        clicked = False
        rects = [turret.getRect() for turret in self.turrets[0:-1]]
        if len(self.turrets) > 1:
            for rect in rects:
                if self.turrets[-1].getRect().colliderect(rect):
                    overlapping = True
        for event in self.events:
            if event.type == MOUSEBUTTONDOWN:
                clicked = True
        if self.dragging and clicked and self.onGrass(self.turrets[-1].getRect()) and not overlapping:
            self.dragging = False
            self.turrets[-1].canShoot = True
            self.money -= self.turrets[-1].price
        if index >= 0 and clicked and not self.dragging and self.money >= self.hud.turrets[index].price:
            self.dragging = True
            self.addTurret(index)
        if self.dragging and not clicked:
            self.turrets[-1].x = self.mouseX - self.turrets[-1].width // 2
            self.turrets[-1].y = self.mouseY - self.turrets[-1].height // 2
            self.turrets[-1].canShoot = False

    def update(self):
        """ (None) -> None
        Update the entire game state and draws all objects on the screen. """
        self.displaySurf.blit(self.background, ORIGIN)
        self.updateInputs()
        self.handleAI()
        self.updateEnemies()
        self.updateTurrets()
        self.updateHud()
        self.handleDragging()
        self.redrawAndProceedTick()
        self.updateState()

    def execute(self):
        """ (None) -> None
        Execute the Tower Defense game. """

        # Play background music and enter the title screen
        self.backgroundMusic.play(-1)
        self.menu.drawTitleMenu(self.displaySurf)
        filename = self.menu.drawSelectLevelScreen(self.displaySurf)

        # Load the first level properties
        self.loadTowerLoc(filename)
        self.loadIntersections(filename)
        self.generateEnemies(5)

        # Blit the tower and paths onto the background Surface
        self.drawIntersections(self.intersectionSurface)
        self.background.blit(self.intersectionSurface, ORIGIN)
        self.tower.draw(self.background)

        # Play!
        while self.inPlay:
            self.update()
        self.menu.drawLosePanel (self.displaySurf)
        self.menu.drawCredits(self.displaySurf)
        pygame.quit()

    def getRect(self):
        """ (None) -> Rect
        Return a pygame Rect object defining the display surface boundaries. """
        return self.displaySurf.get_rect()

    def canRun (self):
        if self.tower.health <= 0:
            self.terminate ()
