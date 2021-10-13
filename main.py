import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

pygame.init()

screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])

loop = True
running = True
while running:
    for event in pygame.event.get():
        screen.fill((226,226,226))
        pygame.display.flip()

pygame.quit()