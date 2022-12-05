# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.
import random
import pandas as pd

games_database_filename = "games_database.csv"
def read_games_database():
    try:
        return pd.read_csv(games_database_filename)
    except FileNotFoundError:
        return pd.DataFrame(columns = [
            "Game ID",
            "Player 1",
            "Player 2",
            "Winner",
        ])

moves_database = pd.DataFrame(columns = [
    "Game ID",
    "Turn",
    "Player",
    "Position",
])

players_database = pd.DataFrame(columns = [
    "Name",
    "Type",
])

game_history_filename = "game_history.csv"
game_history = pd.DataFrame(columns = [
    "Game ID",
    "Player 1",
    "Player 2",
    "Winner",
    "Player 1 Type",
    "Player 2 Type",   
    ])

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


class Game:

    def get_next_turn(self, current_player):
        if current_player == 'O':
            return 'X'
        else:
            return 'O'

    def get_winner(self, board):
        """Determines the winner of the given board. Returns 'X', 'O', or None."""

        if board.rows[0][0] == board.rows[0][1] == board.rows[0][2]:
            if board.rows[0][0] == 'O' or board.rows[0][0] == 'X':
                return board.rows[0][0]
            else:
                return None
        elif board.rows[1][0] == board.rows[1][1] == board.rows[1][2]:
            if board.rows[1][0] == 'O' or board.rows[1][0] == 'X':
                return board.rows[1][0]
            else:
                return None
        elif board.rows[2][0] == board.rows[2][1] == board.rows[2][2]:
            if board.rows[2][0] == 'O' or board.rows[2][0] == 'X':
                return board.rows[2][0]
            else:
                return None
        elif board.rows[0][0] == board.rows[1][0] == board.rows[2][0]:
            if board.rows[0][0] == 'O' or board.rows[0][0] == 'X':
                return board.rows[0][0]
            else:
                return None
        elif board.rows[0][1] == board.rows[1][1] == board.rows[2][1]:
            if board.rows[0][1] == 'O' or board.rows[0][1] == 'X':
                return board.rows[0][1]
            else:
                return None
        elif board.rows[0][2] == board.rows[1][2] == board.rows[2][2]:
            if board.rows[0][2] == 'O' or board.rows[0][2] == 'X':
                return board.rows[0][2]
            else:
                return None
        elif board.rows[0][0] == board.rows[1][1] == board.rows[2][2]:
            if board.rows[0][0] == 'O' or board.rows[0][0] == 'X':
                return board.rows[0][0]
            else:
                return None
        elif board.rows[0][2] == board.rows[1][1] == board.rows[2][0]:
            if board.rows[0][2] == 'O' or board.rows[0][2] == 'X':
                return board.rows[0][2]
            else:
                return None
        else:
            draw_counter = 0
            for i in range(len(board.rows)):
                for j in range(len(board.rows[i])):
                    if board.get(i, j) != None:
                        draw_counter += 1
            if draw_counter == 9:
                return 'Draw'
        return None


class Human:

    def __init__(self, name):
        self.name = name


class Bot:

    def __init__(self, name):
        self.name = name

    def get_random_position(self, board):
        x, y = random.randint(0, 2), random.randint(0, 2)
        while board.get(x, y) != None:
            x, y = random.randint(0, 2), random.randint(0, 2)
        return x, y
