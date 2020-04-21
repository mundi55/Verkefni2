import sys
import numpy as np
import pygame
import math
import random
import time
from pygame.locals import *
from dot import Dot

class Simulation:
    # set up the colors (RGB - red-green-blue values)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    LIGHT_RED = (255, 100, 100)
    RED = (255, 0, 0)
    GREEN = (100, 255, 0)

    # set up pygame
    pygame.init()

    # set up the window
    xmax = 600
    ymax = 400
    windowSurface = pygame.display.set_mode((xmax, ymax))
    pygame.display.set_caption('Covid-19 hermir')

    FRAMES_PER_SECOND = 30
    fpsClock = pygame.time.Clock()

    n = 50 # Number of points
    speed = 0.01
    radius = 5
    infectious = 2 # Time it takes to become infectious (sec)
    recovery = 7 # Time it takes to recover (sec)
    inf_prob = 0.7 # Probability of infection when points meet
    dot = list()

    for i in range(n):
        dot.append(Dot(n, speed))

    for i in range(0,3):
        dot[i].infect()

    # run the main loop
    while True:
        # Clear screen
        windowSurface.fill(WHITE)
        # Draw borders
        pygame.draw.line(windowSurface, BLACK, [0,ymax/2], [xmax,ymax/2], 3)
        pygame.draw.line(windowSurface, BLACK, [xmax/2,0], [xmax/2,ymax], 3)
        
        # Update positions
        for i in range(n):
            dot[i].reverse()

        # Redraw
        for i in range(n):
            dot[i].draw(windowSurface,xmax, ymax, radius)

        for i in range(n):
            if time.time() - dot[i].cnt > infectious and dot[i].cnt != 0:
                dot[i].infectious()

            if time.time() - dot[i].cnt > recovery and dot[i].status == 2:
                dot[i].recovered()

        # Redraw
        for i in range(n):
            dot[i].draw(windowSurface, xmax, ymax, radius)
            
        # Check if points meet each other   
        for i in range(n-1):
            for j in range(i+1,n):
                dist = math.sqrt(math.pow(dot[i].x - dot[j].x,2) + math.pow(dot[i].y - dot[j].y, 2))
                if dist < 2 * (radius/xmax):
                    # Check if one is infectious
                    if dot[i].status == 2 and dot[j].status == 0:
                        inf = random.random()
                        if inf < inf_prob:
                            dot[j].infect()
                            
                    if dot[j].status == 2 and dot[i].status == 0:
                        inf = random.random()
                        if inf < inf_prob:
                            dot[i].infect()

        # Redraw
        for i in range(n):
            dot[i].draw(windowSurface, xmax, ymax, radius)

        # Event handling
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        fpsClock.tick(FRAMES_PER_SECOND)
