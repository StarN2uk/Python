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
rec1 = Rect(100, 300, 100, 60)
rec2 = Rect(400, 300, 100, 60)
count = 0
COLOR1 = WHITE
COLOR2 = BLUE
sysfont = pygame.font.SysFont(None, 36)
sysfont2 = pygame.font.SysFont(None, 60)
u_txt = sysfont.render("O", True, GREEN)
l_txt = sysfont.render("X", True, RED)
c_txt = sysfont.render(str(count), True, WHITE)
while True:
    SCREEN.fill(BLACK)
    cnt += 1
    if cnt >= 60:
        cnt = 0
        i = randint(0, 20)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if i % 2 == 0:
            rec1 = Rect(100, 300, 150, 90)
            pygame.draw.rect(SCREEN, COLOR1, rec1)
        if i % 2 != 0:
            rec2 = Rect(400, 300, 150, 90)
            pygame.draw.rect(SCREEN, COLOR2, rec2)
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if i % 2 == 0:
                    SCREEN.blit(u_txt, (285, 250))
                    rec1 = Rect(100, 300, 100, 60)
                    rec2 = Rect(400, 300, 100, 60)
                    pygame.display.update()
                    CLOCK.tick(100)
                    count += 1
                    c_txt = sysfont.render(str(count), True, WHITE)
                if i % 2 != 0:
                    SCREEN.blit(l_txt, (285, 250))
                    rec1 = Rect(100, 300, 100, 60)
                    rec2 = Rect(400, 300, 100, 60)
                    pygame.display.update()
                    CLOCK.tick(100)
                    count -= 1
                    c_txt = sysfont.render(str(count), True, WHITE)
            if event.button == 3:
                if i % 2 != 0:
                    SCREEN.blit(u_txt, (285, 250))
                    rec1 = Rect(100, 300, 100, 60)
                    rec2 = Rect(400, 300, 100, 60)
                    pygame.display.update()
                    CLOCK.tick(100)
                    count += 1
                    c_txt = sysfont.render(str(count), True, WHITE)
                if i % 2 == 0:
                    SCREEN.blit(l_txt, (285, 250))
                    rec1 = Rect(100, 300, 100, 60)
                    rec2 = Rect(400, 300, 100, 60)
                    pygame.display.update()
                    CLOCK.tick(100)
                    count -= 1
                    c_txt = sysfont.render(str(count), True, WHITE)
    pygame.draw.rect(SCREEN, COLOR1, rec1)
    pygame.draw.rect(SCREEN, COLOR2, rec2)
    SCREEN.blit(c_txt, (10, 10))
    pygame.display.update()
    CLOCK.tick(60)