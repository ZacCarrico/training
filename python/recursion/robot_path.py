"""
At the top left of a matrix is a robot that can only move down and to the right.
There are inaccessible points in the matrix.
Return True if the robot can reach the bottom right or False if it cannot.

patterns:
* to use create a fake-global variable use a nested function


lessons learned:
* if we let the robot visit the same place
 multiple times, the time complexity = O(2^(r+c)),
 space = O(r+c) (I'm guessing about space)
* if we don't let the robot visit the same place
 multiple times, the time complexity = O(r*c), space = O(r+c) (I'm guessing about space)
"""

def is_bottom_right_reachable(M, i , j):
    """Doesn't cache visited grid points"""
    print(M)
    if i == len(M) - 1 and j == len(M[0]) - 1:
        return True

    # if the robot exceeds the bounds of the matrix or the point is inaccessible
    if i == len(M) or j == len(M[0]) or M[i][j] == 'x':
        return False

    return is_bottom_right_reachable(M, i + 1, j) or is_bottom_right_reachable(M, i, j + 1)

def test_is_bottom_righ_reachable():
    assert is_bottom_right_reachable([[0, 0], [0, 0]], 0, 0) == True
    assert is_bottom_right_reachable([[0, 'x'], ['x', 0]], 0, 0) == False

def is_bottom_right_reachable_with_cache(M, i, j):
    """The purpose of the wrapper function is to create a local variable (M)
    that acts like a global variable"""
    M = M
    def is_path_possible(M, i, j):
        print(M)
        if i == len(M) - 1 and j == len(M[0]) - 1:
            return True

        # if the robot exceeds the bounds of the matrix or the point is inaccessible
        if i == len(M) or j == len(M[0]) or M[i][j] == 'x':
            return False

        M[i][j] = 'x'

        return is_path_possible(M, i + 1, j) or is_path_possible(M, i, j + 1)
    return is_path_possible(M, i, j)

def test_is_bottom_right_reachable_with_cache():
    assert is_bottom_right_reachable_with_cache([[0, 0], [0, 0]], 0, 0) == True
    assert is_bottom_right_reachable_with_cache([[0, 0, 0], [0, 0, 0]], 0, 0) == True
    assert is_bottom_right_reachable_with_cache([[0, 'x'], ['x', 0]], 0, 0) == False