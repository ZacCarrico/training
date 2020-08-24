# create a binary search tree of shortest height from sorted array
# lessons learned:
# * manually checking that this was doing what I expected was the toughest part
import unittest

class Node:
    def __init__(self, label, left, right):
        self.label = label
        self.left = left
        self.right = right

def create_binary_search_tree(arr, start, end):
    if end < start:
        return None
    mid = (start + end)/2
    left = create_binary_search_tree(arr[start : mid - 1], start, mid - 1)
    right = create_binary_search_tree(arr[mid + 1 : end], mid + 1, end)
    return Node(mid, left, right)

class TestCreateBinarySearchTree(unittest.TestCase):

    def test_create_binary_search_tree(self):
        arr = [0]
        # this assertion is correct, but fails for a reason I don't understand
        assert(create_binary_search_tree(arr, 0, len(arr) - 1) == Node(0, None, None))


        arr = [0,1,2,3,4]
        # this assertion is correct, but fails for a reason I don't understand
        assert(create_binary_search_tree(arr, 0, len(arr) - 1) == Node(2, Node(0, None, Node(1, None, None)), Node(3, None, Node(4, None, None))))

if __name__ == "__main__":
    unittest.main()