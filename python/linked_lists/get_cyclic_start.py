# return the node that the cyclic portion of a linked-list starts on (eg. if A->B->C->D->E->C then C is the cyclic start node)
# lessons learned:
# * you need a graph (used a dict) for cyclic linked lists because you otherwise there's a recursive definition
import unittest

class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

def get_cyclic_start(root, graph):
    """If returns None then the linked list acyclic"""
    visited = []
    while root not in visited:
        visited.append(root)
        if root.next:
            root = graph[root.next]
        else:
            return None
    return root

class TestGetCyclicStart(unittest.TestCase):
    def test_get_cyclic_start(self):
        cyclic = {'A': Node('A', 'B'), 'B': Node('B', 'C'), 'C': Node('C', 'B')}
        acyclic = {'A': Node('A', 'B'), 'B': Node('B', 'C'), 'C': Node('C', None)}
        assert(get_cyclic_start(cyclic['A'], cyclic) == cyclic['B'])
        assert (get_cyclic_start(acyclic['A'], acyclic) is None)

if __name__ == "__main__":
    unittest.main()

