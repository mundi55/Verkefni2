import sys
import pygame
import random
import time

class Dot:
    # Colors to show different stages of infection
    BLUE = (0, 0, 255)
    LIGHT_RED = (255, 100, 100)
    RED = (255, 0, 0)
    GREEN = (100, 255, 0)

    # Set up characteristics for each dot
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
        self.color = color

    # Activated if dot becomes infected
    def infect(self, color=LIGHT_RED):
        self.status = 1
        self.cnt = time.time()
        self.color = color

    # Reverse dots when they hit edges
    def edges(self):
        if self.x < 0 or self.x > 1:
            self.vx = -1 * self.vx
        if self.y < 0 or self.y > 1:
            self.vy = -1 * self.vy
        self.x += self.vx
        self.y += self.vy

    # Adds quarantine borders
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

    # Adds holes to quarantine borders to create spillage
    def break_quarantine(self, xmax, ymax):
        if self.x < 0 or self.x > 1:
            self.vx = -1 * self.vx
        if self.y < 0 or self.y > 1:
            self.vy = -1 * self.vy
        if self.x > 0.49 and self.x < 0.51:
            if self.y < 250/ymax or self.y > 280/ymax:
                self.vx = -1 * self.vx
            if self.y > 249/ymax and self.y < 251/ymax:
                self.vy = -1 * self.vy
            if self.y > 279/ymax and self.y < 281/ymax:
                self.vy = -1 * self.vy
        if self.y > 0.49 and self.y < 0.51:
            if self.x < 420/xmax or self.x > 460/xmax:
                self.vy = -1 * self.vy
            if self.x > 419/xmax and self.x < 421/xmax:
                self.vx = -1 * self.vx
            if self.x > 459/xmax and self.x < 461/xmax:
                self.vx = -1 * self.vx
        self.x += self.vx
        self.y += self.vy

    # Draws the dot visually
    def draw(self, windowSurface, xmax, ymax, radius):
        pygame.draw.circle(windowSurface, self.color, \
                               (int(xmax * self.x), int(ymax * self.y)), radius, 0)

    # Activated when infected dot becomes infectious
    def infectious(self, color=RED):
        self.status = 2
        self.color = color

    # Activated when infected dot recovers
    def recovered(self, color=GREEN):
        self.status = 3
        self.color = color

    # Implements social distancing
    def social_dist1(self):
        self.vx = -1 * self.vx
        self.x += self.vx

    def social_dist2(self):
        self.vy = -1 * self.vy
        self.y += self.vy
