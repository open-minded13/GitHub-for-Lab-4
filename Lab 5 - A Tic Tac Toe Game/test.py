import unittest
import logic


class TestLogic(unittest.TestCase):

    def test_get_winner_1(self):
        board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]
        self.assertEqual(logic.get_winner(board), 'X')

    def test_get_winner_2(self):
        board = [
            ['X', 'O', 'O'],
            ['O', 'X', 'X'],
            ['X', 'O', 'O'],
        ]
        self.assertEqual(logic.get_winner(board), 'Draw')

    def test_other_player(self):
        self.assertEqual(logic.other_player('O'), 'X')


if __name__ == '__main__':
    unittest.main()
