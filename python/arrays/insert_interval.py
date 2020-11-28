"""
insert an interval [start, end] into a sorted list of intervals
eg. insert_interval(arr = [[1,3], [5,8]], [2,6]) -> [[1,8]]
patterns:
* a for loop with many if conditionals
* a snowball interval, that can include overlapping intervals

lessons learned:
* the final elif operates on those that didn't match the initial if clauses, which means you can safely use
 (new_interval[0] <= interval[1]) or (new_interval[0] >= interval[0]). Using this without the prior if
 clauses wouldn't have worked.
* create a new interval list rather than trying to modify the input interval list
"""
import unittest


def insert_interval(intervals, new_interval) -> list:
    result = []
    for interval in intervals:
        if new_interval[0] > interval[1]:
            result.append(interval)
        elif new_interval[1] < interval[0]:
            result.append(new_interval)
            new_interval = interval
        elif (new_interval[0] <= interval[1]) or (new_interval[0] >= interval[0]):
            new_interval = [min(new_interval[0], interval[0]), max(new_interval[1], interval[1])]
    result.append(new_interval)
    return result

class TestInsertInterval(unittest.TestCase):
    def test_insert_interval(self):
        assert(insert_interval([[1,3], [5,8]], [2,6]) == [[1,8]])
        assert (insert_interval([[-1, 0], [1, 3], [5, 8], [20,40]], [2, 21]) == [[-1, 0], [1, 40]])

if __name__ == "__main__":
    unittest.main()
