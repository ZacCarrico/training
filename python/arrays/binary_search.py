"""
create a vanilla binary search
"""
import math


def binary_search(A: list, val: int) -> int:
    """
    Requires a sorted list
    Returns the index if the value is in the list.
    If the value is not in the list it returns None
    """
    low = 0
    mid = int(math.ceil(len(A)/2))
    high = len(A) - 1 # assumes a non-empty list
    while low != mid and high != mid:
        if val < A[mid]:
            high = mid
            mid = int(math.floor((low + mid) / 2))
        elif val > A[mid]:
            low = mid
            mid = int(math.ceil((high + mid) / 2))
        elif A[mid] == val:
            return mid

    return None

def test_binary_search():
    assert(binary_search(list(range(10)), 6) == 6)
    assert (binary_search(list(range(10)), 4) == 4)
    assert(binary_search(list(range(10)), 11) == None)
    assert (binary_search(list(range(10)), -1) == None)