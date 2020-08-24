# create a list for each level of a binary search tree
# lessons learned:
# * you need to pass a list of lists, but otherwise can use BFS or DFS
import unittest


class Node:
    def __init__(self, label, left, right):
        self.label = label
        self.left = left
        self.right = right

def create_graph_level_lists_using_DFS(root, lists, level):
    if not root:
        return
    if len(lists) == level:
        list = []
        lists.append(list)
    else:
        list = lists[level]
    list.append(root)
    create_graph_level_lists_using_DFS(root.left, lists, level + 1)
    create_graph_level_lists_using_DFS(root.right, lists, level + 1)

def create_graph_level_lists_using_BFS(root):
    current = []
    level_lists = []
    current.append(root)
    while current:
        print([node.label for node in current if node])
        level_lists.append(current)
        parent = current
        current = []
        for node in parent:
            if node:
                if node.left:
                    current.append(node.left)
                if node.right:
                    current.append(node.right)
        if not current:
            return level_lists


class TestCreateGraphLevelLists(unittest.TestCase):

    def test_create_graph_level_lists_using_DFS(self):
        # could have created these nodes in setUp, but didn't want to have to write self all the time
        D = Node('D', None, None)
        C = Node('C', None, None)
        B = Node('B', D, None)
        A = Node('A', B, C)
        lists = []
        create_graph_level_lists_using_DFS(A, lists, 0)
        assert(lists == [[A], [B, C], [D]])

    def test_create_graph_level_lists_using_BFS(self):
        # could have created these nodes in setUp, but didn't want to have to write self all the time
        D = Node('D', None, None)
        C = Node('C', None, None)
        B = Node('B', D, None)
        A = Node('A', B, C)
        assert(create_graph_level_lists_using_BFS(A) == [[A], [B, C], [D]])

if __name__ == "__main__":
    unittest.main()