import sys
import pygame
from pygame.locals import *
pygame.init()
SURFACE = pygame.display.set_mode((400, 300))
CLOCK = pygame.time.Clock()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit
    SURFACE.fill(WHITE)
    rec = Rect(20, 10, 60, 40)
    pygame.draw.rect(SURFACE, RED, rec)
    pygame.draw.circle(SURFACE, GREEN, (120, 50), 10)
    pygame.draw.polygon(SURFACE, BLUE, [[50, 50], [0, 100], [100, 100]])
    pygame.draw.line(SURFACE,BLACK, [120, 0], [120, 100])
    pygame.display.update()
    CLOCK.tick(1)