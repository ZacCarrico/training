"""
lessons learned:
* you cannot use [[0*l]*h] because this creates references of list,
 which means that if you did M[1,0] = 1, it would create [[1,0], [1, 0], [1,0]]
"""

from typing import List

class Board:
    def __init__(self, rows: int, cols: int):
        self.grid = [[0]*cols for _ in range(rows)]
        self.top_left_open_position = (0,0)

    def update_top_left_open_position(self):
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                if self.grid[row][col] == 0:
                    self.top_left_open_position = (row, col)
                    return

    def narrowest_nonzero_height(self):
        pass

    def narrowest_nonzero_width(self):
        pass

class Piece:
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols

class Solver:
    def __init__(self, board: Board, pieces: List[Piece]):
        self.board = board
        self.pieces = self.enumerate_pieces_and_rotations(pieces)
        self.piece_locations = {}

    def enumerate_pieces_and_rotations(self, pieces):
        pieces_and_rotations = {}
        for i, piece in enumerate(pieces):
            pieces_and_rotations[i] = piece
        return pieces_and_rotations

    def min_piece_dimension(self):
        return min([min([piece.cols, piece.rows]) for piece in self.pieces.values()])

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

    def solve(self):
        for piece_key, piece in self.pieces.items():
            rotated_piece = Piece(piece.rows, piece.cols)
            if self.place_piece(self.pieces[piece_key]):
                pass
            elif self.place_piece(rotated_piece):
                pass
        print(self.piece_locations)
        return self.piece_locations

def test_board():
    assert Board(3, 2).grid == [[0, 0], [0, 0], [0, 0]]

def test_Solver__solve_single_piece():
    solver = Solver(Board(3,2), [Piece(2,2)])
    solver.solve()
    print(solver.board.grid)

def test_Solver__solve_multiple_pieces():
    solver = Solver(Board(2,3), [Piece(1,1), Piece(2,2)])
    solver.solve()
    print(solver.board.grid)

def test_Solver__min_piece_dimension():
    solver = Solver(Board(2,3), [Piece(3,2), Piece(1,4)])
    assert solver.min_piece_dimension() == 1

test_Solver__solve_multiple_pieces()