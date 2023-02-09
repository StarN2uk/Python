import pygame
import sys
from pygame.locals import *
from random import *
c1 = 0
c2 = 0
c3 = 0
pygame.init()
screen = pygame.display.set_mode((400, 300))
sysfont = pygame.font.SysFont(None, 36)
CLOCK = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((255, 255, 255))
    c1 = randint(1, 255)
    c2 = randint(1, 255)
    c3 = randint(1, 255)
    cnt_txt = sysfont.render("Hello python", True, (c1, c2, c3))
    screen.blit(cnt_txt, (0, 0))
    pygame.display.update()
    CLOCK.tick(1)