import sys
import numpy as np
import pygame
import math
import random
import time
from pygame.locals import *

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

    # Initial coordinates are uniformly random in (0, 1)
    x = np.random.rand(n)
    y = np.random.rand(n)
    status = np.zeros(n)
    cnt = np.zeros(n)

    # Move coordinates from border to area
    for i in range(n):
        if x[i] > 0.49 and x[i] < 0.51:
            x[i] += 0.02
        if y[i] > 0.49 and y[i] < 0.51:
            y[i] += 0.02

    # Point velocity is uniformly random in (0, speed)
    vx = speed * np.random.rand(n)
    vy = speed * np.random.rand(n)

    # Make one point infected and start recovery counter
    for i in range(0,3):
        status[i] = 1
        cnt[i] = time.time()

    # run the main loop
    while True:
        # Clear screen
        windowSurface.fill(WHITE)
        # Draw borders
        pygame.draw.line(windowSurface, BLACK, [0,ymax/2], [420,ymax/2], 3)
        pygame.draw.line(windowSurface, BLACK, [460,ymax/2], [xmax,ymax/2], 3)
        pygame.draw.line(windowSurface, BLACK, [xmax/2,0], [xmax/2,250], 3)
        pygame.draw.line(windowSurface, BLACK, [xmax/2,280], [xmax/2,ymax], 3)

        # Update positions
        for i in range(n):
            # Reverse directon if point hits the boundary
            if x[i] < 0 or x[i] > 1:
                vx[i] = -1 * vx[i]
            if y[i] < 0 or y[i] > 1:
                vy[i] = -1 * vy[i]
            # Reverse direction if point hits border
            if x[i] > 0.495 and x[i] < 0.505:
                if y[i] < 250/ymax or y[i] > 280/ymax:
                    vx[i] = -1 * vx[i]
                if y[i] > 250/ymax and y[i] < 251/ymax:
                    vy[i] = -1 * vy[i]
                if y[i] > 279/ymax and y[i] < 280/ymax:
                    vy[i] = -1 * vy[i]
            if y[i] > 0.495 and y[i] < 0.505:
                if x[i] < 420/xmax or x[i] > 460/xmax:
                    vy[i] = -1 * vy[i]
                if x[i] > 420/xmax and x[i] < 421/xmax:
                    vx[i] = -1 * vx[i]
                if x[i] > 459/xmax and x[i] < 460/xmax:
                    vx[i] = -1 * vx[i]
            x[i] += vx[i]
            y[i] += vy[i]

        # Redraw
        for i in range(n):
            if status[i] == 0:
                pygame.draw.circle(windowSurface, BLUE, \
                               (int(xmax * x[i]), int(ymax * y[i])), radius, 0)

            if status[i] == 1:
                pygame.draw.circle(windowSurface, LIGHT_RED, \
                               (int(xmax * x[i]), int(ymax * y[i])), radius, 0)
                # Check if infectious
                if time.time() - cnt[i] > infectious and cnt[i] != 0:
                        status[i] = 2
                        pygame.draw.circle(windowSurface, RED, \
                               (int(xmax * x[i]), int(ymax * y[i])), radius, 0)

            if status[i] == 2:
                # Check if recovered
                if time.time() - cnt[i] > recovery:
                        status[i] = 3
                        pygame.draw.circle(windowSurface, GREEN, \
                               (int(xmax * x[i]), int(ymax * y[i])), radius, 0)

        # Check if points meet each other   
        for i in range(n-1):
            for j in range(i+1,n):
                dist = math.sqrt(math.pow(x[i] - x[j],2) + math.pow(y[i] - y[j], 2))
                if dist < 2 * (radius/xmax):
                    # Check if one is infectious
                    if status[i] == 2 and status[j] == 0:
                        inf = random.random()
                        if inf < inf_prob:
                            status[j] = 1
                            cnt[j] = time.time()
                            
                    if status[j] == 2 and status[i] == 0:
                        inf = random.random()
                        if inf < inf_prob:
                            status[i] = 1
                            cnt[i] = time.time()

        # Redraw
        for i in range(n):
            if status[i] == 0:
                pygame.draw.circle(windowSurface, BLUE, \
                               (int(xmax * x[i]), int(ymax * y[i])), radius, 0)

            if status[i] == 1:
                 pygame.draw.circle(windowSurface, LIGHT_RED, \
                               (int(xmax * x[i]), int(ymax * y[i])), radius, 0)

            if status[i] == 2:
                pygame.draw.circle(windowSurface, RED, \
                               (int(xmax * x[i]), int(ymax * y[i])), radius, 0)

            if status[i] == 3:
                pygame.draw.circle(windowSurface, GREEN, \
                               (int(xmax * x[i]), int(ymax * y[i])), radius, 0) 
                
        # Event handling
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        fpsClock.tick(FRAMES_PER_SECOND)

