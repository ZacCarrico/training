# Answers the question of whether two nodes are connected in a graph
# lessons learned:
# * when creating a graph from connections you need to leave the adjacent nodes as their string labels
#   because if A.adjacent = B, and B.adjacent = A, you can't say A.adjacent = Node(B, adjacent=A) because you're
#   self referencing. You could go through the entire dictionary if things are in the correct order and swap, but I just
#   created the nodes with string labels
# * use BFS

import unittest
from collections import deque, defaultdict


class Node:
    def __init__(self, label, adjacent, visited = False):
        self.label = label
        self.adjacent = adjacent
        self.visited = visited

class Graph(object):
    def __init__(self, connections, directed=False):
        self.connections = connections
        self.nodes = self.create_graph_from_connections()

    def create_graph_from_connections(self):
        graph = defaultdict()
        for label, adj_labels in self.connections.items():
            graph[label] = Node(label, adj_labels)
        return graph

def are_two_nodes_connected(graph, nodeA_label, nodeB_label):
    queue = deque()
    queue.append(graph.nodes[nodeA_label])
    while queue:
        node = queue.popleft()
        node.visited = True
        for adj_node in [graph.nodes[_] for _ in node.adjacent]:
            if adj_node == graph.nodes[nodeB_label]:
                return True
            if not adj_node.visited:
                queue.append(adj_node)
    return False


class TestAreTwoNodesConnected(unittest.TestCase):
    def setUp(self):
        # this graph is meant to be used for a directed graph, but for this use case I will ignore this
        # taken from https://www.python.org/doc/essays/graphs/
        graph_connections = {'A': ['B', 'C'],
                      'B': ['A', 'C', 'D'],
                      'C': ['B', 'D', 'F'],
                      'D': ['B', 'C'],
                      'E': ['F'],
                      'F': ['E', 'C'],
                      'G': []}
        self.graph = Graph(graph_connections)

    def test_are_two_nodes_connected(self):
        assert(are_two_nodes_connected(self.graph, 'A', 'B') == True)
        assert (are_two_nodes_connected(self.graph, 'A', 'F') == True)
        assert(are_two_nodes_connected(self.graph, 'A', 'G') == False)

if __name__ == "__main__":
    unittest.main()