import numpy as np
import time
import pygame
import math
import random

class Einn:

    def __init__(self):
        self.status = 0
        self.svaedi = 0
        self.x = np.random.rand()
        self.y = np.random.rand()
        self.vx = 0.01 * np.random.rand()
        self.vy = 0.01 * np.random.rand()
        self.teljari = time.time()

    def draw(self, windowSurface, xmax, ymax, color):
        pygame.draw.circle(windowSurface, color,(int(xmax * self.x), int(ymax * self.y)), 5, 0)

    def reverse(self):
        # Reverse directon if point hits the boundary
        if self.x < 0 or self.x > 1:
            self.vx = -1 * self.vx
        if self.y < 0 or self.y > 1:
            self.vy = -1 * self.vy
        # Reverse direction if point hits border
        if self.x > 0.49 and self.x < 0.51:
            self.vx = -1 * self.vx
        if self.y > 0.49 and self.y < 0.51:
            self.vy = -1 * self.vy
        self.x += self.vx
        self.y += self.vy

    def collision(self,xmax,ymax,inf_prob,n):
        for i in range(n - 1):
            for j in range(i + 1, n):
                dist = math.sqrt(math.pow(dot[i].x - dot[j].x, 2) + math.pow(dot[i].y - dot[j].y, 2))
                if dist < 2 * (5 / xmax):
                    if dot[i].status == 2 and dot[j].status == 0:
                        inf = random.random()
                        if inf < inf_prob:
                            dot[j].status = 1
                            dot[j].teljari = time.time()

                    if status[j] == 1 and status[i] == 0:
                        inf = random.random()
                        if inf < inf_prob:
                            status[i] = 1
                            cnt[i] = time.time()

    def infect(self):
        self.status = 1

    def infectius(self):
        self.status = 2

    def healed(self):
        self.status = 3



