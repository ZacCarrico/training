"""
Pascal triangle is a matrix of numbers that can be presented like this:
     1
    1 1
   1 2 1
  1 3 3 1
 1 4 6 4 1
1 5 10 10 5 1
...

written another way:
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
...

Write a function to return the value at an index [i, j],
where i is the row and j is like the column (0 indexed)

patterns:
* base case is when the indexes are zero
* return the sum of the functions with decremented index args

time complexity and space complexity for this isn't trivial
"""

def get_point(i: int, j: int) -> int:
    if j == 0 or j == i:
        return 1
    return get_point(i - 1, j - 1) + get_point(i - 1, j)

def test_get_point():
    assert get_point(2, 1) == 2
    assert get_point(5, 4) == 5