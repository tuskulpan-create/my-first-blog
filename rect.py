import sys
from random import randint

import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))
rect = pygame.Rect(40, 40, 80, 80)
color = (255, 0, 0)
clock=pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # if event.type == pygame.KEYDOWN:
        #     color = (255, 255, 255)
    # color = (randint(100,255), randint(10,255), 255)
    pygame.draw.rect(screen, color, rect, 0)
    pygame.display.flip()
    clock.tick(20)