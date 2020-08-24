# given an array, return it such that L[0]<=L[1]>=L[2]<=L[3]>=L[4]...; eg. [9, 2, 3, -1, 4] -> [2, 9, -1, 4, 3]
# lessons learned:
# * there are multiple ways to do this (eg. interleaving the first and last half of a sorted list),
#  but only one very efficient way to do this. To see the non-intuitive way, you need to realize that
#  the larger index values are always odd and that you only need to focus on two index values a time
import unittest


def low_high_low(arr):
    for i in range(len(arr)):
        arr[i:i+2] = sorted(arr[i:i+2], reverse = bool(i%2))
    print(arr)
    return arr

class TestLowHighLow(unittest.TestCase):
    def test_low_High_low(self):
        assert(low_high_low([9, 2, 3, -1, 4]) == [2, 9, -1, 4, 3])

if __name__ == "__main__":
    unittest.main()