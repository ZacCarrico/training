# return triplets that sum to zero
# lessons learned:
# * the tricky part is not returning duplicate triplets (sets aren't appropriate, but sorted lists work) and -1 and +1 changes to i and j
import unittest


def get_triplets_that_sum_to_zero(arr):
    triplets = []
    for i in range(len(arr) - 1):
        for j in range(i+1,len(arr)):
            if -(arr[i] + arr[j]) in arr[:i] + arr[j+1:]:
                triplet = sorted([-(arr[i] + arr[j]), arr[i], arr[j]])
                if triplet not in triplets:
                    triplets.append(triplet)
    return triplets

class TestGetTripletsThatSumToZero(unittest.TestCase):
    def test_get_triplets_that_sum_to_zero(self):
        assert(get_triplets_that_sum_to_zero([1,2,-3,10,20,-10,0]) == [[-3, 1, 2], [-10, 0, 10]])

if __name__ == "__main__":
    unittest.main()