import sys
import pygame
from pygame.locals import *
from random import *
pygame.init()
SCREEN = pygame.display.set_mode((600, 600))
CLOCK = pygame.time.Clock()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE =(0, 0, 255)
direc = ('UP', 'DOWN', 'LEFT', 'RIGHT')
i = 0
cnt = 0
rec1 = Rect(250, 200, 100, 60)
rec2 = Rect(250, 400, 100, 60)
rec3 = Rect(100, 300, 100, 60)
rec4 = Rect(400, 300, 100, 60)
COLOR1 = GREEN
COLOR2 = GREEN
COLOR3 = GREEN
COLOR4 = GREEN
sysfont = pygame.font.SysFont(None, 36)
sysfont2 = pygame.font.SysFont(None, 60)
u_txt = sysfont.render("UP", True, WHITE)
d_txt = sysfont.render("DOWN", True, WHITE)
l_txt = sysfont.render("LEFT", True, WHITE)
r_txt = sysfont.render("RIGHT", True, WHITE)
while True:
    SCREEN.fill(WHITE)
    cnt += 1
    if cnt >= 60:
        cnt = 0
        i = randint(0, 3)
    dr_txt = sysfont2.render(direc[i], True, BLACK)
    SCREEN.blit(dr_txt, (250, 100))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_UP:
                if i == 0:
                    COLOR1 = BLUE
                else:
                    COLOR1 = RED
            if event.key == K_DOWN:
                if i == 1:
                    COLOR2 = BLUE
                else:
                    COLOR2 = RED
            if event.key == K_LEFT:
                if i == 2:
                    COLOR3 = BLUE
                else:
                    COLOR3 = RED
            if event.key == K_RIGHT:
                if i == 3:
                    COLOR4 = BLUE
                else:
                    COLOR4 = RED
        if event.type == KEYUP:
            COLOR1, COLOR2, COLOR3, COLOR4 = GREEN, GREEN, GREEN, GREEN
    pygame.draw.rect(SCREEN, COLOR1, rec1)
    pygame.draw.rect(SCREEN, COLOR2, rec2)
    pygame.draw.rect(SCREEN, COLOR3, rec3)
    pygame.draw.rect(SCREEN, COLOR4, rec4)
    SCREEN.blit(u_txt, (285, 220))
    SCREEN.blit(d_txt, (260, 420))
    SCREEN.blit(l_txt, (120, 320))
    SCREEN.blit(r_txt, (410, 320))
    pygame.display.update()
    CLOCK.tick(60)