###########################
# Programmer: gamecube
# Date: May 11-18, 2014
# Filename: towerclass.py
# Description: Tower class
###########################
import pygame
pygame.init()


class Sound(object):
    def __init__(self, filepath, musicpresent):
        self.filepath=filepath
        self.musicpresent=musicpresent

        if musicpresent==True:
            pygame.mixer.music.load(filepath)
        else:
            self.soundeffect=pygame.mixer.Sound(filepath)

    def play(self,loop=0):
        if self.musicpresent==True:
            pygame.mixer.music.play(loop)
        else: 
            self.soundeffect.play(loop)
            
    def stop(self):
        if self.musicpresent==True:
            pygame.mixer.music.stop()
        else: 
            self.soundeffect.stop()
            
    def pause(self):
        if self.musicpresent==True:
            pygame.mixer.music.pause()
        else: 
            self.soundeffect.stop()

    def set_volume(self, volume):
        """
        Volume can be anywhere from 0.0 to 1.0
        """
        if self.musicpresent==True:
            pygame.mixer.music.set_volume(volume)
        else:
            self.soundeffect.set_volume(volume)
    
