import sys
import numpy as np
import pygame
import math
import random
import time

class Dot:
    BLUE = (0, 0, 255)
    LIGHT_RED = (255, 100, 100)
    RED = (255, 0, 0)
    GREEN = (100, 255, 0)

    def __init__(self, n, speed, color=BLUE):
        self.x = random.random()
        self.y = random.random()
        self.status = 0
        self.cnt = 0
        if self.x > 0.49 and self.x < 0.51:
            self.x += 0.02
        if self.y > 0.49 and self.y < 0.51:
            self.y += 0.02
        self.vx = speed * random.random()
        self.vy = speed * random.random()
        self.x += self.vx
        self.y += self.vy
        self.color = color
            
    def infect(self, color=LIGHT_RED):
        self.status = 1
        self.cnt = time.time()
        self.color = color

    def reverse(self):
        if self.x < 0 or self.x > 1:
            self.vx = -1 * self.vx
        if self.y < 0 or self.y > 1:
            self.vy = -1 * self.vy
        if self.x > 0.49 and self.x < 0.51:
            self.vx = -1 * self.vx
        if self.y > 0.49 and self.y < 0.51:
            self.vy = -1 * self.vy
        self.x += self.vx
        self.y += self.vy

    def draw(self, windowSurface, xmax, ymax, radius):
        pygame.draw.circle(windowSurface, self.color, \
                               (int(xmax * self.x), int(ymax * self.y)), radius, 0)

    def infectious(self, color=RED):
        self.status = 2
        self.color = color

    def recovered(self, color=GREEN):
        self.status = 3
        self.color = color

