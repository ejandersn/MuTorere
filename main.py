import pygame
from pygame.locals import (
    K_ESCAPE,
    QUIT,
    KEYDOWN,
    K_BACKSPACE,
    K_RETURN,
    K_0,
    K_1,
    K_2,
    K_3,
    K_4,
    K_5,
    K_6,
    K_7,
    K_8,
    K_9

)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

x = 370
y = 100



board = pygame.image.load('betterstar.png')
greenPerepereOne = pygame.image.load('piece_one.png')

pygame.init()

screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])

base_font = pygame.font.Font(None,32)
user_text = int()
input_rect = pygame.Rect(100,700,50,32)
color = (0,0,0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if user_text > 9:
                        print('ERROR!')
                else:
                    if event.key == pygame.K_0:
                        user_text = (0)
                    else:
                        if event.key == K_1:
                            user_text = (1)
                        else: 
                            if event.key == K_2:
                                user_text = (2)
                            else:
                                if event.key == K_3:
                                    user_text = (3)
                                else:
                                    if event.key == K_4:
                                        user_text = (4)
                                    else:
                                        if event.key == K_5:
                                            user_text = (5)
                                        else:
                                            if event.key == K_6:
                                                user_text = (6)
                                            else:
                                                if event.key == K_7:
                                                    user_text = (7)
                                                else:
                                                    if event.key == K_8:
                                                        user_text = (8)
                                                    else:
                                                        if event.key == K_9:
                                                            user_text = (9)
                                                            
        if event.key ==  K_ESCAPE:
            running = False
        screen.fill((255,255,255))
        
        pygame.draw.rect(screen,color,input_rect,2 )
        user_string = str(user_text)
        screen.blit(board,(125,100))
        screen.blit(greenPerepereOne, (x,y))
        text_surface = base_font.render(user_string,True,(0,0,0))
        screen.blit(text_surface,(input_rect.x + 10,input_rect.y + 5))
        pygame.display.flip()

pygame.quit()