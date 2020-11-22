"""
Pivot a linked-list around a value such that everything less than the value is before it and everything greater is after,
but don't change the order other this. (eg. f(4->9->5->1->6, pivot = 5) -> (4->1->5->9->6)
patterns:
* while loop to iterate through linked list
* to keep the head node, create a head node that equals iteration node first.
After the while loop, move the head to head.next.
Return the first head node.next
lessons learned:
* update three linked lists (before, pivot, and after) as you iterate through
* don't forget to end the while loop with node = node.next
"""

class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

def linked_list_pivot(node, pivot):
    before_head = before_node = Node(None)
    pivot_head = pivot_node = Node(None)
    after_head = after_node = Node(None)
    while node:
        if node.value < pivot:
            before_node.next = node
            before_node = before_node.next
        elif node.value > pivot:
            after_node.next = node
            after_node = after_node.next
        else:
            pivot_node.next = node
            pivot_node = pivot_node.next
        node = node.next
    before_node.next = pivot_head.next
    pivot_node.next = after_head.next
    after_node.next = None
    return before_head.next

def list_values_from_linked_list(node):
    values = []
    while node:
        values.append(node.value)
        node = node.next
    return values

def test_linked_list_pivot():
    result = linked_list_pivot(Node(4, Node(9, Node(5, Node(1, Node(6))))), 5)
    assert(list_values_from_linked_list(result) == [4,1,5,9,6])