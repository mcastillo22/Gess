import pygame, sys
from pygame.locals import  * 

from constants import *
from setup import *
from functions import *
from GessGame import *


def main():
    pygame.init()
    clock = pygame.time.Clock()
    SCREEN = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption('Gess Game')

    new_game = GessGame()
    pos1, pos2 = None, None
    topx, topy = 0, 0
    highlight = False

    running = True

    while running:        
        gameboard = new_game.get_board()
        player = new_game.get_player()
        setup_board(SCREEN, player)

        if highlight:
            highlight_piece(SCREEN, topx, topy)

        load_icons(SCREEN, gameboard)

        if new_game.get_game_state() != 'UNFINISHED':
            show_winner(SCREEN, player)

        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_x, mouse_y = event.pos

                    topx, topy = on_grid(mouse_x, mouse_y)
                    in_board = topx is not None and topy is not None

                    if pos1 is None and in_board:
                        pos1 = convert(topx, topy)
                        highlight = new_game.correct_turn(pos1)

                    elif pos1 is not None:
                        pos2 = convert(topx, topy)
                        new_game.make_move(pos1, pos2)
                        highlight = False
                        pos1, pos2 = None, None

        pygame.display.update()
    
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
