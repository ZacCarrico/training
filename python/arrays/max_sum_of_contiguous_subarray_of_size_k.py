"""
Find the contiguous subarray of size k with the maximum
patterns:
* check max(current, max_seen_so_far)
lessons learned:
* the only think slightly tricky was to use arr[i-k+1:i+1] for calculating the sliding window sum
"""
import unittest


def max_subarray(arr, k):
    if k > len(arr):
        return None
    max_so_far = sum(arr[:k])
    for i in range(k, len(arr)):
        current_sum = sum(arr[i-k+1:i+1])
        max_so_far = max(max_so_far, current_sum)
    return max_so_far

class TestMaxSubarray(unittest.TestCase):
    def test_max_subarray(self):
        assert(max_subarray([1,2,3], 2) == 5)
        assert (max_subarray([1, 4, 3, 10, 0, 1, 14], 3) == 17)