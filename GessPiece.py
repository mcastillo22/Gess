class GessPiece:
    def __init__(self, origin, target, board):
        self._origin = origin
        self._target = target
        self._board = board
        self._boardlist = board.get_board()

        self._x1, self._y1 = self._origin["Center"]
        self._x2, self._y2 = self._target["Center"]

        self._piece = {}
        self.create_piece()

    def create_piece(self):
        for position, coordinates in self._origin.items():
            self._piece[position] = {"Coordinate": coordinates}
        for position, coordinates in self._origin.items():
            x, y = coordinates
            self._piece[position]["Stone"] = self._boardlist[x][y]

    def unlimited(self):
        """Returns if the piece can move unlimited spaces or not"""
        if self._piece["Center"]["Stone"] != " ":
            return True
        return False

    def clear_origin(self):
        """Clears the original footprint on the board of the piece"""
        for position in self._origin.values():
            self._boardlist[position[0]][position[1]] = " "

    def move_piece(self):
        """Moves the stones to the targeted positions in the same arrangement"""
        coords = [c for c in self._target.values()]
        stones = [s["Stone"] for s in self._piece.values()]
        final = dict(zip(coords, stones))

        if self.available_moves():
            for coord, stone in final.items():
                self._board.place_stone(coord, stone)

    def get_direction(self):
        """Determines the direction the piece wants to move and by how many squares"""
        x_change, y_change = self._x2 - self._x1, self._y2 - self._y1
        compass = ""
        if x_change < 0:
            compass = "S"
        elif x_change > 0:
            compass = "N"
        if y_change < 0:
            compass += "W"
        elif y_change > 0:
            compass += "E"

        if compass in ["NW", "SE", "NW", "NE"] and abs(x_change) != abs(y_change):
            compass = False

        if abs(x_change) == 0:
            change = abs(y_change)
        else:
            change = abs(x_change)

        return compass, change

    def available_moves(self):
        """Checks that the piece can move to the desired coordinates based on the piece stones"""
        direction, change = self.get_direction()

        if self._piece[direction]["Stone"] == " ":
            return False

        if not self.unlimited() and change > 3:
            return False

        positions = [p for p in self._origin.keys()]
        positions.remove("Center")

        moves = [
            (self._x1 - change, self._y1 - change),
            (self._x1 - change, self._y1),
            (self._x1 - change, self._y1 + change),
            (self._x1, self._y1 - change),
            (self._x1, self._y1 + change),
            (self._x1 + change, self._y1 - change),
            (self._x1 + change, self._y1),
            (self._x1 + change, self._y1 + change)
        ]

        all_moves = dict(zip(positions, moves))

        return self.blocking(all_moves[direction])

    def blocking(self, direction):
        """
        Receives the coordinates of the desired movement.

        Checks the direction the piece wants to move relative to the target.
        Determines if there is a piece blocking that desired movement.
        Returns True if there is no blocking.
        """
        x_change, y_change = self._x2 - self._x1, self._y2 - self._y1

        xstep, ystep = 1, 1
        if x_change < 0:
            xstep = -1
        if y_change < 0:
            ystep = -1

        if x_change == 0:
            for y in range(self._y1, direction[1], ystep):
                check_footprint = self._board.get_footprint(self._x1, y)
                for pos in check_footprint.values():
                    if self._boardlist[pos[0]][pos[1]] != " ":
                        return False
            return True

        if y_change == 0:
            for x in range(self._x1, direction[0], xstep):
                check_footprint = self._board.get_footprint(x, self._y1)
                for pos in check_footprint.values():
                    if self._boardlist[pos[0]][pos[1]] != " ":
                        return False
            return True

        else:
            for x in range(self._x1, direction[0], xstep):
                for y in range(self._y1, direction[1], ystep):
                    check_footprint = self._board.get_footprint(x, y)
                    for pos in check_footprint.values():
                        if self._boardlist[pos[0]][pos[1]] != " ":
                            return False

            return True
