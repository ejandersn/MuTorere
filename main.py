import pygame
from pygame.fastevent import init
from pygame.locals import (
    K_ESCAPE,
    QUIT,
    KEYDOWN,
    K_BACKSPACE,
    K_RETURN,
    MOUSEBUTTONDOWN,
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



#Position Locations 
one_x,one_y = 360,100
two_x,two_y = 530,165
three_x,three_y = 610,330
four_x,four_y = 535,510
five_x,five_y = 360,600
six_x,six_y = 175,510
seven_x,seven_y = 105,330
eight_x,eight_y = 175,155
nine_x,nine_y = 360,330

#Perepere Locations
gp_one_x,gp_one_y = 360,100
gp_two_x,gp_two_y = 530,165
gp_three_x,gp_three_y = 610,330
gp_four_x,gp_four_y = 535,510
bp_one_x,bp_one_y = 360,600
bp_two_x,bp_two_y = 175,510
bp_three_x,bp_three_y = 105,330
bp_four_x,bp_four_y = 175,155  

pos = int()



class Perepere(pygame.sprite.Sprite):
    
    def __init__(self,image_file,location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
    
    def find_where(self,pos):
        global position
        position = int()
        if pos == ((one_x,one_y)):
            position = 1
            return position
        elif pos == ((two_x,two_y)):
            position = 2
            return position
        elif pos == ((three_x,three_y)):
            position = 3
            return position
        elif pos == ((four_x,four_y)):
            position = 4
            return position
        elif pos == ((five_x,five_y)):
            position = 5
            return position
        elif pos == ((six_x,six_y)):
            position = 6
            return position
        elif pos == ((seven_x,seven_y)):
            position = 7
            return position
        elif pos == ((eight_x,eight_y)):
            position = 8
            return position
        elif pos == ((nine_x, nine_y)):
            position = 9
            return position




class Position(pygame.sprite.Sprite):
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

        pos_one = Position('semitransparrent_position.png',[one_x,one_y])
        pos_two = Position('semitransparrent_position.png',[two_x,two_y])
        pos_three = Position('semitransparrent_position.png',[three_x,three_y])
        pos_four = Position('semitransparrent_position.png',[four_x,four_y])
        pos_five = Position('semitransparrent_position.png',[five_x,five_y])
        pos_six = Position('semitransparrent_position.png', [six_x,six_y])
        pos_seven = Position('semitransparrent_position.png',[seven_x,seven_y])
        pos_eight = Position('semitransparrent_position.png',[eight_x,eight_y])
        pos_nine = Position('semitransparrent_position.png', [nine_x,nine_y])

        gp_one = Perepere('green_perepere.png',[gp_one_x,gp_one_y])
        gp_two = Perepere('green_perepere.png', [gp_two_x,gp_two_y])
        gp_three = Perepere('green_perepere.png',[gp_three_x,gp_three_y])
        gp_four = Perepere('green_perepere.png', [gp_four_x,gp_four_y])

        bp_one = Perepere('blue_perepere.png',[bp_one_x,bp_one_y])
        bp_two = Perepere('blue_perepere.png',[bp_two_x,bp_two_y])
        bp_three = Perepere('blue_perepere.png',[bp_three_x,bp_three_y])
        bp_four = Perepere('blue_perepere.png',[bp_four_x,bp_four_y])

        location = ()
        piece = ()
       
        if event.type == pygame.MOUSEBUTTONDOWN:
            if gp_one.rect.collidepoint(event.pos): 
                move_piece = 1
                gp_one.find_where((gp_one_x,gp_one_y))
                tahi_pos = position
                print(tahi_pos)
                gp_two.find_where((gp_two_x,gp_two_y))
                rua_pos = position
                print(rua_pos)
                gp_three.find_where((gp_three_x,gp_three_y))
                toru_pos = position
                print(toru_pos)
                gp_four.find_where((gp_four_x,gp_four_y))
                wha_pos = position
                print(wha_pos)
                bp_one.find_where((bp_one_x,bp_one_y))
                rima_pos = position
                print(rima_pos)
                bp_two.find_where((bp_two_x,bp_two_y))
                ono_pos = position
                print(ono_pos)
                bp_three.find_where((bp_three_x,bp_three_y))
                whito_pos = position
                print(whito_pos)
                bp_four.find_where((bp_four_x,bp_four_y))
                waru_pos = position
                print(waru_pos)

            if gp_two.rect.collidepoint(event.pos):
                gp_two.find_where((gp_two_x,gp_two_y))
                move_piece = 2
            if gp_three.rect.collidepoint(event.pos):
                gp_three.find_where((gp_three_x,gp_three_y))
                move_piece = 3
            if gp_four.rect.collidepoint(event.pos):
                gp_four.find_where((gp_four_x,gp_four_y))
                move_piece = 4
            if bp_one.rect.collidepoint(event.pos):
                bp_one.find_where((bp_one_x,bp_one_y))
                move_piece = 5
            if bp_two.rect.collidepoint(event.pos):
                bp_two.find_where((bp_two_x,bp_two_y))
                move_piece = 6
            if bp_three.rect.collidepoint(event.pos):
                bp_three.find_where((bp_three_x,bp_three_y))
                move_piece = 7
            if bp_four.rect.collidepoint(event.pos):
                bp_four.find_where((bp_four_x,bp_four_y))
                move_piece = 8
        
        if event.type == pygame.KEYDOWN:
            if event.key ==  K_ESCAPE:
                running = False
        
        # if move_piece 

        screen.fill((255,255,255))

        screen.blit(board,(125,100))

        screen.blit(pos_one.image, pos_one.rect)
        screen.blit(pos_two.image, pos_two.rect)
        screen.blit(pos_three.image, pos_three.rect)
        screen.blit(pos_four.image, pos_four.rect)
        screen.blit(pos_five.image, pos_five.rect)
        screen.blit(pos_six.image, pos_six.rect)
        screen.blit(pos_seven.image, pos_seven.rect)
        screen.blit(pos_eight.image, pos_eight.rect)
        screen.blit(pos_nine.image, pos_nine.rect)

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