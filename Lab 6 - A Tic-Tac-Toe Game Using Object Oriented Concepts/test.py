import unittest
import logic
from logic import *


class TestLogic(unittest.TestCase):

    def test_get_of_Board(self):
        test_board = Board()
        test_board.rows = [['X', None, 'O'],
                           [None, 'X', None],
                           [None, 'O', 'X']]
        self.assertEqual(test_board.get(0, 0), 'X')

    def test_set_of_Board(self):
        test_board = Board()
        test_board.rows = [['X', None, 'O'],
                           [None, 'X', None],
                           [None, 'O', 'X']]
        test_board.set(0, 2, 'O')
        self.assertEqual(test_board.rows[0][2], 'O')

    def test_get_next_turn_of_Game_1(self):
        self.assertEqual(logic.Game.get_next_turn(self, 'O'), 'X')

    def test_get_next_turn_of_Game_2(self):
        self.assertEqual(logic.Game.get_next_turn(self, 'X'), 'O')

    def test_get_winner_of_Game_1(self):
        test_board = Board()
        test_board.rows = [['X', None, 'O'],
                           [None, 'X', None],
                           [None, 'O', 'X']]
        self.assertEqual(logic.Game.get_winner(self, test_board), 'X')

    def test_get_winner_of_Game_2(self):
        test_board = Board()
        test_board.rows = [['X', 'X', 'O'],
                           ['X', 'O', 'O'],
                           ['O', 'O', 'X']]
        self.assertEqual(logic.Game.get_winner(self, test_board), 'O')

    def test_get_winner_of_Game_3(self):
        test_board = Board()
        test_board.rows = [['X', None, 'O'],
                           [None, 'X', None],
                           [None, 'O', 'O']]
        self.assertEqual(logic.Game.get_winner(self, test_board), None)

    def test_get_winner_of_Game_4(self):
        test_board = Board()
        test_board.rows = [['X', 'O', 'O'],
                           ['O', 'X', 'X'],
                           ['X', 'O', 'O']]
        self.assertEqual(logic.Game.get_winner(self, test_board), 'Draw')

    def test_get_random_position_of_Bot(self):
        test_board = Board()
        test_board.rows = [['X', None, 'O'],
                           ['O', 'X', 'X'],
                           ['X', 'O', 'O']]
        x, y = logic.Bot.get_random_position(self, test_board)
        self.assertEqual(x, 0)
        self.assertEqual(y, 1)


if __name__ == '__main__':
    unittest.main()
