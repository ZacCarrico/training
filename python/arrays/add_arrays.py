# add arrays that contain comma separated integers (eg. 123 would be [1,2,3] and if you added that to [9], you would get  [1, 3, 2]
# patterns used:
# * `reversed(range(len(arr)))`
# * `/` to get the quotient
# * `%` to get the remainder
# `insert`
# lessons learned:
# * add zeroes to the front of the shorter array to make things easy for adding
import unittest


def add_arrays(arr1, arr2):
    # making it so that arr1 is always the smaller of the two
    if len(arr1) > len(arr2):
        arr1, arr2 = arr2, arr1
    for _ in range(len(arr2)-len(arr1)):
        arr1.insert(0, 0)
    a = 0
    for i in reversed(range(len(arr2))):
        total = arr1[i] + arr2[i] + a
        if total >= 10:
            a = int(total / 10)
            arr2[i] = total % 10
        else:
            arr2[i] = total
            a = 0
    if a:
        arr2.insert(0, a)
    return arr2

class TestAddArrays(unittest.TestCase):
    def test_add_arrays(self):
        print(add_arrays([1,2,3], [9]))
        assert(add_arrays([1,2,3], [9]) == [1,3,2])
        assert (add_arrays([9, 9, 9], [1]) == [1, 0, 0, 0])
        assert (add_arrays([9, 9, 9], [1, 1, 1]) == [1, 1, 1, 0])

if __name__ == "__main__":
    unittest.main()