"""
reverse stack iteratively and recursively

patterns:
* inner helper function using outer function's list
* while loop and popping

time/space complexity
recursive: O(n) for both
iterative: O(n) for both
"""

def reverse_stack_recursively(stack: list) -> list:
    reversed_stack = []
    def helper(stack: list) -> None:
        if not stack:
            return None
        reversed_stack.append(stack.pop())
        helper(stack)
    helper(stack)
    return reversed_stack

def test_reverse_stack_recursively():
    assert reverse_stack_recursively([1,2,3]) == [3,2,1]

def reverse_stack_iteratively(stack: list) -> list:
    reversed_stack = []
    while stack:
        reversed_stack.append(stack.pop())
    return reversed_stack

def test_reverse_stack_iteratively():
    assert reverse_stack_iteratively([1,2,3]) == [3,2,1]