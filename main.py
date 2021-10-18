import pygame
from pygame.fastevent import init
from pygame.locals import (
    K_ESCAPE,
    QUIT,
    KEYDOWN,
    MOUSEBUTTONDOWN,

)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800



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

class gameLogic():
    
    def find_where(self):
        global piece_position
        match pos:
            case (one_x,one_y):
                piece_position = 1
                return piece_position
            case (two_x,two_y):
                piece_position = 2
                return piece_position
            case (three_x,three_y):
                piece_position = 3
                return piece_position
            case (four_x,four_y):
                piece_position = 4
                return piece_position
            case (five_x,five_y):
                piece_position = 5
                return piece_position
            case (six_x,six_y):
                piece_position = 6
                return piece_position
            case (seven_x,seven_y):
                piece_position = 7
                return piece_position
            case (eight_x,eight_y):
                piece_position = 8
                return piece_position
    
    def set_position(self):
        gp_one.find_where(gp_one_x,gp_one_y)
        global one_pos
        one_pos = piece_position
            
        gp_two.find_where((gp_two_x,gp_two_y))
        global two_pos
        two_pos = piece_position
                
        gp_three.find_where((gp_three_x,gp_three_y))
        global three_pos
        three_pos = piece_position
                
        gp_four.find_where((gp_four_x,gp_four_y))
        global four_pos
        four_pos = piece_position
            
        bp_one.find_where((bp_one_x,bp_one_y))
        global five_pos
        five_pos = piece_position
                
        bp_two.find_where((bp_two_x,bp_two_y))
        global six_pos
        six_pos = piece_position
                
        bp_three.find_where((bp_three_x,bp_three_y))
        global seven_pos
        seven_pos = piece_position

        bp_four.find_where((bp_four_x,bp_four_y))
        global eight_pos
        eight_pos = piece_position

    def find_available_position(self):
        global total
        global move_request
        total = one_pos+two_pos+three_pos+four_pos+five_pos+six_pos+seven_pos+eight_pos

        if total == 36:
            global available_pos
            available_pos = 9
            
        if total == 37:
            available_pos = 8  

        if total == 38:
            available_pos = 7    

        if total == 39:
            available_pos = 6
            
        if total == 40:
            available_pos = 5
            
        if total == 41:
            available_pos = 4
            
        if total == 42:
            available_pos = 3
            
        if total == 43:
            available_pos = 2
            
        if total == 44:
            available_pos = 1
            
    def start_move(self,start):
        global selected_piece
        if start == 1:                  #the integer values for start represent the piece itself
            selected_piece = one_pos   #this says that the selected piece is the piece at this location   
        elif start == 2:
            selected_piece = two_pos 
        elif start == 3:
            selected_piece = three_pos   
        elif start == 4:
            selected_piece = four_pos
        elif start == 5:
            selected_piece = five_pos     
        elif start == 6:
            selected_piece = six_pos    
        elif start == 7:
            selected_piece = seven_pos 
        elif start == 8:
            selected_piece = eight_pos

class Rules():
    def rule_set():
        match available_pos:
            case 1:
                if selected_piece == 2 or 8 or 9:
                    print('valid 1')
            case 2:
                if selected_piece == 1 or 3 or 9:
                    print('valid 2')
            case 3:
                if selected_piece == 2 or 4 or 9:
                    print('valid 3')
            case 4:
                if selected_piece == 3 or 5 or 9:
                    print('valid 4')
            case 5:
                if selected_piece == 4 or 6 or 9:
                    print('valid 5')
            case 6:
                if selected_piece == 5 or 7 or 9:
                    print('valid 6')
            case 7:
                if selected_piece == 6 or 8 or 9:
                    print('valid 7')
            case 8:
                if selected_piece == 7 or 1 or 9:
                    print('valid 8')

    
pygame.init()

screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])

title_font = pygame.font.Font(None,50)
title = "Mū Tōrere"

base_font = pygame.font.Font(None,32)


running = True
while running:
    for event in pygame.event.get():

        gp_one = Perepere('green_perepere.png',[gp_one_x,gp_one_y])
        gp_two = Perepere('green_perepere.png', [gp_two_x,gp_two_y])
        gp_three = Perepere('green_perepere.png',[gp_three_x,gp_three_y])
        gp_four = Perepere('green_perepere.png', [gp_four_x,gp_four_y])

        bp_one = Perepere('blue_perepere.png',[bp_one_x,bp_one_y])
        bp_two = Perepere('blue_perepere.png',[bp_two_x,bp_two_y])
        bp_three = Perepere('blue_perepere.png',[bp_three_x,bp_three_y])
        bp_four = Perepere('blue_perepere.png',[bp_four_x,bp_four_y])

        logic = gameLogic()

        rules = Rules()

        board = pygame.image.load('guidestar.png')



        if event.type == pygame.MOUSEBUTTONDOWN:
            
            if gp_one.rect.collidepoint(event.pos):
                logic.find_where()
                logic.set_position()
                logic.start_move(1)
                logic.find_available_position()
                rules.rule_set()



            if gp_two.rect.collidepoint(event.pos):
                logic.find_where()
                logic.set_position()
                logic.start_move(2)
                logic.find_available_position()
                rules.rule_set()

           
            if gp_three.rect.collidepoint(event.pos):
                logic.find_where()
                logic.set_position()
                logic.start_move(3)
                logic.find_available_position()
                rules.rule_set()

                
            if gp_four.rect.collidepoint(event.pos):
                logic.find_where()
                logic.set_position()
                logic.start_move(4)
                logic.find_available_position()
                rules.rule_set()


            if bp_one.rect.collidepoint(event.pos):
                logic.find_where()
                logic.set_position()
                logic.start_move(5)
                logic.find_available_position()
                rules.rule_set()
                
            if bp_two.rect.collidepoint(event.pos):
                logic.find_where()
                logic.set_position()
                logic.start_move(6)
                logic.find_available_position()
                rules.rule_set()

                
            if bp_three.rect.collidepoint(event.pos):
                logic.find_where()
                logic.set_position()
                logic.start_move(7)
                logic.find_available_position()
                rules.rule_set()

                
            if bp_four.rect.collidepoint(event.pos):
                logic.find_where()
                logic.set_position()
                logic.start_move(8)
                logic.find_available_position()
                rules.rule_set()

                
        if event.type == pygame.KEYDOWN:
            if event.key ==  K_ESCAPE:
                running = False
        

        screen.fill((255,255,255))

        title_surface = title_font.render(title,True,(0,0,0))
        screen.blit(title_surface,(335,50))

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