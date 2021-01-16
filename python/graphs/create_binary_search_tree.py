"""
Create a function to create binary search trees from lists

patterns:
* if at the leaf, simply add the new node,
 but if not at a leaf, recurse down until a leaf is reached
 checking along the way whether the arg value < node.value

time complexity: O(n)
space complexity: O(n)
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class CreateBinarySearchTree:
    def __init__(self):
        self.visited_nodes = []

    def create_binary_search_tree(self, arr):
        root = Node(arr[0])
        for val in arr[1:]:
            self._add_node(root, val)
        return root

    def _add_node(self, root, val):
        if val <= root.val:
            if not root.left:
                root.left = Node(val)
            else:
                self._add_node(root.left, val)
        else:
            if not root.right:
                root.right = Node(val)
            else:
                self._add_node(root.right, val)


    def get_in_order_list(self, node):
        if node:
            self.get_in_order_list(node.left)
            self.visited_nodes.append(node.val)
            self.get_in_order_list(node.right)

def test_create_binary_search_tree():
    create_binary_search_tree = CreateBinarySearchTree()
    root = create_binary_search_tree.create_binary_search_tree([2, 1, 3, 0, 4])
    create_binary_search_tree.get_in_order_list(root)

    assert create_binary_search_tree.visited_nodes == [0, 1, 2, 3, 4]
