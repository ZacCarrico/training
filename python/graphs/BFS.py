# create and test breadth first search alg
# lessons learned:
# * use a queue (deque "deck" in the case of util)
# * deque is unintuitive for a queue because rather than append and pop, you need to use appendleft and pop (which pops from the right)
# * don't forget to mark visited as True once a node has been visited to find its adjacent nodes
# * the steps are root -> appendleft -> while queue -> popleft -> flag visited instance variable as True -> append adjacent nodes
import unittest
from collections import deque

class Node:
    def __init__(self):
        self.adjacent = None
        self.visited = False
        self.label = None

def bfs(root):
    q = deque()
    q.append(root)
    while q:
        node = q.pop()
        if not node.visited:
            node.visited = True
            print(node.label)
            if node.adjacent:
                for n in node.adjacent:
                    q.appendleft(n) # need to use appendleft because pop() removes from right. This way it's FIFO

class TestBfs(unittest.TestCase):
    def setUp(self):
        self.root = Node()
        self.root.label = "root"
        a = Node()
        a.label="a"
        b = Node()
        b.label="b"
        a1 = Node()
        a1.adjacent = [self.root] # making it cyclic so that if the visited flag pattern fails, it will run infinitely
        a1.label="a1"
        a2 = Node()
        a2.label="a2"
        a.adjacent = [a1,a2]

        self.root.adjacent = [a,b]

    def test_bfs(self):
        bfs(self.root)

if __name__ == "__main__":
    unittest.main()