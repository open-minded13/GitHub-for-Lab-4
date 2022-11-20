# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import make_empty_board
from logic import get_winner
from logic import other_player

if __name__ == '__main__':

    board = make_empty_board()
    winner = None
    current_player = 'O'

    while winner == None:

        # TODO: Show the board to the user.
        if board == make_empty_board():
            print("\nLet's start the game. Now, it is",
                  current_player, "'s turn!")
            print("【Tic-Tac-Toe Board】\n" +
                  "      Y = 0 Y = 1 Y = 2\n" +
                  "X = 0", board[0], "\n" +
                  "X = 1", board[1], "\n" +
                  "X = 2", board[2])
        else:
            print("【Tic-Tac-Toe Board】\n",
                  board[0], "\n",
                  board[1], "\n",
                  board[2])

        # TODO: Input a move from the player.
        X, Y = input(
            "Please enter your coordinates X Y (e.g., enter \"0 1\" for the coordinate (0,1)): ").split()
        X = int(X)
        Y = int(Y)
        while (X != 0 and X != 1 and X != 2) or (Y != 0 and Y != 1 and Y != 2):
            print("Incorrect corrdinates entered!")
            X, Y = input("Please re-enter your coordinates X Y: ").split()
            X = int(X)
            Y = int(Y)
        while board[X][Y] != None:
            print("Incorrect corrdinates entered!")
            X, Y = input("Please re-enter your coordinates X Y: ").split()
            X = int(X)
            Y = int(Y)

        # TODO: Update the board.
        if current_player == 'O':
            board[X][Y] = 'O'
        else:
            board[X][Y] = 'X'

        # TODO: Update who's turn it is.
        winner = get_winner(board)  # FIXME
        if winner == None:
            current_player = other_player(current_player)
            print("\nNow, it is", current_player, "'s turn!")
        else:
            print("\n" + winner, "just won the game.")
