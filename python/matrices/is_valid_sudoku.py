"""
Sudoku is a game played on a 9x9 matrix.
It uses integers 1-9, and one of the rules
is there cannot be duplicates of any integer
in a single row, column, or within designated
3x3 regions.
The purpose of this code is to simply verify
whether these no-dupes rules have been broken,
given a 9x9 matrix.

input: List(List()): the empty indices will be passed as zeroes
output: boolean

patterns:
* nested for loop to iterate matrix

lessons learned:
* list(filter(lambda x: expression, list)) is useful
* list comprehension for the columns just requires switching i and j during list comprehension
* use the sqrt of the subarray's length to get the region size
"""
import math


def has_duplicate(A: list) -> bool:
    zeroless = list(filter(lambda x: x != 0, A))
    return len(set(zeroless)) != len(zeroless)

def is_valid_sudoku(A: list(list())) -> bool:

    n = len(A[0]) # we're assuming it's always a sqr matrix

    # checking that rows and columns that span the
    #  entire length of the sudoku matrix are valid
    if any(
            has_duplicate([A[i][j] for j in range(n)]) and  # checking rows
            has_duplicate(([A[j][i] for j in range(n)]))  # checking cols
            for i in range(n)
    ):
        return False

    region_size = int(math.sqrt(n))

    # checking regions of matrix (3x3 grids for normal sudoku) for validity
    return all(
        not has_duplicate([
            A[i][j]
            for i in range(I*region_size, (I+1)*region_size)
            for j in range(J*region_size, (J+1)*region_size)
        ])
        for I in range(region_size)
        for J in range(region_size)
    )

def test_has_duplicate():
    assert(has_duplicate([0] * 9) == False)
    assert(has_duplicate([1] * 9) == True)

def test_is_valid_sudoku():
    valid_sudoku = [[0]*9 for _ in range(9)]
    invalid_sudoku = [[1]*9 for _ in range(9)]
    assert(is_valid_sudoku(valid_sudoku) == True)
    assert (is_valid_sudoku(invalid_sudoku) == False)