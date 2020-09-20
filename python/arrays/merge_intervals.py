"""
Merge intervals, eg. [[1,3], [2, 6], [3,5], [8, 12], [15, 21], [22, 25], [28, 40], [30,35]] -> [[1,6], [8, 12], [15, 21], [22, 25], [28, 40]]
We're not assuming exclusivity, which means that [[15, 21], [22, 25]] does not get merged into [15, 25]
patterns:
* stack
* need a new array because you can't delete existing elements while iterating
* take max of end of interval

lessons learned:
* take max of end of interval

time, space complexity
O(n), O(n)
"""
import unittest


def merge_intervals(arr):
    arr.sort()
    if not arr:
        return None
    if len(arr) == 1:
        return arr
    merged_arr = []
    merged_arr.append(arr[0])
    for interval in arr[1:]:
        top = merged_arr[-1]
        if top[1] > interval[0]:
            top[1] = max(top[1], interval[1])
            merged_arr[-1] = top
        else:
            merged_arr.append(interval)
    return merged_arr

class TestMergeIntervals(unittest.TestCase):
    def test_merge_intervals(self):
        assert(merge_intervals([[1,3], [2, 6], [3,5], [8, 12], [15, 21], [22, 25], [28, 40], [30,35], [42, 45], [44, 46]]) == [[1,6], [8, 12], [15, 21], [22, 25], [28, 40], [42, 46]])

if __name__ == "__main__":
    unittest.main()
