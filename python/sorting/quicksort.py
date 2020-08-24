# quicksort
# lessons learned:
# * i becomes -1 for the first partition
# * the action isn't at the pivot, it's between j and i. They are indexes at which values are swapped.
#  The pivot is just there for comparison
# * the penultimate step of the partition is to swap the pivot with the value at index i + 1
# * i + 1 is returned as the pivot index from partition
import unittest


def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quicksort(arr, low, high):
    if arr == 1:
        return arr
    if low < high:
        pivot = partition(arr, low, high)

        # sort left
        quicksort(arr, low, pivot - 1)
        quicksort(arr, pivot + 1, high)

class TestQuicksort(unittest.TestCase):
    def test_quicksort(self):
        arr = [1,8,3,9,4,5,7]
        quicksort(arr, 0, len(arr) - 1)
        print(arr)
        assert(arr == sorted(arr))

if __name__ == "__main__":
    unittest.main()