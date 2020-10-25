"""
Problem: return True if linked list is a palindrome or False if not
pattern:
* slow and fast pointer
* while loop to iterate over head before None
* find the mid-point with a fast and slow pointer
lessons learned:
* the most elegant way requires reversing the linked list (easier to understand how this works if you draw out the steps)
* to make this work with odd numbered linked lists, a check must be added for None during the "fast" head iteration
* both finding the mid-point and checking that the values are palindromic are simple while loops to check for end of linked list
"""

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

def is_linked_list_palindrome(head: Node) -> bool:
    slow = head
    fast = head

    while slow and fast:
        slow = slow.next
        if fast.next:
            fast = fast.next.next

    reversed_head = reverse_linked_list(slow)

    while head and reversed_head:
        if head.value != reversed_head.value:
            return False
        head, reversed_head = head.next, reversed_head.next

    return True

def test_is_linked_list_palindrome():
    assert is_linked_list_palindrome(Node(0,Node(1,Node(2,Node(2,Node(1,Node(0, None))))))) == True
    assert is_linked_list_palindrome(Node(0, Node(1, Node(2, Node(1, Node(0, None)))))) == True
    assert is_linked_list_palindrome(Node(0,Node(1,Node(3,Node(2,Node(1,Node(0, None))))))) == False

