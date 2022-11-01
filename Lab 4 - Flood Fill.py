from re import A
from typing import List

board = [
    "......................",
    "......##########......",
    "......#........#......",
    "......#........#......",
    "......#........#####..",
    "....###............#..",
    "....#............###..",
    "....##############....",
]


# Step 1 - Since the board is an str object, assignment is not allowed. We want to convert it to a list type
Board = []
for x in range(len(board)):
    Board = Board + [[0] * len(board[x])]
for x in range(len(board)):
    Board[x] = list(board[x])


# Step 3 - The flood fill function. The function implemented the concept of recursion.
def flood_fill(input_board: List[str], old: str, new: str, x: int, y: int) -> List[str]:
    """Returns board with old values replaced with new values
    through flood filling starting from the coordinates x, y
    Args:
        input_board (List[str])
        old (str): Value to be replaced
        new (str): Value that replaces the old
        x (int): X-coordinate of the flood start point
        y (int): Y-coordinate of the flood start point
    Returns:
        List[str]: Modified board
    """

    if x >= 7 or x <= 0 or y >= 21 or y <= 0:
        return
    if Board[x][y] == '~':
        return
    if Board[x][y] == '#':
        return

    if Board[x][y] == old:
        Board[x][y] = new

    flood_fill(input_board, old, new, x+1, y)
    flood_fill(input_board, old, new, x-1, y)
    flood_fill(input_board, old, new, x, y+1)
    flood_fill(input_board, old, new, x, y-1)

    return Board


# Step 2 - Execute the flood_fill function, and store the result into modified_board.
modified_board = flood_fill(input_board=Board, old=".", new="~", x=5, y=12)


# Step 4 - Print modified_board as the form of an str object.
for x in range(len(board)):
    print(''.join(str(a) for a in modified_board[x]))

# Expected output:
# ......................
# ......##########......
# ......#~~~~~~~~#......
# ......#~~~~~~~~#......
# ......#~~~~~~~~#####..
# ....###~~~~~~~~~~~~#..
# ....#~~~~~~~~~~~~###..
# ....##############....
