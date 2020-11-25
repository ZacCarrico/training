"""
Given a binary tree, return a list of lists, where each list is all the values at a given depth of a binary tree.
Example: If a binary tree has a root of 1, at depth 1 there are values [2,3,4,5] and at depth 2 [6,7,8,9] then the result
would be [[1], [2,3], [4,5,6,7]]
patterns:
* while node exists
* the children replace the parents (children nodes become the parent nodes) for the list comprehension solution
"""

def get_nodes_at_each_depth_of_BT(node):
    result = []
    if not node:
        return result
    curr_depth_nodes = [node]
    while curr_depth_nodes:
        result.append([curr.value for curr in curr_depth_nodes])
        new_curr_depth_nodes = []
        for node in curr_depth_nodes:
            for child in (node.left, node.right):
                if child:
                    new_curr_depth_nodes.append(child)
        curr_depth_nodes = new_curr_depth_nodes
    return result

# just for the purpose of showing the solution using list comprehension
def get_nodes_at_each_depth_of_BT_list_comprehension(node):
    result = []
    if not node:
        return result
    curr_depth_nodes = [node]
    while curr_depth_nodes:
        result.append([curr.value for curr in curr_depth_nodes])
        curr_depth_nodes = [
            child for node in curr_depth_nodes
            for child in (node.left, node.right)
            if child
        ]
    return result

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def test_get_nodes_at_each_depth_of_BT():
    tree = Node(0, Node(1, Node(2), Node(3)), Node(4, Node(5), Node(6)))
    assert(get_nodes_at_each_depth_of_BT(tree) == [[0], [1,4], [2,3,5,6]])
    assert (get_nodes_at_each_depth_of_BT_list_comprehension(tree) == [[0], [1, 4], [2, 3, 5, 6]])

test_get_nodes_at_each_depth_of_BT()