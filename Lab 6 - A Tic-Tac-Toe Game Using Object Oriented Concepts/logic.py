# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.

class Board:

    def __init__(self):
        self.rows = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ]
        self.empty = True

    def __str__(self):
        s = '\n-------\n'
        for row in self.rows:
            for cell in row:
                s = s + '|'
                if cell == None:
                    s = s + ' '
                else:
                    s = s + cell
            s = s + '\n-------\n'
        return s

    def get(self, x, y):
        return self.rows[x][y]

    def set(self, x, y, value):
        self.rows[x][y] = value
        self.empty = False

    def get_winner(self):
        """Determines the winner of the given board. Returns 'X', 'O', or None."""

        if self.rows[0][0] == self.rows[0][1] == self.rows[0][2]:
            if self.rows[0][0] == 'O' or self.rows[0][0] == 'X':
                return self.rows[0][0]
            else:
                return None
        elif self.rows[1][0] == self.rows[1][1] == self.rows[1][2]:
            if self.rows[1][0] == 'O' or self.rows[1][0] == 'X':
                return self.rows[1][0]
            else:
                return None
        elif self.rows[2][0] == self.rows[2][1] == self.rows[2][2]:
            if self.rows[2][0] == 'O' or self.rows[2][0] == 'X':
                return self.rows[2][0]
            else:
                return None
        elif self.rows[0][0] == self.rows[1][0] == self.rows[2][0]:
            if self.rows[0][0] == 'O' or self.rows[0][0] == 'X':
                return self.rows[0][0]
            else:
                return None
        elif self.rows[0][1] == self.rows[1][1] == self.rows[2][1]:
            if self.rows[0][1] == 'O' or self.rows[0][1] == 'X':
                return self.rows[0][1]
            else:
                return None
        elif self.rows[0][2] == self.rows[1][2] == self.rows[2][2]:
            if self.rows[0][2] == 'O' or self.rows[0][2] == 'X':
                return self.rows[0][2]
            else:
                return None
        elif self.rows[0][0] == self.rows[1][1] == self.rows[2][2]:
            if self.rows[0][0] == 'O' or self.rows[0][0] == 'X':
                return self.rows[0][0]
            else:
                return None
        elif self.rows[0][2] == self.rows[1][1] == self.rows[2][0]:
            if self.rows[0][2] == 'O' or self.rows[0][2] == 'X':
                return self.rows[0][2]
            else:
                return None
        else:
            return None


class Player:

    def __init__(self, name):
        self.name = name

    def next_turn(self):
        if self.name == 'O':
            self.name = 'X'
        else:
            self.name = 'O'
