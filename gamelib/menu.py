#Trey Robinson -101Factorial
#Menu class that handles the main title menu

'''Changes:
DrawLosePanel function
'''

import pygame, sys
from localvars import *
from graphicButton import *; from button import *

def createFontSurface (text, colour, size, font=None):
    '''(str, (int, int, int), int, str) -> pygame.Surface
    Creates a pygame surface of rendered text argument with colour, size and given font
    '''
    return pygame.font.Font(font, size).render (text, 1, colour)

eight_bit = getDataFilepath('8-BIT WONDER.TTF')


class Menu(object):
    def __init__ (self):
        self.pausedWindow = pygame.image.load (getDataFilepath ('paused_window.png'))
        self.resumeButton = pygame.image.load (getDataFilepath ('resume_button.png'))
        self.returnButton = pygame.image.load (getDataFilepath ('return.png'))
        
    @staticmethod
    def drawTitleMenu (window):
        '''(pygame.Surface) -> None
        Draws the title screen + buttons onto the given surface while handling input
        '''
        window.fill (GREY)
        startButton = GraphicButton (getDataFilepath('start_button.png'),550 , 240)
        quitButton = GraphicButton (getDataFilepath('quit_button.png'), 550, 300)
        window.blit (createFontSurface (GAME_NAME, WHITE, 30, eight_bit), (0, 0))
        looping = True

        while looping:
            events = pygame.event.get ()

            for ev in events:
                if ev.type == pygame.QUIT or (ev.type == KEYDOWN and ev.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()

            if startButton.pressed():
                looping = False
            if quitButton.pressed():
                pygame.quit()
                sys.exit()

            startButton.draw (window)
            quitButton.draw (window)
            pygame.display.flip ()

    def drawPauseMenu (self, window):
        ''' (pygame.Surface) -> None
        Draws the pause screen onto the screen while handling user input
        '''
        pygame.mixer.music.stop ()

        pauseWindowRect = self.pausedWindow.get_rect()
        resumeButtonRect = self.resumeButton.get_rect()
        returnButtonRect=self.returnButton.get_rect()   

        centerx = window.get_rect().centerx
        centery = window.get_rect().centery
        resumeButton = GraphicButton(self.resumeButton, centerx - resumeButtonRect.w/2, centery - (resumeButtonRect.h/2+10) )

        returnButton = GraphicButton(self.returnButton, centerx - resumeButtonRect.w/2, centery - (resumeButtonRect.h/2 + 70) )

        window.blit (createFontSurface('PAUSE', WHITE, 30, eight_bit), (0,100))
        window.blit (self.pausedWindow, (centerx - pauseWindowRect.w/2, centery - pauseWindowRect.h/2))

        
        resumeButton.draw(window)
        returnButton.draw(window)  

        looping = True

        while looping:
            events = pygame.event.get ()

            for ev in events:
                if ev.type == pygame.QUIT or (ev.type == KEYDOWN and ev.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit ()

            if resumeButton.pressed ():
                looping = False
                
            if returnButton.pressed():
                return True
            
            resumeButton.draw(window)
            pygame.display.flip ()

        pygame.mixer.music.play (-1)

    @staticmethod
    def drawSelectLevelScreen (window):
        window.fill (GREY)
        buttons = []
        images= []

        for x in range (5):
            buttons.append (GraphicButton (getDataFilepath('level'+str(x+1)+'.png'),
                                           (window.get_rect().w)/5*x, 300))
            images.append (pygame.image.load (getDataFilepath ('lvl'+str(x+1)+
                                                               'screenshot.png')))
            images[x] = pygame.transform.scale (images[x], (buttons[x].rect.w,
                                                100))            
            
        levels = [1, 2, 3, 4, 5]

        

        looping = True
        while looping:
            events = pygame.event.get ()

            for ev in events:
                if ev.type == pygame.QUIT or (ev.type == KEYDOWN and ev.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit ()
            for i in xrange (len (buttons)):
                if buttons[i].pressed():
                    return getDataFilepath('lvl' + str (levels[i]) + '.txt')

                buttons[i].draw (window)
                window.blit (images[i], (window.get_rect().w/5*i, 400))
                
            window.blit (createFontSurface ("LEVEL SELECTION", WHITE, 20, eight_bit), (100, 0))
            pygame.display.flip ()

    def drawLosePanel (self, window):
        losePanel = pygame.image.load (getDataFilepath ('lose_panel.png'))
        contin = pygame.image.load (getDataFilepath ('continue.png'))
        centerx, centery = window.get_rect().w/2, window.get_rect().h/2
        continueButton = GraphicButton (contin, centerx - contin.get_rect().w/2,
                                        centery - contin.get_rect().h/2 + 20)

        looping = True
        while looping:
            events = pygame.event.get ()
            for ev in events:
                if ev.type == pygame.QUIT or (ev.type == KEYDOWN and ev.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit ()

            if continueButton.pressed ():
                return

            window.blit (losePanel, (centerx - losePanel.get_rect().w/2,
                                     centery - losePanel.get_rect().h/2))
            continueButton.draw (window)
            pygame.display.flip ()

    @staticmethod
    def drawCredits (window):
        '''(pygame.Surface) -> None
        Draws the final end credits onto the screen
        '''
        window.fill (BLACK)
        text = ['END', 'Credits:', 'kendev55 * Lead Programmer Main Game Logic File IO HUD Design',
                '101Factorial * Project Manager, Menu DesignFunctionality Music Composition Level Design',
                'gamecube * Local Variables Tower Functionality On-Screen Buttons Game Testing',
                'tender * Turret Functionality Enemy Functionality Money',
                'SamRaisbeck * Bullet Functionality Movable Objects Math functions',
                'neshant * Art Design Tower Upgrades Code Inspector Extraordinaire',
                'Hope you had fun! We sure did!', 'Pyweek 18']
        locations = [(0, 0), (30, 50), (30, 70), (30, 90), (30, 110), (30, 130), (30, 150), (30, 170), (30, 190), (30, 210),
            (30, 230)]

        for i in range (len (text)):
            window.blit (createFontSurface(text[i], WHITE, 10, eight_bit), (locations[i]))

        pygame.display.flip ()

        looping = True
        while looping:
            events = pygame.event.get ()
            for ev in events:
                if ev.type == pygame.QUIT or (ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE):
                    pygame.quit()
                    sys.exit()
