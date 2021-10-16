import pygame
from pygame.locals import (
    K_ESCAPE,
    QUIT,
    KEYDOWN
)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

x = 50
y = 100

greenPerepereOne = pygame.image.load('piece_one.png')

pygame.init()

screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])

base_font = pygame.font.Font(None,32)
user_text = ''

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            user_text += event.unicode
            if event.key ==  K_ESCAPE:
                running = False
        screen.fill((255,255,255))
        screen.blit(greenPerepereOne, (x,y))
        text_surface = base_font.render(user_text,True,(0,0,0))
        screen.blit(text_surface,(100,100))
        pygame.display.flip()

pygame.quit()