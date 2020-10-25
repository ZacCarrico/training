"""
Reverse a linked list.
pattern: reassign location of pointers as you go in a stone hopping fashion. First move one, reassign, then move another pointer
Lessons learned: this requires seeing in "motion". Once you write it out several times it will click
"""
import unittest


class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next


def reverse_linked_list(head: Node) -> Node:
    previous = None
    tail = None

    while head:
        next = head.next
        head.next = previous
        previous = head
        head = next
        if head:
            tail = head

    return tail


def get_linked_list_values(node):
    linked_list_values = []
    while node:
        linked_list_values.append(node.value)
        print(node.value)
        node = node.next

    return linked_list_values

class TestReverseLinkedList(unittest.TestCase):
    def test_reverse_linked_list(self):
        TEST_LINKED_LIST = Node(0, Node(1, Node(2, None)))
        head = reverse_linked_list(TEST_LINKED_LIST)
        assert(get_linked_list_values(head) == [2,1,0])

if __name__ == "__main__":
    unittest.main()
