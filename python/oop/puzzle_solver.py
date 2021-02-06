"""
lessons learned:
* you cannot use [[0*l]*h] because this creates references of list,
 which means that if you did M[1,0] = 1, it would create [[1,0], [1, 0], [1,0]]
"""

from typing import List, Dict

class Board:
    def __init__(self, rows: int, cols: int):
        self.grid = [[0]*cols for _ in range(rows)]
        self.top_left_open_position = (0,0)

    def update_top_left_open_position(self):
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                if self.grid[row][col] == 0:
                    self.top_left_open_position = (row, col)
                    return None

class Piece:
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols

class PuzzleState:
    def __init__(self, board: Board, pieces: List[Piece], piece_locations: Dict[tuple, tuple]):
        self.board = board
        self.pieces = pieces
        self.piece_locations = piece_locations
        self.is_finished = len(self.pieces) == 0

    def rotate_matrix(self, mat):
        # taken from https://www.geeksforgeeks.org/rotate-matrix-elements/
        if not len(mat):
            return

        """ 
            top : starting row index 
            bottom : ending row index 
            left : starting column index 
            right : ending column index 
        """

        top = 0
        bottom = len(mat) - 1

        left = 0
        right = len(mat[0]) - 1

        while left < right and top < bottom:

            # Store the first element of next row,
            # this element will replace first element of
            # current row
            prev = mat[top + 1][left]

            # Move elements of top row one step right
            for i in range(left, right + 1):
                curr = mat[top][i]
                mat[top][i] = prev
                prev = curr

            top += 1

            # Move elements of rightmost column one step downwards
            for i in range(top, bottom + 1):
                curr = mat[i][right]
                mat[i][right] = prev
                prev = curr

            right -= 1

            # Move elements of bottom row one step left
            for i in range(right, left - 1, -1):
                curr = mat[bottom][i]
                mat[bottom][i] = prev
                prev = curr

            bottom -= 1

            # Move elements of leftmost column one step upwards
            for i in range(bottom, top - 1, -1):
                curr = mat[i][left]
                mat[i][left] = prev
                prev = curr

            left += 1

        return mat

    def min_piece_dimension(self):
        return min([min([piece.cols, piece.rows]) for piece in self.pieces])

    def place_piece(self, piece):
        grid_rows = len(self.board.grid)
        grid_cols = len(self.board.grid[0])
        if piece.rows <= grid_rows - self.board.top_left_open_position[0] \
                and piece.cols <= grid_cols - self.board.top_left_open_position[1]:
            for i in range(piece.rows):
                for j in range(piece.cols):
                    row = self.board.top_left_open_position[0] + i
                    col = self.board.top_left_open_position[1] + j
                    if self.board.grid[row][col] == 1:
                        return False
                    else:
                        self.board.grid[row][col] = 1
            self.piece_locations[self.board.top_left_open_position] = (piece.rows, piece.cols)
            self.board.update_top_left_open_position()
            return True
        return False

    def narrowest_nonzero_length(self):
        narrowest_row = [len([1 for x in array if x == 0]) for array in self.board.grid]
        narrowest_col = [len([1 for x in array if x == 0]) for array in self.rotate_matrix(self.board.grid)]
        return min([_ for _ in narrowest_row + narrowest_col if _ != 0])

def solve(puzzle_state):
    if puzzle_state.is_finished:
        return puzzle_state
    result = None
    for piece_i, piece in puzzle_state.pieces.items():
        print(piece_i)
        curr_pieces = puzzle_state.pieces.copy()
        if puzzle_state.place_piece(piece):
            del curr_pieces[piece_i]
            if piece_i % 2 == 0:
                del curr_pieces[piece_i - 1]
            else:
                del curr_pieces[piece_i + 1]
            result = solve(PuzzleState(puzzle_state.board, curr_pieces, puzzle_state.piece_locations))
        else:
            result = None
    return result

pieces = {
    1: Piece(1,2),
    2: Piece(2,1),
    3: Piece(1,1),
    4: Piece(1,1),
    5: Piece(1,1),
    6: Piece(1,1)
}

pieces = [
    Piece(7,28),
    Piece(14,17),
    Piece(32,11),
    Piece(21,18),
    Piece(21,18),
    Piece(10,7),
    Piece(28,6),
    Piece(14,4),
    Piece(32,10),
    Piece(28,14),
    Piece(21,14),
    Piece(21,14)
]

pieces = {
    1: Piece(7,28),
    2: Piece(28,7),
    3: Piece(14,17),
    4: Piece(17, 14),
    5: Piece(32,11),
    6: Piece(11,32),
    7: Piece(21,18),
    8: Piece(18,21),
    9: Piece(21,18),
    10: Piece(18,21),
    11: Piece(10,7),
    12: Piece(7,10),
    13: Piece(28,6),
    14: Piece(6,28),
    15: Piece(14,4),
    16: Piece(4,14),
    17: Piece(32,10),
    18: Piece(10,32),
    19: Piece(28,14),
    20: Piece(14,28),
    21: Piece(21,14),
    22: Piece(14,21),
    23: Piece(21,14),
    24: Piece(14,21)
}

print(solve(PuzzleState(Board(56,56), pieces, {})).__dict__)


# def solve(board, pieces, piece_locations):
#     puzzle_state = PuzzleState(board, pieces, piece_locations)
#     result = puzzle_state
#     if puzzle_state.narrowest_nonzero_length() < puzzle_state.min_piece_dimension():
#         return piece_locations
#     if puzzle_state.is_finished:
#         return puzzle_state
#     print("new level")
#     for i, piece in enumerate(puzzle_state.pieces):
#         rotated_piece = Piece(piece.cols, piece.rows)
#         if puzzle_state.place_piece(puzzle_state.pieces[i]):
#             one_fewer_pieces = puzzle_state.pieces.copy()
#             del one_fewer_pieces[i]
#             if len(one_fewer_pieces) == 0:
#                 return PuzzleState(board, one_fewer_pieces, piece_locations)
#             result = solve(puzzle_state.board, one_fewer_pieces, puzzle_state.piece_locations)
#             if len(result.pieces) == 0:
#                 return result
#         elif puzzle_state.place_piece(rotated_piece):
#             one_fewer_pieces = puzzle_state.pieces.copy()
#             del one_fewer_pieces[i]
#             if len(one_fewer_pieces) == 0:
#                 return PuzzleState(board, one_fewer_pieces, piece_locations)
#             result = solve(puzzle_state.board, one_fewer_pieces, puzzle_state.piece_locations)
#             if len(result.pieces) == 0:
#                 return result
#     return result

# def map_pieces(pieces):
#     mapped_pieces = {}
#     for i, piece in enumerate(pieces):
#         mapped_pieces[i] = piece
#         mapped_pieces[i+1] = Piece(piece.cols, piece.rows)
#     return mapped_pieces

def test_board():
    assert Board(3, 2).grid == [[0, 0], [0, 0], [0, 0]]

pieces = [
    Piece(7,28),
    Piece(14,17),
    Piece(32,11),
    Piece(21,18),
    Piece(21,18),
    Piece(10,7),
    Piece(28,6),
    Piece(14,4),
    Piece(32,10),
    Piece(28,14),
    Piece(21,14),
    Piece(21,14)
]


# def test_Board__narrowest_nonzero_length():
#     solver = PuzzleState(Board(56, 56), pieces, {})
#     print(len(solve(solver.board, solver.pieces, solver.piece_locations).pieces))
# test_Board__narrowest_nonzero_length()

def test_regular():
    solver = PuzzleState(Board(1, 2), [Piece(1,2)], {})
    assert len(solve(solver.board, solver.pieces, solver.piece_locations).pieces) == 0

def test_rotating():
    solver = PuzzleState(Board(1, 2), [Piece(2,1)], {})
    assert len(solve(solver.board, solver.pieces, solver.piece_locations).pieces) == 0

def test_narrowest_nonzero_length():
    # narrowest_nonzero_length()
    pass

# def test_three_pieces():
#     solver = PuzzleState(Board(2, 2), [Piece(1,1), Piece(1,1), Piece(2,1)], {})
#     assert len(solve(solver.board, solver.pieces, solver.piece_locations).pieces) == 0
#
# test_three_pieces()

from itertools import permutations
import time

# def create_all_rotation_permutations():
#     rotation_perms = []
#     for i in range(len(pieces)):
#         perms = [_ for _ in permutations(pieces, i)]
#         print(len(perms))
#         rotation_perms.append(perms)
#
# # this times out
# create_all_rotation_permutations()
# def create_set_with_rotations():
#     pieces_permutations = [pieces]
#     for n_pieces_to_rotate in range(len())
#     for i, piece in enumerate(pieces):
#         if i + 1 < len(pieces):
#             new_pieces = pieces[:i] + [Piece(piece.cols, piece.rows)] + pieces[i + 1:]
#             pieces_permutations.append(new_pieces)
#         else:
#             pieces_permutations.append(pieces[:i] + [Piece(piece.cols, piece.rows)])

# def evaluate_feasibility_of_brute_force():
#     start = time.time()
#     # create_set_with_rotations()
#     print(len(pieces))
#     print(len(set(pieces)))
#     print(time.time() - start)
#
# evaluate_feasibility_of_brute_force()