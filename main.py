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
INVALID = False
VALID = True

class Perepere(pygame.sprite.Sprite):
    
    def __init__(self,image_file,location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        global type
        type = image_file

    def which_player(self):
        global player
        player = ()
        if type == 'green_perepere.png':
            player = 'green'
            print(player) 
        else:
            player == 'blue'
            print(player)
    
    def find_where(self,pos): #This finds where perepere are at
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
            elif pos == (nine_x, nine_y):
                position = 9
                return position

class game_logic():

    def find_all(self):     #This shows the specfic location in corralation with its respective piecessss  
            gp_one.find_where((gp_one_x,gp_one_y))
            gp_one.which_player() 
            if player == 'green':
                tahi_type = 'green'
            else:
                tahi_type = 'blue'
            global tahi_pos
            tahi_pos = position
            print(tahi_pos)                             #all prints are tests
           
            gp_two.find_where((gp_two_x,gp_two_y))
            gp_two.which_player()
            if player == 'green':
                rua_type = 'green'
            else:
                rua_type = 'blue'
            global rua_pos
            rua_pos = position
            print(rua_pos)
            
            gp_three.find_where((gp_three_x,gp_three_y))
            gp_three.which_player()
            if player == 'green':
                toru_type = 'green'
            else:
                toru_type ='blue'
            global toru_pos
            toru_pos = position
            print(toru_pos)

            gp_four.find_where((gp_four_x,gp_four_y))
            gp_four.which_player()
            if player == 'green':
                wha_type = 'green'
            else:
                wha_type ='blue'
            global wha_pos
            wha_pos = position
            print(wha_pos)

            bp_one.find_where((bp_one_x,bp_one_y))
            bp_one.which_player()
            if player == 'green':
                rima_type = 'green'
            else:
                rima_type ='blue'
            global rima_pos
            rima_pos = position
            print(rima_pos)

            bp_two.find_where((bp_two_x,bp_two_y))
            bp_two.which_player()
            if player == 'green':
                ono = 'green'
            else:
                ono_type ='blue'
            global ono_pos
            ono_pos = position
            print(ono_pos)
            
            bp_three.find_where((bp_three_x,bp_three_y))
            bp_three.which_player()
            if player == 'green':
                whitu_type = 'green'
            else:
                whitu_type ='blue'
            global whito_pos
            whito_pos = position
            print(whito_pos)

            bp_four.find_where((bp_four_x,bp_four_y))
            bp_four.which_player()
            if player == 'green':
                whitu_type = 'green'
            else:
                whitu_type ='blue'
            global waru_pos
            waru_pos = position
            print(waru_pos)
    
    def start_move(self,start):
        global selected_piece
        if start == 1:                  #the integer values for start represent the piece itself
            selected_piece = tahi_pos   #this says that the selected piece is the piece at this location
        elif start == 2:
            selected_piece = rua_pos
        elif start == 3:
            selected_piece = toru_pos
        elif start == 4:
            selected_piece = wha_pos
        elif start == 5:
            selected_piece = rima_pos
        elif start == 6:
            selected_piece = ono_pos
        elif start == 7:
            selected_piece = whito_pos
        elif start == 8:
            selected_piece = waru_pos

    def find_available_position(self):
        global total
        total = tahi_pos+rua_pos+toru_pos+wha_pos+rima_pos+ono_pos+whito_pos+waru_pos
        global move_to
        print(total)
        
        if total == 36:
            global available_pos
            available_pos = 9
            move_to = nine_x,nine_y

        if total == 37:
            available_pos = 8
            move_to = ((eight_x,eight_y))

        if total == 38:
            available_pos = 7
            move_to = ((seven_x,seven_y))

        if total == 39:
            available_pos = 6
            move_to = ((six_x,six_y))

        if total == 40:
            available_pos = 5
            move_to = ((five_x,five_y))

        if total == 41:
            available_pos = 4
            move_to = ((four_x,four_y))

        if total == 42:
            available_pos = 3
            move_to = ((three_x,three_y))

        if total == 43:
            available_pos = 2
            move_to = ((two_x,two_y))

        if total == 44:
            available_pos = 1
            move_to = ((one_x,one_y))


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

        pos_one = Position('transparrent_position.png',[one_x,one_y])
        pos_two = Position('transparrent_position.png',[two_x,two_y])
        pos_three = Position('transparrent_position.png',[three_x,three_y])
        pos_four = Position('transparrent_position.png',[four_x,four_y])
        pos_five = Position('transparrent_position.png',[five_x,five_y])
        pos_six = Position('transparrent_position.png', [six_x,six_y])
        pos_seven = Position('transparrent_position.png',[seven_x,seven_y])
        pos_eight = Position('transparrent_position.png',[eight_x,eight_y])
        pos_nine = Position('transparrent_position.png', [nine_x,nine_y])

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
                print(selected_piece) #this is a test
                logic.find_available_position()
                gp_one_x,gp_one_y = move_to

            if gp_two.rect.collidepoint(event.pos):
                location.find_all()
                move_piece.start_move(2)
                print(selected_piece)
                logic.find_available_position()
                gp_two_x,gp_two_y = move_to

           
            if gp_three.rect.collidepoint(event.pos):
                location.find_all()
                move_piece.start_move(3)
                print(selected_piece)
                logic.find_available_position()
                gp_three_x,gp_three_y = move_to
                
            if gp_four.rect.collidepoint(event.pos):
                location.find_all()
                move_piece.start_move(4)
                print(selected_piece)
                logic.find_available_position()
                gp_four_x,gp_four_y = move_to

            if bp_one.rect.collidepoint(event.pos):
                location.find_all()
                move_piece.start_move(5)
                print(selected_piece)
                logic.find_available_position()
                bp_one_x,bp_one_y = move_to
                
            if bp_two.rect.collidepoint(event.pos):
                location.find_all()
                move_piece.start_move(6)
                print(selected_piece)
                logic.find_available_position()
                bp_two_x,bp_two_y = move_to
                
            if bp_three.rect.collidepoint(event.pos):
                location.find_all()
                move_piece.start_move(7)
                print(selected_piece)
                logic.find_available_position()
                bp_three_x, bp_three_y = move_to
                
            if bp_four.rect.collidepoint(event.pos):
                location.find_all()
                move_piece.start_move(8)
                print(selected_piece)
                logic.find_available_position()
                bp_four_x, bp_four_y = move_to
                
        
        if event.type == pygame.KEYDOWN:
            if event.key ==  K_ESCAPE:
                running = False
        

        screen.fill((255,255,255))

        title_surface = title_font.render(title,True,(0,0,0))
        screen.blit(title_surface,(335,50))

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