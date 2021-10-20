import pygame
from pygame.display import set_allow_screensaver
from pygame.fastevent import init
from pygame.locals import (
    K_ESCAPE,
    QUIT,
    KEYDOWN,
    MOUSEBUTTONDOWN,
    WINDOWCLOSE
)

class Mutorere:
    def __init__(self):
        print("place holder")

    def start(self):
        pygame.init()
        running = True
        while running:
            for event in pygame.event.get():
                if(event.type == WINDOWCLOSE or (event.type == KEYDOWN and event.key == K_ESCAPE)):
                    running = False
            screen = pygame.display.set_mode([800,800])
            screen.fill((255,255,255))
            pygame.display.flip()
        pygame.quit()  