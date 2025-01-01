# one player and AI chess in python with Pygame!
# part one, set up variables images and game loop

import pygame
from pygame import MOUSEBUTTONDOWN

pygame.init()
WIDTH = 1000
HEIGHT = 900
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Checkmate Crew Pygame Chess!')
font = pygame.font.Font("assets/fonts/bold_font.ttf", 20)
big_font = pygame.font.Font("assets/fonts/bold_font.ttf", 50)
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
captured_pieces_pink = []
captured_pieces_blue = []
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



# main board
def draw_board():
    for i in range(32):# there are 8*8 = 64 squares on a board, but we can cut the amount in half by using the background as every other square
        column = i % 4
        row = i // 4
        # calculates which row and column to put a square, for example square 11 will be placed on column = 11 % 4 = 3(4, because we have a zero), and row = 11 // 4 = 2(3, because we have a zero)
        if row % 2 != 0:
            pygame.draw.rect(screen, (72,149,191,255), [600 - (column * 200), row * 100, 100, 100])# draws rect
        else:
            pygame.draw.rect(screen, (72,149,191,255), [700 - (column * 200), row * 100, 100, 100])# offsets neven squares by 100
        pygame.draw.rect(screen, (41,80,149,255), [0, 800, WIDTH, 100], 5)# draws outline
        pygame.draw.rect(screen, (41,80,149,255), [800, 0, 200, HEIGHT], 5)# draws outline
        status_text = ['White, pick your piece', 'Where should it go?', 'Black, pick your piece', 'Where should it go?']# all the status texts
        screen.blit(big_font.render(status_text[turn_step], True, (151,71,124,255)), (20, 820))

# Drawing pieces on board
def draw_pieces():
    for i in range(len(white_pieces)): # not making for i in range(16) because the amount of pieces can change
        index = piece_list.index(white_pieces[i]) # we need an index to know which image we can use

        if white_pieces[i] == 'pawn': # we need a separate one for pawns, because they are smaller
            screen.blit(white_pawn, (white_locations[i][0] * 100 + 18, white_locations[i][1] * 100 + 16))# offset to make the pawn sit in the middle of a square
        else:
            screen.blit(white_images[index], (white_locations[i][0] * 100 + 10, white_locations[i][1] * 100 + 10))# the same thing with other pieces, but the all share the same offset
        if turn_step < 2: # outline white selected piece
            if selection == i:
                pygame.draw.rect(screen, (30,28,67,255), [white_locations[i][0] * 100, white_locations[i][1] * 100, 100, 100], 2)

    for i in range(len(black_pieces)):  # not making for i in range(16) because the amount of pieces can change
         index = piece_list.index(black_pieces[i])  # we need an index to know which image we can use

         if black_pieces[i] == 'pawn':  # we need a separate one for pawns, because they are smaller
            screen.blit(black_pawn, (black_locations[i][0] * 100 + 18, black_locations[i][1] * 100 + 16))  # offset to make the pawn sit in the middle of a square
         else:
            screen.blit(black_images[index], (black_locations[i][0] * 100 + 10, black_locations[i][1] * 100 + 10))  # the same thing with other pieces, but the all share the same offset
         if turn_step >= 2:  # outline white selected piece
            if selection == i:
                pygame.draw.rect(screen,(151,71,124,255), [black_locations[i][0] * 100, black_locations[i][1] * 100, 100, 100], 2)




# function to check all pieces valid options on board
def check_options(pieces, locations, turn):
    moves_list = []
    all_moves_list = []
    for i in range((len(pieces))):
        location = locations[i]
        piece = pieces[i]
        if piece == 'pawn':
            moves_list = check_pawn(location, turn)
        elif piece == 'rook':
            moves_list = check_rook(location, turn)
        elif piece == 'knight':
            moves_list = check_knight(location, turn)
        elif piece == 'bishop':
            moves_list = check_bishop(location, turn)
        elif piece == 'queen':
            moves_list = check_queen(location, turn)
        elif piece == 'king':
            moves_list = check_king(location, turn)
        all_moves_list.append(moves_list)
    return all_moves_list

# check bishop moves
def check_bishop(position, color):
    moves_list = []
    if color == 'white':  # user selected white rook that means black - enemies , white - friends
        enemies_list = black_locations
        friends_list = white_locations
    else:  # the same, but user selected black rook
        enemies_list = white_locations
        friends_list = black_locations
    for i in range(4):  # up-right, up-left, down-right, down-left (the possible/valid moves)
        path = True
        chain = 1  # if we find a piece open then the chain of pieces in our path is one, but every time we find another piece to continue on with is open then we will extend that chain value
        if i == 0:  # that would be down
            x = 1 # going right
            y = -1 # going up
        elif i == 1:  # that would be up
            x = -1 # going left
            y = -1
        elif i == 2:  # that would be right
            x = 1
            y = 1 # going down
        else:  # that would be left
            x = -1
            y = 1
        while path:  # you don't have to checking down or up or left or right that line you've hit a wall you've hit a piece you can't move any farther
            # the code below should check if we have an open path going forward
            # also we want to check if we're allowed to move to the right (X = 1) \
            # and change chain starts as a 1, that means that the first position \
            # we check is our current Y position, because Y is equal to zero so \
            # this whole piece becomes equal to zero so this is just checkin our current white position \
            # plus one to the right of our current X position and if that's not in the friends list \
            # and that spot position 0 to the right is between 0 and 7 then we can move there \
            # whether it's empty or there's an enemy there we can move that way

            # we check for any direction we're checking to see if we can continue going in that way \
            # so it's either empty or with an enemy if all this first lines are true, so that means \
            # that we can add it ot the moves list, but if it is an enemy we need to do additional thing and say \
            # then the path is actually false , we can't go any further in that direction
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and \
                    0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append((position[0] + (chain * x), position[1] + (chain * y)))
                # the code below should check if the piece is an enemies list ,if yes , we need to break it
                if (position[0] + (chain * x), position[1] + (chain * y)) not in enemies_list:
                    path = False
                chain += 1

            else:
                path = False

    return moves_list


# check valid pawn moves
def check_pawn(position, color):
    moves_list = [] # List to store possible moves

    # Check moves for a white pawn
    if color == 'white':
        # Move one step forward if the cell is empty and within the board's bounds
        if (position[0], position[1] + 1) not in white_locations and \
                (position[0], position[1] + 1) not in black_locations and position[1] < 7:
            moves_list.append((position[0], position[1] + 1))
        # Move two steps forward if the pawn is on its starting position and both cells are empty
        if (position[0], position[1] + 2) not in white_locations and \
                (position[0], position[1] + 2) not in black_locations and position[1] == 1:
            moves_list.append((position[0], position[1] + 2))
        # Capture an opponent's piece diagonally to the right
        if (position[0] + 1, position[1] + 1) in black_locations:
            moves_list.append((position[0] + 1, position[1] + 1))
        # Capture an opponent's piece diagonally to the left
        if (position[0] - 1, position[1] + 1) in black_locations:
            moves_list.append((position[0] - 1, position[1] + 1))
    # Check moves for a black pawn
    else:
        # Move one step forward if the cell is empty and within the board's bounds
        if (position[0], position[1] - 1) not in white_locations and \
                (position[0], position[1] - 1) not in black_locations and position[1] > 0:
            moves_list.append((position[0], position[1] - 1))
        # Move two steps forward if the pawn is on its starting position
        if (position[0], position[1] - 2) not in white_locations and \
                (position[0], position[1] - 2) not in black_locations and position[1] == 6:
            moves_list.append((position[0], position[1] - 2))
        # Capture an opponent's piece diagonally to the right
        if (position[0] + 1, position[1] - 1) in white_locations:
            moves_list.append((position[0] + 1, position[1] - 1))
          # Capture an opponent's piece diagonally to the left
        if (position[0] - 1, position[1] - 1) in white_locations:
            moves_list.append((position[0] - 1, position[1] - 1))
    # Return the list of possible moves
    return moves_list

# check rook moves
def check_rook(position,color):
    moves_list = []
    if color == 'white': # user selected white rook that means black - enemies , white - friends
        enemies_list = black_locations
        friends_list = white_locations
    else: # the same, but user selected black rook
        enemies_list = white_locations
        friends_list = black_locations
    for i in range(4): # down, up, right, left (the possible/valid moves)
        path = True
        chain = 1 # if we find a piece open then the chain of pieces in our path is one, but every time we find another piece to continue on with is open then we will extend that chain value
        if i == 0: # that would be down
            x = 0
            y = 1
        elif i == 1: # that would be up
            x = 0
            y = -1
        elif i == 2: # that would be right
            x = 1
            y = 0
        else:        # that would be left
            x = -1
            y = 0
        while path: # you don't have to checking down or up or left or right that line you've hit a wall you've hit a piece you can't move any farther
            # the code below should check if we have an open path going forward
            # also we want to check if we're allowed to move to the right (X = 1) \
            # and change chain starts as a 1, that means that the first position \
            # we check is our current Y position, because Y is equal to zero so \
            # this whole piece becomes equal to zero so this is just checkin our current white position \
            # plus one to the right of our current X position and if that's not in the friends list \
            # and that spot position 0 to the right is between 0 and 7 then we can move there \
            # whether it's empty or there's an enemy there we can move that way

            # we check for any direction we're checking to see if we can continue going in that way \
            # so it's either empty or with an enemy if all this first lines are true, so that means \
            # that we can add it ot the moves list, but if it is an enemy we need to do additional thing and say \
            # then the path is actually false , we can't go any further in that direction
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and \
                0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append((position[0] + (chain * x), position[1] + (chain * y)))
            # the code below should check if the piece is an enemies list ,if yes , we need to break it
                if (position[0] + (chain * x), position[1] + (chain * y)) not in enemies_list:
                    path = False
                chain += 1

            else:
                path = False

    return moves_list

# check king valid moves
def check_king(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
    # 8 squares to check for kings, they can go one square any direction
    targets = [(1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1)]
    # where it can go (if first number is with - is left, if the second
    # number is with - is up, and so on)
    for i in range(8): # because there are 8 places where knight can move
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
    return moves_list
  
# main game loop
run = True
while run:
    timer.tick(fps)
    screen.fill((164,208,221,255))
    draw_board()
    draw_pieces()


    # event handling
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
                            black_piece = black_locations.index(click_coords) # check in which black piece we took out
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
                    if turn_step == 2: # to be in the step two means you don't have anything selected now you have to select something
                        turn_step = 3 # also it will help to stay in turn_step 2 if you want to use another piece / change your selection
                    if click_coords in valid_moves and selection != 100: # that means we just click on the square that we are allowed to move that piece
                        black_locations[selection] = click_coords
                        if click_coords in white_locations:
                            white_piece = white_locations.index(click_coords) # check in which white piece we took out
                            captured_pieces_black.append(white_pieces[white_piece])
                            white_pieces.pop(white_piece) # remove white piece from our list of the black player's active pieces
                            white_locations.pop(white_piece) # remove the black piece that we just landed on from our pieces and our locations list and add to captured white pieces
                        black_options = check_options(black_pieces, black_locations, 'black')
                        white_options = check_options(white_pieces, white_locations, 'white')
                        turn_step = 0
                        selection = 100
                        valid_moves = []







    pygame.display.flip()
pygame.quit()

