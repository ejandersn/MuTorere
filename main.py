import pygame
import pygame.gfxdraw
from pygame.locals import (
    K_ESCAPE,
    QUIT,
    KEYDOWN
)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
x = 50
y = 100
# x,y = 50,100

sprite = pygame.image.load('piece_one.png')

pygame.init()

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

loop = True
running = True
while running:
    for event in pygame.event.get():
        ev = pygame.event.get()
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            print (pos)
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
    screen.fill((226, 223, 232))
    screen.blit(sprite, (x,y))
    pygame.display.flip()
  
pygame.quit()