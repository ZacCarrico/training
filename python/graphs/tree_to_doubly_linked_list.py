"""
Create a doubly-linked list from a tree.
For a tree like this
    1
  2   3
 4 5 6 7
the doubly linked list would be:
None <- 4 <-> 2 <-> 5 <-> 1 <-> 6 <-> 3 <-> 7 ->
# note that only 4 and 7 have None pointers because
 they are the first and last node for in-order traversal

patterns:
* in-order traversal
* if there is no previous node, set the head to the current node
* set previous.next to current node in traversal
* set the current.prev to previous node

runtime/spacetime:
O(n)/O(n)
"""

class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class CreateDoublyLinkedListFromBinaryTree:
    prev = None
    head = None

    def create_doubly_linked_list_from_binary_tree(self, node: Node) -> Node:
        if not node:
            return None
        self.create_doubly_linked_list_from_binary_tree(node.left)
        if self.prev == None:
            self.head = node
        else:
            self.prev.right = node
            node.left = self.prev
        self.prev = node
        self.create_doubly_linked_list_from_binary_tree(node.right)
        return self.head

def list_from_linked_list(node: Node) -> list:
    l = []
    while node:
        l.append(node.val)
        node = node.right
    return l

def test_CreateDoublyLinkedListFromBinaryTree():
    root = Node(
        1,
        Node(2, Node(4), Node(5)),
        Node(3, Node(6), Node(7))
    )
    head = CreateDoublyLinkedListFromBinaryTree().create_doubly_linked_list_from_binary_tree(root)
    assert list_from_linked_list(head) == [4, 2, 5, 1, 6, 3, 7]