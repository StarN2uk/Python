import sys
import pygame
from pygame.locals import *

pygame.init()
SCREEN = pygame.display.set_mode((300, 300))
CLOCK = pygame.time.Clock()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
sysfont = pygame.font.SysFont(None, 36)
txt = sysfont.render("", True, BLACK)
n = 0
while True :
    SCREEN.fill(WHITE)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 3:
                n = 0
                txt = sysfont.render(str(n), True, BLACK)
        if event.type == KEYDOWN:
            if event.key == K_UP:
                n = n + 10
                txt = sysfont.render(str(n), True, BLACK)
            if event.key == K_DOWN:
                n = n - 10
                txt = sysfont.render(str(n), True, BLACK)
            if event.key == K_LEFT:
                n = n * 10
                txt = sysfont.render(str(n), True, BLACK)
            if event.key == K_RIGHT:
                n = n / 10
                txt = sysfont.render(str(n), True, BLACK)
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
    SCREEN.blit(txt, (100, 120))
    pygame.display.update()
    CLOCK.tick(60)