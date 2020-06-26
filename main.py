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
    pygame.display.set_caption(TITLE)

    new_game = start_new_game()
    pos1, pos2, pos3 = None, None, None
    topx, topy = 0, 0
    highlight = False
    confirm_move = False

    running = True

    while running:        
        gameboard = new_game.get_board()
        player = new_game.get_player()
        setup_board(SCREEN, player)

        if highlight and (not_none(topx) and not_none(topy)):
                highlight_piece(SCREEN, topx, topy)

        load_icons(SCREEN, gameboard)

        if new_game.get_game_state() != UNFINISHED:
            show_winner(SCREEN, player)

        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_x, mouse_y = event.pos

                    topx, topy = on_grid(mouse_x, mouse_y)
                    in_board = not_none(topx) and not_none(topy)

                    if in_board:
                        if pos1 is None:
                            pos1 = convert(topx, topy)
                            highlight = new_game.correct_turn(pos1)

                        elif confirm_move:
                            pos3 = convert(topx, topy)

                            # Click again to confirm move
                            if pos2 == pos3:
                                new_game.change_turn()

                            else:
                                new_game.undo()
                            
                            confirm_move = False
                            highlight = False
                            pos1, pos2, pos3 = None, None, None

                        elif not_none(pos1):
                            pos2 = convert(topx, topy)

                            if new_game.make_move(pos1, pos2):
                                confirm_move = True
                            else:
                                highlight = False
                                pos1, pos2 = None, None
                    else:
                        if check_new_game(mouse_x, mouse_y):
                            new_game = start_new_game()

                        if confirm_move:
                            new_game.undo()

                        confirm_move = False
                        highlight = False
                        pos1, pos2, pos3 = None, None, None

        pygame.display.update()
    
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
