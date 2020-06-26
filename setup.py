import pygame
from constants import *


def setup_board(screen, player):
    screen_bg(screen)
    draw_grid(screen)
    board_bg(screen)
    show_turn(screen, player)

def load_image(image):
    return pygame.image.load(f'Images/{image}')

def blit_image(screen, img, pos):
    screen.blit(img, pos)

def screen_bg(screen):    
    background = load_image('bg.jpg')
    blit_image(screen, background, (0, 0))

def load_icons(screen, gameboard):
    blue = load_image('dblue.png')
    green = load_image('green.png')
    for row in range(ARRAY - 1):
        for col in range(ARRAY - 1):
            if gameboard[row][col] == 'B':
                blit_image(screen, blue, (PIECE_POS + col*SPACE, PIECE_POS + row*SPACE))
            if gameboard[row][col] == 'W':
                blit_image(screen, green, (PIECE_POS + col*SPACE, PIECE_POS + row*SPACE))

def board_bg(screen):
    bg = pygame.Surface((ARRAY*SPACE+1, ARRAY*SPACE+1))
    bg.set_alpha(64)
    bg.fill(WHITE)
    screen.blit(bg, (X1, Y1))

def draw_grid(screen):
    for n in range(Y1, (ARRAY + 2) * SPACE, SPACE):
        pygame.draw.line(screen, SLEET, (X1, n), (X1 + SPACE * ARRAY, n), 1)
        pygame.draw.line(screen, SLEET, (n, Y1), (n, (Y1 + SPACE * ARRAY)), 1)

def show_turn(screen, player):
    blue = load_image('dblue.png')
    green = load_image('green.png')
    turn = load_image('turn.png')
    blit_image(screen, turn, (TURN_SPACE, int(SPACE//2)))
    if player == 'BLACK':
        blit_image(screen, blue, (TURN_SPACE + 75, TURN_HEIGHT))
    else:
        blit_image(screen, green, (TURN_SPACE + 75, TURN_HEIGHT))

def show_winner(screen, player):
    if player == 'BLACK':
        winner = load_image('db_wins.png')
    else:
        winner = load_image('gr_wins.png')
    blit_image(screen, winner, (WINNER, WINNER))
