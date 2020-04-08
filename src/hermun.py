import numpy as np
import pygame
import Einn


WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# set up pygame
pygame.init()

# set up the window
xmax = 600
ymax = 400
windowSurface = pygame.display.set_mode((xmax, ymax))
pygame.display.set_caption('Covid-19 hermir')

FRAMES_PER_SECOND = 30
fpsClock = pygame.time.Clock()
g = Einn



g.draw(pygame, windowSurface)



while True:
   # for i in range(n):
    #    # Reverse directon if point hits the boundary
     #   if x[i] < 0 or x[i] > 1:
      #      vx[i] = -1 * vx[i]
       # if y[i] < 0 or y[i] > 1:
        #    vy   [i] = -1 * vy[i]
   # x[i] += vx[i]
   # y[i] += vy[i]

  # for i in range(n):



    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FRAMES_PER_SECOND)
