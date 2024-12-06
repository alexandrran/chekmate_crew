# one player and AI chess in python with Pygame!
# part one, set up variables images and game loop

import pygame
from pygame import MOUSEBUTTONDOWN

pygame.init()
WIDTH = 1000
HEIGHT = 900
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Checkmate Crew Pygame Chess!')
font = pygame.font.Font('freesansbold.ttf', 20)
big_font = pygame.font.Font('freesansbold.ttf', 50)
timer = pygame.time.Clock()
fps = 60
# game variables and images
white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                  (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                  (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
captured_pieces_white = []
captured_pieces_black = []
# 0 - whites turn, no selections: 1-whites turn, piece selected: 2- black turn no selection, 3 - black turn piece selected
turn_step = 0
selection = 100
valid_moves = []
# load in game piece images (queen, king, rook, bishop, knight, pawn) x 2
black_queen = pygame.image.load('assets/images/black queen.png')
black_queen = pygame.transform.scale(black_queen, (80, 80))
black_queen_small = pygame.transform.scale(black_queen, (45, 45))
black_king = pygame.image.load('assets/images/black king.png')
black_king = pygame.transform.scale(black_king, (80, 80))
black_king_small = pygame.transform.scale(black_king, (45, 45))
black_rook = pygame.image.load('assets/images/black rook.png')
black_rook = pygame.transform.scale(black_rook, (80, 80))
black_rook_small = pygame.transform.scale(black_rook, (45, 45))
black_bishop = pygame.image.load('assets/images/black bishop.png')
black_bishop = pygame.transform.scale(black_bishop, (80, 80))
black_bishop_small = pygame.transform.scale(black_bishop, (45, 45))
black_knight = pygame.image.load('assets/images/black knight.png')
black_knight = pygame.transform.scale(black_knight, (80, 80))
black_knight_small = pygame.transform.scale(black_knight, (45, 45))
black_pawn = pygame.image.load('assets/images/black pawn.png')
black_pawn = pygame.transform.scale(black_pawn, (65, 65))
black_pawn_small = pygame.transform.scale(black_pawn, (45, 45))
white_queen = pygame.image.load('assets/images/white queen.png')
white_queen = pygame.transform.scale(white_queen, (80, 80))
white_queen_small = pygame.transform.scale(white_queen, (45, 45))
white_king = pygame.image.load('assets/images/white king.png')
white_king = pygame.transform.scale(white_king, (80, 80))
white_king_small = pygame.transform.scale(white_king, (45, 45))
white_rook = pygame.image.load('assets/images/white rook.png')
white_rook = pygame.transform.scale(white_rook, (80, 80))
white_rook_small = pygame.transform.scale(white_rook, (45, 45))
white_bishop = pygame.image.load('assets/images/white bishop.png')
white_bishop = pygame.transform.scale(white_bishop, (80, 80))
white_bishop_small = pygame.transform.scale(white_bishop, (45, 45))
white_knight = pygame.image.load('assets/images/white knight.png')
white_knight = pygame.transform.scale(white_knight, (80, 80))
white_knight_small = pygame.transform.scale(white_knight, (45, 45))
white_pawn = pygame.image.load('assets/images/white pawn.png')
white_pawn = pygame.transform.scale(white_pawn, (65, 65))
white_pawn_small = pygame.transform.scale(white_pawn, (45, 45))
white_images = [white_pawn, white_queen, white_king, white_knight, white_rook, white_bishop]
small_white_images = [white_pawn_small, white_queen_small, white_king_small, white_knight_small,
                      white_rook_small, white_bishop_small]
black_images = [black_pawn, black_queen, black_king, black_knight, black_rook, black_bishop]
small_black_images = [black_pawn_small, black_queen_small, black_king_small, black_knight_small,
                      black_rook_small, black_bishop_small]
piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']
# check variables/ flashing counter

# function to check all pieces valid options on board
def check_options():
    pass

# main game loop
run = True
while run:
    timer.tick(fps)
    screen.fill('dark gray')


    # event gandling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # checking if user uses left mouse button
        if event.type == pygame.MOUSEBUTTONDOWN and event.buttom == 1:
            x_coord = event.pos[0] // 100 # define x coordinate of the mouse click
            y_coord = event.pos[0] // 100 # define y coordinate of the mouse click
            click_coords = (x_coord, y_coord)
            # variation based on white of black pieces
            if turn_step <= 1:
                if click_coords in white_locations: # if we click on the white piece
                    selection = white_locations.index(click_coords)
                    if turn_step == 0: # to be in the step zero means you don't have anything selected now you have to select something
                        turn_step = 1 # also it will help to stay in turn_step 1 if you want to use another piece / change your selection
                    if click_coords in valid_moves and selection != 100: # that means we just click on the square that we are allowed to move that piece
                        white_locations[selection] = click_coords
                        if click_coords in black_locations:
                            black_piece = black_locations.index(click_coords) # checkin which black piece we took out
                            captured_pieces_white.append(black_pieces[black_piece])
                            black_pieces.pop(black_piece) # remove black piece from our list of the black player's active pieces
                            black_locations.pop(black_piece) # remove the white piece that we just landed on from our pieces and our locations list and add to captured white pieces
                        black_options = check_options(black_pieces, black_locations, 'black')
                        white_options = check_options(white_pieces, white_locations, 'white')
                        turn_step = 2
                        selection = 100
                        valid_moves = []


            if turn_step > 1:
                if click_coords in black_locations: # if we click on the black piece
                    selection = black_locations.index(click_coords)
                    if turn_step == 2: # to be in the step zero means you don't have anything selected now you have to select something
                        turn_step = 3 # also it will help to stay in turn_step 1 if you want to use another piece / change your selection
                    if click_coords in valid_moves and selection != 100: # that means we just click on the square that we are allowed to move that piece
                        black_locations[selection] = click_coords
                        if click_coords in white_locations:
                            white_piece = white_locations.index(click_coords) # checkin which white piece we took out
                            captured_pieces_black.append(white_pieces[white_piece])
                            white_pieces.pop(white_piece) # remove white piece from our list of the black player's active pieces
                            white_locations.pop(white_piece) # remove the black piece that we just landed on from our pieces and our locations list and add to captured white pieces
                        black_options = check_options(black_pieces, black_locations, 'black')
                        white_options = check_options(white_pieces, white_locations, 'white')
                        turn_step = 2
                        selection = 100
                        valid_moves = []







    pygame.display.flip()
pygame.quit()

