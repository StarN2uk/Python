import pygame
import sys
from pygame.locals import *
from random import *
x = randint(1, 400)
y = randint(1, 300)
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
    cnt_txt = sysfont.render("HI", True, (0, 0, 0))
    screen.blit(cnt_txt, (x, y))
    x = randint(1, 400)
    y = randint(1, 300)
    pygame.display.update()
    CLOCK.tick(1)