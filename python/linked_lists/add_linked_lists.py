"""
Add linked lists
eg. If the numbers 413 and 678 were put into linked lists they would look like this 3->1->4 adn 8->7->6
Add these two to get 1091 (1->9->0->1)

patterns:
* while loop to iterate through nodes
* using another while loop to collect values for testing
* for iteration: node.next if node else None
* for summing: node.next if node else 0
* collect the value that will be carried with floor division (//)
* once the remainder is calculated, assign sum_head.next to it, then move sum_head to sum_head.next

lessons learned:
This problem is full of goodies
* don't forget to keep the while loop running if there's a `carry` value
* to instantiate the sum_head before the while loop, you can set it the first node to None, but
this means you need to make the sum head equal to a dummy head so that you can return dummy_head.next
"""
class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

def add_linked_lists(ll1, ll2):
    carry = 0
    sum_head = dummy_head = Node(None)
    while ll1 or ll2 or carry:
        sum = (ll1.value if ll1 else 0) + (ll2.value if ll2 else 0) + carry
        carry = sum // 10
        sum_head.next = Node(sum % 10)
        sum_head = sum_head.next
        ll1 = ll1.next if ll1 else None
        ll2 = ll2.next if ll2 else None
    return dummy_head.next

def get_linked_list_values(node):
    linked_list_values = []
    while node:
        if node.value != None:
            linked_list_values.append(node.value)
        node = node.next

    return linked_list_values

def test_add_linked_list():
    sum = add_linked_lists(
        Node(3, Node(1, Node(4))),
        Node(8, Node(7, Node(6)))
    )
    get_linked_list_values(sum)
    assert get_linked_list_values(sum) == [1,9,0,1]