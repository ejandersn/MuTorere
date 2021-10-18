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
VALID = False
class Perepere(pygame.sprite.Sprite):
    
    def __init__(self,image_file,location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        global type
        type = image_file
    
    def find_where(self,pos): #This finds where perepere are at
            global position
            position = int()

            if pos == (one_x,one_y):
                position = 1
                return position
            elif pos == (two_x,two_y):
                position = 2
                return position
            elif pos == (three_x,three_y):
                position = 3
                return position
            elif pos == (four_x,four_y):
                position = 4
                return position
            elif pos == (five_x,five_y):
                position = 5
                return position
            elif pos == (six_x,six_y):
                position = 6
                return position
            elif pos == (seven_x,seven_y):
                position = 7
                return position
            elif pos == (eight_x,eight_y):
                position = 8
                return position
            elif pos == (nine_x, nine_y):
                position = 9
                return position
class game_logic():
    def find_all(self):     #This shows the specfic location in corralation with its respective piecessss  
            gp_one.find_where((gp_one_x,gp_one_y))
            tahi_type = 1
            global one_pos
            one_pos = position
           
            gp_two.find_where((gp_two_x,gp_two_y))
            rua_type = 1
            global two_pos
            two_pos = position
            
            gp_three.find_where((gp_three_x,gp_three_y))
            toru_type = 1
            global three_pos
            three_pos = position
            
            gp_four.find_where((gp_four_x,gp_four_y))
            wha_type = 1
            global four_pos
            four_pos = position
           
            bp_one.find_where((bp_one_x,bp_one_y))
            ima_type = 2
            global five_pos
            five_pos = position
            
            bp_two.find_where((bp_two_x,bp_two_y))
            ono_type = 2
            global six_pos
            six_pos = position
            
            bp_three.find_where((bp_three_x,bp_three_y))
            whitu_type = 2
            global seven_pos
            seven_pos = position
            bp_four.find_where((bp_four_x,bp_four_y))
            whitu_type = 2
            global eight_pos
            eight_pos = position

            logic.find_available_position()


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

    def find_available_position(self):
        global total
        
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
            


    def check_neighbor(self):
        print(available_pos, 'first')
        if selected_piece != 8:
            if selected_piece != 1:
                if selected_piece == one_pos:
                        print(selected_piece)
                        if one_pos-1 == two_pos or one_pos-1 == three_pos or one_pos-1 ==four_pos:
                            if one_pos+1 == two_pos or one_pos+1 == three_pos or one_pos+1 == four_pos:
                                print('invalid')
                if selected_piece == two_pos:
                        print(selected_piece)
                        if two_pos-1 == one_pos or two_pos-1 == three_pos or two_pos-1 == four_pos:
                            if two_pos+1 == one_pos or two_pos+1 == three_pos or  two_pos+1 == four_pos:
                                print('invalid')
                if selected_piece == three_pos:
                    print(selected_piece)
                    if three_pos-1 == one_pos or three_pos-1 == two_pos or three_pos-1 == four_pos:
                        if three_pos+1 == one_pos or three_pos+1 == two_pos or three_pos+1 == four_pos:
                            print('invalid')
                if selected_piece == four_pos:
                    print(selected_piece)
                    if four_pos-1 == one_pos or four_pos-1 == two_pos or four_pos-1 == three_pos:
                        if three_pos+1 == one_pos or three_pos+1 == two_pos or three_pos+1 == three_pos:
                            print('invalid')
                if selected_piece == five_pos:
                    print(selected_piece)
                    if five_pos-1 == six_pos or five_pos-1 == seven_pos or five_pos-1 == eight_pos:
                        if five_pos+1 == six_pos or five_pos+1 == seven_pos or five_pos+1 == eight_pos:
                            print('invalid')
                if selected_piece == six_pos:
                    print(selected_piece)
                    if six_pos-1 == five_pos or six_pos-1 == seven_pos or six_pos-1 == eight_pos:
                        if six_pos+1 == five_pos or six_pos+1 == seven_pos or six_pos+1 == eight_pos:
                            print('invalid')
                if selected_piece == seven_pos:
                    print (selected_piece)
                    if seven_pos-1 == five_pos or seven_pos-1 == six_pos or seven_pos-1 == eight_pos:
                        if seven_pos+1 == five_pos or seven_pos+1 == six_pos or seven_pos+1 == eight_pos:
                            print('invalid')
                if selected_piece == eight_pos:
                    print(selected_piece)
                    if eight_pos-1 == five_pos or eight_pos-1 == six_pos or eight_pos-1 == seven_pos:
                        if eight_pos+1 == five_pos or eight_pos+1 == six_pos or eight_pos+1 == seven_pos:
                            print('invalid')
            else: 
                if selected_piece == one_pos:
                    print(selected_piece)
                    if two_pos == 8 or three_pos == 8 or four_pos == 8:
                        if two_pos == 2 or three_pos == 2 or four_pos == 2:
                            print('invalid')
                if selected_piece == two_pos:
                    print(selected_piece)
                    if one_pos == 8 or three_pos == 8 or four_pos == 8:
                        if one_pos == 2 or three_pos == 2 or four_pos == 2:
                            print('invalid')
                if selected_piece == three_pos:
                    print(selected_piece)
                    if one_pos == 8 or two_pos ==  8 or four_pos == 8:
                        if one_pos == 2 or two_pos == 8 or four_pos == 8:
                                print('invalid')
                if selected_piece == four_pos:
                    print(selected_piece)
                    if one_pos == 8 or two_pos == 8 or three_pos == 8:
                        if one_pos == 2 or two_pos == 2 or three_pos == 2:
                            print('invalid')
                if selected_piece == five_pos:
                    print (selected_piece)
                    if six_pos == 8 or seven_pos == 8 or eight_pos == 8:
                        if six_pos == 2 or seven_pos == 2 or eight_pos == 2:
                            print('invalid')
                if selected_piece == six_pos:
                    print(selected_piece)
                    if five_pos == 8 or seven_pos == 8 or eight_pos == 8:
                        if five_pos == 2 or seven_pos == 2 or eight_pos == 2:
                            print('invalid')
                if selected_piece == seven_pos:
                    print(selected_piece)
                    if five_pos == 8 or six_pos == 8 or eight_pos == 8:
                        if five_pos == 2 or six_pos == 2 or eight_pos == 2:
                            print('invalid')
                if selected_piece == eight_pos:
                    print(selected_piece)
                    if five_pos == 8 or six_pos == 8 or seven_pos == 8:
                        if five_pos == 2 or six_pos == 2 or seven_pos == 2:
                            print('invalid')

        else:
            if selected_piece == one_pos:
                print(selected_piece)
                if two_pos == 7 or three_pos == 7 or four_pos == 7:
                    if two_pos == 1 or three_pos == 1 or four_pos == 1:
                        print('invalid')
            if selected_piece == two_pos:
                print(selected_piece)
                if one_pos == 7 or three_pos == 7 or four_pos == 7:
                    if one_pos == 1 or three_pos == 1 or four_pos == 1:
                        print('invalid')
            if selected_piece == three_pos:
                print(selected_piece)
                if one_pos == 7 or two_pos ==  7 or four_pos == 7:
                    if one_pos == 1 or two_pos == 1 or four_pos == 1:
                            print('invalid')
            if selected_piece == four_pos:
                print(selected_piece)
                if one_pos == 7 or two_pos == 7 or three_pos == 7:
                    if one_pos == 1 or two_pos == 1 or three_pos == 1:
                        print('invalid')
            if selected_piece == five_pos:
                print (selected_piece)
                if six_pos == 7 or seven_pos == 7 or eight_pos == 7:
                    if six_pos == 1 or seven_pos == 1 or eight_pos == 1:
                        print('invalid')
            if selected_piece == six_pos:
                print(selected_piece)
                if five_pos == 7 or seven_pos == 7 or eight_pos == 7:
                    if five_pos == 1 or seven_pos == 7 or eight_pos == 1:
                        print('invalid')
            if selected_piece == seven_pos:
                print(selected_piece)
                if five_pos == 7 or six_pos == 7 or eight_pos == 7:
                    if five_pos == 1 or six_pos == 1 or eight_pos == 1:
                        print('invalid')
            if selected_piece == eight_pos:
                print(selected_piece)
                if five_pos == 7 or six_pos == 7 or seven_pos == 7:
                    if five_pos == 1 or six_pos == 1 or seven_pos == 1:
                        print('invalid')
            
        global move_to
        move_to = ()                
        # match available_pos:
        #     case 9:
        #         print(selected_piece)
        #         if selected_piece == 2 or 8:
        #             global move_to
        #             move_to = (nine_x, nine_y)
        #             print('valid')






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

        gp_one = Perepere('green_perepere.png',[gp_one_x,gp_one_y])
        gp_two = Perepere('green_perepere.png', [gp_two_x,gp_two_y])
        gp_three = Perepere('green_perepere.png',[gp_three_x,gp_three_y])
        gp_four = Perepere('green_perepere.png', [gp_four_x,gp_four_y])
        bp_one = Perepere('blue_perepere.png',[bp_one_x,bp_one_y])
        bp_two = Perepere('blue_perepere.png',[bp_two_x,bp_two_y])
        bp_three = Perepere('blue_perepere.png',[bp_three_x,bp_three_y])
        bp_four = Perepere('blue_perepere.png',[bp_four_x,bp_four_y])

        location = game_logic()
        move_piece = game_logic()
        logic = game_logic()
        if event.type == pygame.MOUSEBUTTONDOWN:

            if gp_one.rect.collidepoint(event.pos): 
                location.find_all() #we have to constantly know where all pieces are otherwise we do not know where to go
                move_piece.start_move(1)
                logic.check_neighbor()
                
                logic.find_available_position()
                # gp_one_x,gp_one_y = move_to

            if gp_two.rect.collidepoint(event.pos):
                location.find_all()
                move_piece.start_move(2)
                logic.check_neighbor()
                
                logic.find_available_position()
                # gp_two_x,gp_two_y = move_to

            if gp_three.rect.collidepoint(event.pos):
                location.find_all()
                move_piece.start_move(3)
                logic.check_neighbor()
                
                logic.find_available_position()
                # gp_three_x,gp_three_y = move_to

            if gp_four.rect.collidepoint(event.pos):
                location.find_all()
                move_piece.start_move(4)
                logic.check_neighbor()
                
                logic.find_available_position()
                # gp_four_x,gp_four_y = move_to

            if bp_one.rect.collidepoint(event.pos):
                location.find_all()
                move_piece.start_move(5)
                logic.check_neighbor()
                
                logic.find_available_position()
                # bp_one_x,bp_one_y = move_to

            if bp_two.rect.collidepoint(event.pos):
                location.find_all()
                move_piece.start_move(6)
                logic.check_neighbor()
                
                logic.find_available_position()
                # bp_two_x,bp_two_y = move_to

            if bp_three.rect.collidepoint(event.pos):
                location.find_all()
                move_piece.start_move(7)
                logic.check_neighbor()
                
                logic.find_available_position()
                # bp_three_x, bp_three_y = move_to

            if bp_four.rect.collidepoint(event.pos):
                location.find_all()
                move_piece.start_move(8)
                
                logic.check_neighbor()
                
                logic.find_available_position()
                # bp_four_x, bp_four_y = move_to

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