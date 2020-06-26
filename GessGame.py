from GessPiece import GessPiece
from GessBoard import GessBoard


class GessGame:
    """Gess Game Engine"""
    def __init__(self):
        """Initialize a new Game Object"""
        self._game_state = "UNFINISHED"
        self._turn = "BLACK"
        self._board = GessBoard()
        self._debug_mode = False

    def resign_game(self):
        """Lets current player concede the game"""
        if self._turn == "WHITE":
            self._game_state = "BLACK_WON"
        else:
            self._game_state = "WHITE_WON"

    def get_player(self):
        """Return current player"""
        return self._turn

    def correct_turn(self, center):
        """Returns Bool if selected piece belongs to the player whose turn it is"""
        return self._board.is_piece(center) == self._turn[0]

    def make_move(self, start, end):
        """
        Takes the center of a piece and the center of the position the player desires moving.
        Checks that requested move is valid and updates any game conditions based on that move
        """
        # Check move validity:
        #   1. Game is unfinished
        if self._game_state != "UNFINISHED":
            return False
        
        if start == end:
            return False

        #   3. Requested piece belongs to the player whose turn it is
        correct_turn = self.correct_turn(start)
        if not correct_turn:
            return False

        #   4. The requested movement is valid
        x1, y1 = start
        x2, y2 = end

        # If target movement is out of bounds, return False
        if x2 in [0, 19] or y2 in [0, 19]:
            return False

        original = self._board.get_footprint(x1, y1)
        target = self._board.get_footprint(x2, y2)

        piece = GessPiece(original, target, self._board)

        self._board.make_copy()
        piece.clear_origin()

        valid = piece.available_moves()
        if valid:
            piece.move_piece()
            self._board.clear_edges()

        # If move results in the player making the move not having a ring, return False
        ring_check = self._board.check_rings(self._turn)

        if not ring_check or not valid:
            self._board.undo_board()
            return False

        # If opponent has no rings after valid move, the current player wins
        if not self._board.check_rings(self.get_opponent()):
            self._game_state = self.get_player() + "_WON"
            return True

        # Pass turn and return true
        self.change_turn()

        if self._debug_mode:
            self.print_board()

        return True

    def get_opponent(self):
        if self._turn == "BLACK":
            return "WHITE"
        return "BLACK"

    def change_turn(self):
        """Updates whose turn it is"""
        if self._turn == "BLACK":
            self._turn = "WHITE"
        else:
            self._turn = "BLACK"

    def get_game_state(self):
        """Returns game state: UNFINISHED, BLACK_WON, or WHITE_WON"""
        return self._game_state

    def print_board(self):
        """For CLI or debugging purposes, prints board on CL"""
        self._board.print_board()

    def debug_mode(self):
        self._debug_mode = True

    def get_board(self):
        """Returns the board associated with game object"""
        return self._board.get_board()
