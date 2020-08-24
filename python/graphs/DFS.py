# create depth-first search alg
import unittest


class Node:
    def __init__(self, label, left, right):
        self.label = label
        self.left = left
        self.right = right
        self.visited = False

def DFS(node):
    if node == None:
        return
    if node.visited == True:
        return
    node.visited = True
    DFS(node.left)
    DFS(node.right)
    return node

class TestDFS(unittest.TestCase):

    def test_DFS(self):
        D = Node('D', None, None)
        C = Node('C', None, None)
        B = Node('B', D, None)
        A = Node('A', B, C)
        DFS(A)
        assert(D.visited==True)

if __name__ == "__main__":
    unittest.main()