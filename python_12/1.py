import sys
import pygame
from pygame.locals import *
pygame.init()
SCREEN = pygame.display.set_mode((200, 200))
CLOCK = pygame.time.Clock()
img = pygame.image.load("img.png")
img_size = img.get_size()
print(img_size)
while True :
    SCREEN.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    SCREEN.blit(img, (25, 40))
    pygame.display.update()
    CLOCK.tick(1)