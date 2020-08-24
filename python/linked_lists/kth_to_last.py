# create a function to return the kth to last node in a linked list
# lessons learned:
# * the iterative solution makes much more sense to me and doesn't require extra function parameters
# * the shorter, but more space intensive solution is recursion: O(N) time, O(N) space
# * For the recursive solution:
#  *  you need to pass both the kth_node and counter
#  *  you need to start the counter at -1
# * For the iterative solution: O(N) time, O(1) space
#  * have a two-runner system with one runner k ahead of the other
import unittest


class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

# recursive solution
def get_kth_to_last_node_recursively(node, k, counter = -1, kth_node = None):
    if node:
        kth_node, counter = get_kth_to_last_node_recursively(node.next, k, counter, kth_node)
        counter += 1
        if counter == k:
            return node, counter
    return kth_node, counter

def get_kth_to_last_node_iteratively(node, k):
    leader, follower = node, node
    for _ in range(k):
        if leader:
            leader = leader.next
        else:
            return "k is too large for list"

    while leader.next:
        leader = leader.next
        follower = follower.next

    return follower.value




class TestGetKthToLastNode(unittest.TestCase):
    def test_get_kth_to_last_node_recursively(self):
        node = Node('a', Node('b', Node('c', None)))
        assert (get_kth_to_last_node_recursively(node, 0)[0].value == 'c')
        assert(get_kth_to_last_node_recursively(node, 1)[0].value == 'b')
        assert (get_kth_to_last_node_recursively(node, 2)[0].value == 'a')

    def test_get_kth_to_last_node_iteratively(self):
        node = Node('a', Node('b', Node('c', None)))
        assert (get_kth_to_last_node_iteratively(node, 0) == 'c')
        assert(get_kth_to_last_node_iteratively(node, 1) == 'b')
        assert (get_kth_to_last_node_iteratively(node, 2) == 'a')

if __name__ == "__main__":
    unittest.main()