import pygame, sys
from pygame.locals import  *
from constants import *
from GessGame import GessGame

def on_grid(x, y):
    """Checks that mouse has been clicked on an actual grid space on the gameboard"""
    for top_x in range(X1, (ARRAY+1)*SPACE, SPACE):
        for top_y in range(X1, (ARRAY+1)*SPACE, SPACE):
            box = pygame.Rect(top_x, top_y, SPACE, SPACE)
            if box.collidepoint(x, y):
                return [top_x, top_y]
    
    return [None, None]

def convert(x, y):
    return BOARD_ARRAY.index(y), BOARD_ARRAY.index(x)

def highlight_piece(screen, x, y):
    piece = pygame.Surface((PIECE-1, PIECE-1))
    piece.set_alpha(96)
    piece.fill(HL)
    screen.blit(piece, (x - SPACE+1, y - SPACE+1))

def not_none(pos):
    if pos is not None:
        return True
    return False

def start_new_game():
    return GessGame()

def check_new_game(x, y):
    """Checks if new game button was clicked"""
    button = pygame.Rect(NEW_GAME_X, TURN_HEIGHT, BUTTON_SIZE, BUTTON_SIZE)
    if button.collidepoint(x, y):
        return True

