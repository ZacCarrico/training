# fn for determining if binary tree is a binary search tree
# lessons learned:
# * always make sure your base case and None case are well handled
# * there are two ways to do this:
# 1. using a global last_value variable and comparing node values (O(N) time, O(logN) space complexity b/c of recursion)
#  * you only need one if check to see if the current value is less than the last value
#  * it's an in-order traversal with the check for sortedness between descending the left and right
#  * this only works if there aren't duplicate values
# 2. using a min/max approach (O(N) time, O(logN) space complexity b/c of recursion)
#  * this is interesting because the min is None for the entire left branch traversal while the max shrinks,
#    and the max is None for the entire right branch traversal while the min shrinks

import unittest


class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

last_value = None
def is_binary_tree_bst_using_global_var(node):
    global last_value
    if node == None: # base case for None
        return True
    if is_binary_tree_bst_using_global_var(node.left) == False:
        return False
    if node.value < last_value: # base case for False
        return False
    last_value = node.value
    if is_binary_tree_bst_using_global_var(node.right) == False:
        return False
    return True

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
        assert(is_binary_tree_bst_using_global_var(Node(1, Node(0, None, None), Node(2, None, None))) == True)
        assert (is_binary_tree_bst_using_global_var(Node(0, Node(1, None, None), Node(2, None, None))) == False)
        assert (is_binary_tree_bst_using_min_max(Node(1, Node(0, None, None), Node(2, None, None)), None, None) == True)
        assert (is_binary_tree_bst_using_min_max(Node(0, Node(1, None, None), Node(2, None, None)), None, None) == False)

if __name__ == "__main__":
    unittest.main()