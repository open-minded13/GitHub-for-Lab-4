# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import *
import random

if __name__ == '__main__':

    board = Board()
    winner = None
    game_mode = None

    while winner == None:

        # TODO: Initialize the game.
        if board.empty == True:

            game_mode = input(
                'Please enter the game mode number (1. You vs Bot; 2. I have friends): ')
            while game_mode != '1' and game_mode != '2':
                print('Invalid! Note: Please enter 1 or 2')
                game_mode = input(
                    'Please re-enter the game mode number (1. You vs Bot; 2. I have friends): ')

            if game_mode == '1':
                current_player = Player('O')
                print('\nYou are \'O\'. Bot is \'X\'')
            else:
                Temp = input(
                    'Who is going to be the first turn (\'O\' or \'X\')? ')
                while Temp != 'O' and Temp != 'X':
                    print('Invalid! Note: Please enter \'O\' or \'X\'')
                    Temp = input(
                        'Who is going to be the first turn (\'O\' or \'X\')? ')
                current_player = Player(Temp)

            print('Let\'s start the game. Now, it is',
                  str(current_player.name), '\'s turn!')
            print(board)

        # TODO: Human vs Bot
        if game_mode == '1':

            if current_player.name == 'O':
                # TODO: Input a move from the player.
                X, Y = input(
                    "Please enter your coordinates X Y (e.g., enter '0 1' for the coordinate (0,1)): ").split()
                X = int(X)
                Y = int(Y)
                while (X != 0 and X != 1 and X != 2) or (Y != 0 and Y != 1 and Y != 2):
                    print("Incorrect corrdinates entered!")
                    X, Y = input(
                        "Please re-enter your coordinates X Y: ").split()
                    X = int(X)
                    Y = int(Y)

                # TODO: Update the board.
                board.set(X, Y, current_player.name)

            else:
                X = random.randint(0, 2)
                Y = random.randint(0, 2)
                while board.get(X, Y) != None:
                    X = random.randint(0, 2)
                    Y = random.randint(0, 2)

                board.set(X, Y, current_player.name)

            if current_player.name == 'X':
                print(board)
                print("'X' just completed the action.")
            else:
                print(board)

            # TODO: Update who is the next turn.
            winner = board.get_winner()
            if winner == None:
                current_player.next_turn()
                print("\nNow, it is", current_player.name, "'s turn!")
            else:
                print("\n" + winner, "just won the game.")

        # TODO: Human vs Human
        else:
            # TODO: Input a move from the player.
            X, Y = input(
                "Please enter your coordinates X Y (e.g., enter '0 1' for the coordinate (0,1)): ").split()
            X = int(X)
            Y = int(Y)
            while (X != 0 and X != 1 and X != 2) or (Y != 0 and Y != 1 and Y != 2):
                print("Incorrect corrdinates entered!")
                X, Y = input("Please re-enter your coordinates X Y: ").split()
                X = int(X)
                Y = int(Y)

            # TODO: Update the board.
            board.set(X, Y, current_player.name)

            # TODO: Update who is the next turn.
            winner = board.get_winner()
            if winner == None:
                current_player.next_turn()
                print(board)
                print("\nNow, it is", current_player.name, "'s turn!")
            else:
                print("\n" + winner, "just won the game.")
