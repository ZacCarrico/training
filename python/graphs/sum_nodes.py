"""
Sum nodes in a graph

patterns:
* depth first search

lessons learned:
* for recursion, you don't want to use the total (or whatever cumulative argument) as a function parameter
"""
import unittest

class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def dfs_sum(head):
    if not head:
        return 0
    return head.value + dfs_sum(head.left) + dfs_sum(head.right)

class TestDfsSum(unittest.TestCase):
    def test_dfs_sum(self):
        assert(dfs_sum(Node(3, left = Node(1, left = Node(0), right = Node(2)), right = Node(5, left = Node(4)))) == 15)

if __name__ == "__main__":
    unittest.main()
