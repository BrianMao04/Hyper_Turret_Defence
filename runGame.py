###########################
# Programmer: kendev55
# Date: May 11-18, 2014
# Filename: runGame.py
# Description: Launching point for Tower Defense game
###########################

from gamelib.game import *

if __name__ == '__main__':
    g = Game(SMOOTH_FPS, True)
    g.execute()

    
