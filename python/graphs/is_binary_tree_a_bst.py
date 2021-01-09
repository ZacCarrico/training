"""
function for determining if binary tree is a binary search tree
lessons learned:
* always make sure your base case and None case are well handled
* here are two ways to create this function:
1. using a global last_value variable and comparing node values (O(N) time, O(logN) space complexity b/c of recursion)
2. using a min/max approach (O(N) time, O(logN) space complexity b/c of recursion).
 This is the less intuitive approach to me
 * this is interesting because the min is None for the entire left branch traversal while the max shrinks,
   and the max is None for the entire right branch traversal while the min shrinks
"""
import unittest


class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

def is_binary_tree_bst(node):
    last_value = []
    def helper(node):
        if node == None: # base case for None
            return True
        if helper(node.left) == False:
            return False
        if last_value:
            if node.value < last_value.pop(): # base case for False
                return False
        last_value.append(node.value)
        if helper(node.right) == False:
            return False
        return True
    return helper(node)

def is_binary_tree_bst_using_min_max(node, min, max):
    if node == None: # base case for None
        return True
    if (min != None and min > node.value) or (max != None and max < node.value): # base case for False
        return False
    if not is_binary_tree_bst_using_min_max(node.left, min, node.value) or not is_binary_tree_bst_using_min_max(node.right, node.value, max):
        return False
    return True


class TestIsBinaryTreeBST(unittest.TestCase):
    def test_is_binary_tree_bst_(self):
        assert(is_binary_tree_bst(Node(1, Node(0, None, None), Node(2, None, None))) == True)
        assert (is_binary_tree_bst(Node(0, Node(1, None, None), Node(2, None, None))) == False)
        assert (is_binary_tree_bst_using_min_max(Node(1, Node(0, None, None), Node(2, None, None)), None, None) == True)
        assert (is_binary_tree_bst_using_min_max(Node(0, Node(1, None, None), Node(2, None, None)), None, None) == False)

if __name__ == "__main__":
    unittest.main()