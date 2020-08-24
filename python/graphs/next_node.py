# a function that finds the next node in an in-order traversal of a binary search tree
# assumes node has parent information
# lessons learned:
# * very tricky problem
# * requires two functions
# * starts by looking for left most child of the node.right (if it exists). This makes sense b/c
#  in-order traversal goes most left -> most recent parent node -> right, so wherever you are the only next places to go are
#  to the left most child of the right if you're already at the most recent parent node, and then if there isn't a node.right
#  to go to the most recent parent node
# * finding the most recent parent node is tricky too. If parent.left == node star on then you're there, but if it doesn't you
#  need to keep climbing back up the tree until parent.left does equal the node you were just on
import unittest
from collections import namedtuple


class Node:
    def __init__(self, value, left, right, parent = None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

def left_most_child(node):
    if not node:
        return None
    while node.left:
        node = node.left
    return node

def next_node(node):
    """:return next node in-order traversal of binary search tree"""
    if node.right:
        return left_most_child(node.right)
    else:
        past_node = node
        node = node.parent
        # go up until node.left != past_node, which means it's reach a branch node
        while node and node.left != past_node:
            past_node = node
            node = node.parent
        return node

class TestNextNode(unittest.TestCase):
    def test_next_node(self):
        # this could be used to allow the Node's parent variable to be used, but because it makes
        #  the function more difficult to read, more thorough testing will not be done
        # Node = namedtuple('Node', ['left', 'right', 'parent'])
        # bst = {'root': Node('left', 'right', None),
        #        'left': Node(None, None, 'root'),
        #        'right': Node(None, None, 'root')}


        left = Node("left", None, None)
        right = Node("right", None, None)
        root = Node("root", left, right)
        # doesn't test node.parent path
        assert(next_node(root) == right)

if __name__ == "__main__":
    unittest.main()