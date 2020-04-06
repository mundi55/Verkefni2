import pygame
import numpy as np

class einn:

    def __init__(self,stat):
        self.status = stat #h,l,s
        self.svaedi = 0
        self.x = np.random.rand()
        self.y = np.random.rand()
        self.vx = speed * np.random.rand()
        self.vy = speed * np.random.rand()
        self.i = 0

    def teikna(self):
        pygame.draw.circle(windowSurface, BLUE, \
                           (int(600 * self.x), int(400 * self.y), 5, 0))


    def astand(self,st):
        if self.st = "s":
            self.status = "s"
            return
        if self.st = "l":
            self.status = "l"
            return
        if self.st = "h"
            self.status = "h"
            return


    def teljari(self):
        i =+1

