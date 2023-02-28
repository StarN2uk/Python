import sys
import pygame
from pygame.locals import *
import random
pygame.init()
SCREEN = pygame.display.set_mode((600, 600))
CLOCK = pygame.time.Clock()
sysfont = pygame.font.SysFont(None, 72)
light_img = pygame.image.load("img.png")
l_size = light_img.get_size()
man_img = pygame.image.load("img1.png")
m_size = man_img.get_size()
m_x, m_y = 250, 480
l_x = []
l_y = []
cnt = 0
score = 0
game_over = False
while True:
    if game_over:
        break
    SCREEN.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    cnt += 1
    if cnt>= 20:
        cnt = 0
        l_x.append(random.randint(0, 600))
        l_y.append(0)
    for i in range(len(l_x)):
        l_y[i] += 5
        SCREEN.blit(light_img, (l_x[i], l_y[i]))
        if l_y[i] >= 550:
            l_x.remove(l_x[i])
            l_y.remove(l_y[i])
            score += 1
            break
    key_event = pygame.key.get_pressed()
    if key_event[pygame.K_LEFT]:
        if m_x > 0:
            m_x -= 5
    if key_event[pygame.K_RIGHT]:
        if m_x < 500:
            m_x += 5
    SCREEN.blit(man_img, (m_x, m_y))
    for i in range(len(l_x)):
        if l_x[i] + l_size[0] >= m_x and m_x + m_size[0] >= l_x[i]:
            if l_y[i] - l_size[1] >= m_y:
                msg = sysfont.render("GG -> score: %d" % score, True, (255, 0, 0))
                SCREEN.blit(msg, (160, 250))
                game_over = True
    pygame.display.update()
    CLOCK.tick(60)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()