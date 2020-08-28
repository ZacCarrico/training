"""
multiply arrays that contain comma separated integers (eg. 123 would be [1,2,3] and if you multiplied
 that b [2], you would get  [2, 4, 6]
patterns used:
* `reversed(range(len(arr)))`
* `//` to get the quotient
* `%` to get the remainder
Lessons Learned:
* save what will be the products sign so that any negative doesn't interfere with addition
* create a zero filled array that is the sum of the length of the two inputs (max length of product array)
* use next to lazily remove leading zeroes from this array after the product has been added to the array
* you start filling the array at i + j + *1*. The +1 was unexpected, but comes about because the prod array is
  the sum of the length of the two input arrays
"""

import unittest


def multiply_arrays(arr1, arr2):
    prod_sign = -1 if arr1[0] > 0 ^ arr2[0] > 0 else 1
    arr1[0], arr2[0] = abs(arr1[0]), abs(arr2[0])
    prod = [0] * (len(arr1) + len(arr2))
    for i in reversed(range(len(arr1))):
        for j in reversed(range(len(arr2))):
            ij_prod = arr1[i] * arr2[j]
            prod[i + j + 1] += ij_prod
            prod[i + j] += prod[i + j + 1] // 10
            prod[i + j + 1] %= 10

    # removing any leading zeroes
    prod = prod[next((i for i,x in enumerate(prod) if x != 0), len(prod)):] or [0]

    # assigning sign to product
    prod[0] *= prod_sign
    return prod

class TestAddArrays(unittest.TestCase):
    def test_add_arrays(self):
        assert(multiply_arrays([1, 2, 3], [2]) == [2, 4, 6])
        print(multiply_arrays([1, 2, 3], [9, 9, 9]))
        assert(multiply_arrays([1, 2, 3], [9, 9, 9]) == [1,2,2,8,7,7])

if __name__ == "__main__":
    unittest.main()