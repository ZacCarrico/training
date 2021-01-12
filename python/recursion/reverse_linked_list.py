"""
reverse a linked list recursively
compare time and space of recursive vs iterative approaches

patterns:
* base case is when the argument or node.next is None
* the node's next.next is pointed to itself (making it cyclical),
 and then it's next is set to None (breaking the cycle)
* node1 is returned because that is the last node before
 reaching the base case

 recursive approach:
 time and space are O(n)

 iterative approach:
 time is O(n)
 space is O(1)
"""

class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

def reverse_linked_list(node):
    if not node or not node.next:
        return node
    node1 = reverse_linked_list(node.next)
    node.next.next = node
    node.next = None
    return node1

def get_linked_list_values(node):
    linked_list_values = []
    while node:
        linked_list_values.append(node.value)
        print(node.value)
        node = node.next
    return linked_list_values

def test_reverse_linked_list():
    TEST_LINKED_LIST = Node(0, Node(1, Node(2, None)))
    head = reverse_linked_list(TEST_LINKED_LIST)
    assert (get_linked_list_values(head) == [2, 1, 0])