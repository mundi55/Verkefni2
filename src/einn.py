import pygame
import numpy as np

class einn:

    def __init__(self,stat):
        self.status = stat  #h,l,s
        self.svaedi = 0
        self.x = np.random.rand()
        self.y = np.random.rand()
        self.vx = speed * np.random.rand()
        self.vy = speed * np.random.rand()
        self.teljari = 0

    def teikna(self, pygame, windowSurface):
        pygame.draw.circle(windowSurface, BLUE, \
                           (int(600 * self.x), int(400 * self.y), 5, 0))


    def astand(self,st):
        if self.st == 0:  #Heilbriðgur
            self.status = 0
            return
        if self.st == 1:  #Sýktur
            self.status = 1
            return
        if self.st == 2:  #Búinn að jafna sig
            self.status = 2
            return



    def teljari(self):
        i =+1

