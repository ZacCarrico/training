"""
The Dutch Flag problem is a sorting problem given 3 categories. For example, sort [2,1,0,0,2,1] -> [0,0,1,1,2,2]
It can be used to sort any tri-category
pattern:
* multiple pointers
lessons learned:
* when writing the function, first write the return statement, otherwise you may make the dumb mistake of not returning anything
* when arr[mid] > arr[high], you only decrement high after swapping
* when arr[mid] < arr[low], you increment both low and mid after swapping
"""
import unittest


def trisort(arr, low_cat, mid_cat, high_cat):
    low, mid = 0, 0
    high = len(arr) - 1
    while mid <= high:
        if arr[mid] == high_cat:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
        elif arr[mid] == low_cat:
            arr[mid], arr[low] = arr[low], arr[mid]
            low += 1
            mid += 1
        elif arr[mid] == mid_cat:
            mid += 1
    return arr

class TestTrisort(unittest.TestCase):
    def test_trisort(self):
        assert(trisort([2,0,0,1,2,1], 0, 1, 2) == [0,0,1,1,2,2])

if __name__ == "__main__":
    unittest.main()