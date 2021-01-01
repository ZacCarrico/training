"""
create a vanilla binary search
iterative:
time: O(logN), space: O(1)
recursive:
time: O(logN), space: O(logN)
"""
import math


def iterative_binary_search(A: list, target: int) -> int:
    """
    Requires a sorted list
    Returns the index if the value is in the list.
    If the value is not in the list it returns None
    """
    low = 0
    mid = int(math.ceil(len(A)/2))
    high = len(A) - 1 # assumes a non-empty list
    while low != mid and high != mid:
        if target < A[mid]:
            high = mid
            mid = int(math.floor((low + mid) / 2))
        elif target > A[mid]:
            low = mid
            mid = int(math.ceil((high + mid) / 2))
        elif A[mid] == target:
            return mid
    return None

def recursive_binary_search(A: list, target: int, low: int, high: int) -> int:
    mid = int(math.ceil((low + high)/2))
    if target == A[mid]:
        return mid
    elif target < A[mid]:
        return recursive_binary_search(A, target, low, mid - 1)
    elif target > A[mid]:
        return recursive_binary_search(A, target, mid + 1, high)

def test_iterative_binary_search():
    assert(iterative_binary_search(list(range(10)), 6) == 6)
    assert (iterative_binary_search(list(range(10)), 4) == 4)
    assert(iterative_binary_search(list(range(10)), 11) == None)
    assert (iterative_binary_search(list(range(10)), -1) == None)

def test_recursive_binary_search():
    A = list(range(10))
    low = 0
    high = len(A) - 1
    assert(recursive_binary_search(A, 6, low, high) == 6)
    assert (recursive_binary_search(A, 4, low, high) == 4)