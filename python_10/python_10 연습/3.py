import sys
import pygame
from pygame.locals import *
pygame.init()
SURFACE = pygame.display.set_mode((300, 300))
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
    rec = Rect(50, 40, 200, 220)
    pygame.draw.circle(SURFACE, GREEN, (150, 150), 150)
    pygame.draw.rect(SURFACE, BLUE, rec)
    pygame.draw.polygon(SURFACE, RED, [[100, 100], [100, 200], [200, 200]])
    pygame.draw.polygon(SURFACE, BLACK, [[100, 100], [200, 100], [200, 200]])
    pygame.display.update()
    CLOCK.tick(1)