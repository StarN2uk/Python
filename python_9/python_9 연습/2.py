import pygame
import sys
from pygame.locals import *
from random import *
color = 0
pygame.init()
screen = pygame.display.set_mode((400, 300))
sysfont = pygame.font.SysFont(None, 36)
CLOCK = pygame.time.Clock()
Black = (0, 0, 0)
Blue = (0, 0, 255)
Red = (255, 0, 0)
Green = (0, 255, 0)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((255, 255, 255))
    color = randint(1, 4)
    if color == 1:
        cnt_txt = sysfont.render("Hello python", True, Black)
    elif color == 2:
        cnt_txt = sysfont.render("Hello python", True, Blue)
    elif color == 3:
        cnt_txt = sysfont.render("Hello python", True, Red)
    else:
        cnt_txt = sysfont.render("Hello python", True, Green)
    screen.blit(cnt_txt, (0, 0))
    pygame.display.update()
    CLOCK.tick(1)