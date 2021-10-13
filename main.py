import pygame
from pygame.locals import (
    K_ESCAPE,
    QUIT,
    KEYDOWN
)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

pygame.init()

screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])

loop = True
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        screen.fill((226,226,226))
        pygame.display.flip()

pygame.quit()