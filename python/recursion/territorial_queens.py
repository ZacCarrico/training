"""
Place queens on an nxn chess board such that
none are in the same row, column, or diagonal
as any other queen.

patterns:
* function within a function to provide local variable
 scope for recursion

lessons learned:
* because you only have one queen per column,
 you can use a list instead of a matrix.
 The indexes of the list are the row numbers
 and the values are the col numbers
* check for diagonals by checking that abs(col - prev_col) != row - prev_row

* time complexity is at least O(n), where n is the number of rows, but
 the way this increases isn't known
* the number of possible placements is at most n! because there can only
 be one queen per row
"""
from typing import List

def get_all_queen_placements(n: int) -> List[List[int]]:
    def add_placement(row) -> None:
        if row == n:
            results.append(col_placement.copy())
            return None
        for col in range(n):
            if all(
                # 0 checks that col are not the same and `row - ith_row` checks diagonals
                # diagonal check eg. (0,0) and (1,1): row = 1 and ith_row = 0, and col = 1 and prev_col = 0
                abs(prev_col - col) not in (0, row - prev_row)
                for prev_row, prev_col in enumerate(col_placement[:row])
            ):
                col_placement[row] = col
                add_placement(row + 1)
    results: List[List[int]] = []
    col_placement = [0] * n
    add_placement(0)
    return results

def test_get_all_queen_placements():
    assert get_all_queen_placements(4) == [[1, 3, 0, 2], [2, 0, 3, 1]]