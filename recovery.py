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

board = pygame.image.load('guidestar.png')

one_x,one_y = 360,100
two_x,two_y = 530,165
three_x,three_y = 610,330
four_x,four_y = 535,510
five_x,five_y = 360,600
six_x,six_y = 175,510
seven_x,seven_y = 105,330
eight_x,eight_y = 175,155
nine_x,nine_y = 360,330

class Perepere(pygame.sprite.Sprite):
    def __init__(self,image_file,location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

pygame.init()

screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])

title_font = pygame.font.Font(None,50)
title = "Mū Tōrere"

base_font = pygame.font.Font(None,32)

user_text = int()
color = (0,0,0)
input_rect = pygame.Rect(100,700,50,32)

running = True
while running:
    for event in pygame.event.get():
        gp_one = Perepere('green_perepere.png',[one_x,one_y])
        gp_two = Perepere('green_perepere.png', [two_x,two_y])
        gp_three = Perepere('green_perepere.png',[three_x,three_y])
        gp_four = Perepere('green_perepere.png', [four_x,four_y])

        bp_one = Perepere('blue_perepere.png',[five_x,five_y])
        bp_two = Perepere('blue_perepere.png',[six_x,six_y])
        bp_three = Perepere('blue_perepere.png',[seven_x,seven_y])
        bp_four = Perepere('blue_perepere.png',[eight_x,eight_y])

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
                                                        else:    
                                                            if event.key ==  K_ESCAPE:
                                                                running = False
        screen.fill((255,255,255))

        title_surface = title_font.render(title,True,(0,0,0))
        screen.blit(title_surface,(335,50))

        pygame.draw.rect(screen,color,input_rect,2 )
        user_string = str(user_text)
        text_surface = base_font.render(user_string,True,(0,0,0))
        screen.blit(text_surface,(input_rect.x + 10,input_rect.y + 5))

        screen.blit(board,(125,100))

        screen.blit(gp_one.image,gp_one.rect)
        screen.blit(gp_two.image, gp_two.rect)
        screen.blit(gp_three.image, gp_three.rect)
        screen.blit(gp_four.image, gp_four.rect)

        screen.blit(bp_one.image,bp_one.rect)
        screen.blit(bp_two.image,bp_two.rect)
        screen.blit(bp_three.image,bp_three.rect)
        screen.blit(bp_four.image,bp_four.rect)

        pygame.display.flip()

pygame.quit()