# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import *

if __name__ == '__main__':

    board = Board()
    game = Game()
    game_mode = None
    current_player = None
    winner = None
    games_database = read_games_database()

    while winner == None:

        # Step 1: Initialize the game.
        if board.empty == True:

            # Step 1.1
            game_mode = input(
                'Please enter the game mode number (1. You vs Bot; 2. I have friends): ')
            while game_mode != '1' and game_mode != '2':
                print('Invalid! Note: Please enter 1 or 2')
                game_mode = input(
                    'Please re-enter the game mode number (1. You vs Bot; 2. I have friends): ')

            # Step 1.2
            if game_mode == '1':
                human = Human('O')
                bot = Bot('X')        
                current_player = human.name
                print("\nYou are 'O'. Bot is 'X'")
                ######### For Lab of Week 8 (Start Line) ##########
                players_database.loc[0] = {
                    "Name": "User",
                    "Type": "Human",
                }
                players_database.loc[1] = {
                    "Name": "Robot",
                    "Type": "Bot",
                }
                ######### For Lab of Week 8 (End Line) ##########                
            else:
                Temp = input(
                    "Who is going to be the first turn ('O' or 'X')? ")
                while Temp != 'O' and Temp != 'X':
                    print("Invalid! Note: Please enter 'O' or 'X'")
                    Temp = input(
                        "Who is going to be the first turn ('O' or 'X')? ")
                human_player1 = Human(Temp)
                if Temp == 'O':
                    human_player2 = Human('X')
                else:
                    human_player2 = Human('O')                   
                current_player = human_player1.name
                ######### For Lab of Week 8 (Start Line) ##########
                players_database.loc[0] = {
                    "Name": "User 1",
                    "Type": "Human",
                }                
                players_database.loc[1] = {
                    "Name": "User 2",
                    "Type": "Human",
                } 
                ######### For Lab of Week 8 (End Line) ##########                

            # Step 1.3
            print("Let's start the game. Now, it is",
                  str(current_player), "'s turn!")
            print(board)

        # Step 2.1: Start the game mode 1 - Human vs Bot.
        if game_mode == '1':

            # Step 2.1.1: Input a move from the player and update the board.
            if current_player == 'O':
                x, y = input(
                    "Please enter your coordinates X Y (e.g., enter '0 1' for the coordinate (0,1)): ").split()
                x, y = int(x), int(y)
                while (x != 0 and x != 1 and x != 2) or (y != 0 and y != 1 and y != 2):
                    print("Incorrect corrdinates entered!")
                    x, y = input(
                        "Please re-enter your coordinates X Y: ").split()
                    x = int(x)
                    y = int(y)
                while (board.get(x, y) != None):
                    print("Incorrect corrdinates entered!")
                    x, y = input(
                        "Please re-enter your coordinates X Y: ").split()
                    x = int(x)
                    y = int(y)
                board.set(x, y, current_player)
                print(board)
                ######### For Lab of Week 8 (Start Line) ##########
                moves_database.loc[len(moves_database)] = {
                    "Game ID": len(games_database),
                    "Turn": current_player,
                    "Player": "User",
                    "Position": (x, y),
                }
                ######### For Lab of Week 8 (End Line) ##########                
            else:
                x, y = bot.get_random_position(board)
                board.set(x, y, current_player)
                print(board)
                print("'X' just completed the action.")
                ######### For Lab of Week 8 (Start Line) ##########
                moves_database.loc[len(moves_database)] = {
                    "Game ID": len(games_database),
                    "Turn": current_player,
                    "Player": "Robot",
                    "Position": (x, y),
                }
                ######### For Lab of Week 8 (End Line) ########## 

            # Step 2.1.2: Update who is the next turn.
            winner = game.get_winner(board)
            if winner == None:
                current_player = game.get_next_turn(current_player)
                print("\nNow, it is", current_player, "'s turn!")
            elif winner == 'Draw':
                print("\nThe game ended in a draw/tie.")
                ######### For Lab of Week 8 (Start Line) ########## 
                games_database.loc[len(games_database)] = {
                    "Game ID": len(games_database),
                    "Player 1": "User",
                    "Player 2": "Robot",
                    "Winner": "Draw",
                }
                ######### For Lab of Week 8 (End Line) ########## 
            else:
                print("\n" + winner, "just won the game.")
                if winner == 'O':
                    Temp = "User"
                else:
                    Temp = "Robot"
                ######### For Lab of Week 8 (Start Line) ########## 
                games_database.loc[len(games_database)] = {
                    "Game ID": len(games_database),
                    "Player 1": "User",
                    "Player 2": "Robot",
                    "Winner": Temp,
                } 
                ######### For Lab of Week 8 (End Line) ########## 

        # Step 2.2: Start the game mode 2 - Human vs Human.
        else:

            # Step 2.2.1: Input a move from the player and update the board.
            x, y = input(
                "Please enter your coordinates X Y (e.g., enter '0 1' for the coordinate (0,1)): ").split()
            x, y = int(x), int(y)
            while (x != 0 and x != 1 and x != 2) or (y != 0 and y != 1 and y != 2):
                print("Incorrect corrdinates entered!")
                x, y = input("Please re-enter your coordinates X Y: ").split()
                x, y = int(x), int(y)
            while board.get(x, y) != None:
                print("Incorrect corrdinates entered!")
                x, y = input("Please re-enter your coordinates X Y: ").split()
                x, y = int(x), int(y)
            board.set(x, y, current_player)
            print(board)
            ######### For Lab of Week 8 (Start Line) ########## 
            if current_player == human_player1.name:
                Temp = "User 1"
            else:
                Temp = "User 2"
            moves_database.loc[len(moves_database)] = {
                "Game ID": len(games_database),
                "Turn": current_player,
                "Player": Temp,
                "Position": (x, y),
            }
            ######### For Lab of Week 8 (End Line) ########## 

            # Step 2.2.2: Update who is the next turn.
            winner = game.get_winner(board)
            if winner == None:
                current_player = game.get_next_turn(current_player)
                print("\nNow, it is", current_player, "'s turn!")
            elif winner == 'Draw':
                print("\nThe game ended in a draw/tie.")
                ######### For Lab of Week 8 (Start Line) ########## 
                games_database.loc[len(games_database)] = {
                    "Game ID": len(games_database),
                    "Player 1": "User 1",
                    "Player 2": "User 2",
                    "Winner": "Draw",
                }
                ######### For Lab of Week 8 (End Line) ##########           
            else:
                print("\n" + winner, "just won the game.")
                ######### For Lab of Week 8 (Start Line) ########## 
                if winner == human_player1.name:
                    Temp = "User 1"
                else:
                    Temp = "User 2"
                games_database.loc[len(games_database)] = {
                    "Game ID": len(games_database),
                    "Player 1": "User 1",
                    "Player 2": "User 2",
                    "Winner": Temp,
                } 
                ######### For Lab of Week 8 (End Line) ##########

    ######### For Lab of Week 8 (Start Line) ##########    
    print("\nThe movement track of this round:")
    print(moves_database)  
    
    game_history = pd.merge(
                        pd.merge(
                            games_database,
                            players_database.rename(columns = {"Name": "Player 1", "Type": "Player 1 Type",}) 
                        ), 
                        players_database.rename(columns = {"Name": "Player 2", "Type": "Player 2 Type",})        
                    )
    games_database.to_csv(games_database_filename, index = False)
    if len(games_database) > 1:
        game_history.to_csv(game_history_filename, mode = 'a', header = False, index = False)
    else:
        game_history.to_csv(game_history_filename, index = False)
    game_history = pd.read_csv(game_history_filename)
    game_history = game_history.drop_duplicates()  
    game_history.to_csv(game_history_filename, index = False)
    game_history = pd.read_csv(game_history_filename)
    print("\nGame History:")
    print(game_history)
    ######### For Lab of Week 8 (End Line) ########## 