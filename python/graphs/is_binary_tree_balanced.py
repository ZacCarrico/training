# return true if binary tree is balanced. Balanced in this case if the max height of any branch more than 1 larger
#  than any other branch
# lessons learned:
# * the get_height fn will be recursed so you need a separate boolean return function to evaluate whether the tree is balanced
# * just after each recursive call there needs to be a check for whether that call returned a greater than 1 delta result
# * -1 is used if the input node is None. This way, when node.left - node.right of a leaf node is calculated, the
#   returned height will be -1 - -1 = 1
# * the function testing for whether the tree is balanced doesn't compare the difference in heights of left and right to 1,
#   but instead checks to make sure that the get_height function isn't returning GT1
import unittest

class Node:
    def __init__(self, label, left, right):
        self.label = label
        self.left = left
        self.right = right

GT1 = "greater than 1 diff"

def get_height(root):
    if root == None:
        return -1

    left_height = get_height(root.left)
    if left_height == GT1:
        return GT1

    right_height = get_height(root.right)
    if right_height  == GT1:
        return GT1

    if (abs(right_height - left_height)) > 1:
        return GT1
    else:
        return max(right_height, left_height) + 1

def is_binary_tree_balanced(root):
    return get_height(root) != GT1

class TestIsBinaryTreeBalanced(unittest.TestCase):
    def test_is_binary_tree_balanced(self):
        assert (is_binary_tree_balanced(
            Node(2, Node(0, None, Node(1, None, None)), Node(3, None, Node(4, None, None)))) == True)
        assert (is_binary_tree_balanced(
            Node(2, Node(0, Node(-1, None, None), Node(1, None, None)), None)) == False)

if __name__ == "__main__":
    unittest.main()