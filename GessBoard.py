from constants import *


class GessBoard:
    """Controls the board associated with the Gess Game"""
    def __init__(self):
        self._board = [[" " for x in range(20)] for y in range(20)]
        self._temp = None

        init_black_arr = {
            1: [2, 4, 6, 7, 8, 9, 10, 11, 12, 13, 15, 17],
            2: [1, 2, 3, 5, 7, 8, 9, 10, 12, 14, 16, 17, 18],
            3: [2, 4, 6, 7, 8, 9, 10, 11, 12, 13, 15, 17],
            6: [2, 5, 8, 11, 14, 17]}
        init_white_arr = {
            18: [2, 4, 6, 7, 8, 9, 10, 11, 12, 13, 15, 17],
            17: [1, 2, 3, 5, 7, 8, 9, 10, 12, 14, 16, 17, 18],
            16: [2, 4, 6, 7, 8, 9, 10, 11, 12, 13, 15, 17],
            13: [2, 5, 8, 11, 14, 17]}

        for key, item in init_black_arr.items():
            for i in item:
                self._board[key][i] = B

        for key, item in init_white_arr.items():
            for i in item:
                self._board[key][i] = W

    def print_board(self):
        """Prints board for CL"""

        def print_alpha():
            print(" ", end="")
            for char in ALPHA:
                print(f" {char} ", end=" ")
            print()

        def print_black(stone):
            print(f" \033[1;40m{stone}\033[000000m ", end="|")

        def print_white(stone):
            print(f" \033[34;1;44m{stone}\033[000000m ", end="|")

        print()
        print_alpha()
        print("|---" * 20)
        for row in range(len(self._board) - 1, -1, -1):
            print("|", end="")
            for x in self._board[row]:
                if x == B:
                    print_black(x)
                elif x == W:
                    print_white(x)
                else:
                    print(" " + x, end=" |")
            print(f" {row + 1}\n" + "|---" * 20)
        print_alpha()

    def convert(self, square):
        if square[0] not in ALPHA or int(square[1:]) > 20:
            return False

        row = int(square[1:]) - 1
        col = ALPHA.index(square[0])

        return row, col

    def get_footprint(self, x, y):
        """Gets 3x3 footprint of the board from the passed coordinates (x, y)"""
        footprint = {
            SW: (x - 1, y - 1),
            S: (x - 1, y),
            SE: (x - 1, y + 1),
            W: (x, y - 1),
            CENTER: (x, y),
            E: (x, y + 1),
            NW: (x + 1, y - 1),
            N: (x + 1, y),
            NE: (x + 1, y + 1)
        }

        return footprint

    def is_piece(self, center):
        """
        Determines if the piece at the given center is valid
        Returns the player whose piece it belongs to
        """

        x, y = center

        # Ensure piece is not out of bounds
        oob = [0, 19]
        if x in oob or y in oob:
            return False

        pieces = []
        for space in self.get_footprint(x, y).values():
            piece = self._board[space[0]][space[1]]
            if piece != " ":
                pieces.append(piece)

        if not pieces:
            return False

        if self._board[x][y] != " " and len(pieces) == 1:
            return False

        # Check that stones in piece belong to the same player
        check = pieces[0]
        for piece in pieces:
            if piece != check:
                return False

        return check

    def check_rings(self, player):
        """Iterates through board to determine if passed player has a valid ring on the board"""
        player = (player.upper())[0]
        for x in range(1, 19):
            for y in range(1, 19):
                footprint = self.get_footprint(x, y)

                ring = []
                for space in footprint.values():
                    ring.append(self._board[space[0]][space[1]])
                if ring == [player, player, player, player, " ", player, player, player, player]:
                    return True

        return False

    def clear_edges(self):
        """Clears the edges of the board"""
        for col in range(ARRAY-1):
            self._board[0][col], self._board[19][col] = " ", " "
        for row in range(1, 19):
            self._board[row][0], self._board[row][19] = " ", " "

    def make_copy(self):
        """Makes a temporary copy of the current board and the stones' positions"""
        self._temp = [row[:] for row in self._board]

    def undo_board(self):
        """Changes the current board to the stored temporary board"""
        self._board = self._temp
        self._temp = None

    def get_board(self):
        return self._board

    def place_stone(self, coord, stone):
        """Places the given stone to the given coordinate"""
        self._board[coord[0]][coord[1]] = stone
