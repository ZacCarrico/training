# create a set of stacks data structure that has a limit to the size of the stacks, and once that limit is exceeded
# a new stack is created
# it should have pop and add methods
# lessons learned: none. This was strait-forward
import unittest


class Node:
    def __init__(self, arr, prev, next = None):
        self.arr = arr
        self.prev = prev
        self.next = next


class SetOfStacks:
    def __init__(self, limit, arr = []):
        if limit < len(arr):
            raise Exception("array > limit")
        self.limit = limit
        self.root = Node(arr, None, None)
        self.current_node = self.get_last_node(self.root)

    def add(self, value):
        if len(self.current_node.arr) < self.limit:
            self.current_node.arr.append(value)
        else:
            self.current_node.next = Node([value], self.current_node, None)
            self.current_node = self.current_node.next
            print(self.current_node.arr)

    def pop(self):
        if self.current_node.arr:
            self.current_node.arr.pop()
        if not self.current_node.arr:
            self.current_node = self.current_node.prev

    def get_last_node(self, root):
        while root.next:
            root = root.next
        return root

class TestSetOfStacks(unittest.TestCase):
    def setUp(self) -> None:
        self.limit = 3

    def test_set_of_stacks_add_below_limit(self):
        stacks = SetOfStacks(self.limit, [1,2])
        stacks.add(3)
        self.assertEqual(stacks.current_node.arr, SetOfStacks(self.limit, [1,2,3]).current_node.arr)

    def test_set_of_stacks_add_above_limit(self):
        stacks = SetOfStacks(self.limit, [1,2,3])
        stacks.add(4)
        self.assertEqual(stacks.current_node.arr, [4])

    def test_set_of_stacks_pop(self):
        stacks = SetOfStacks(self.limit, [1,2,3])
        stacks.add(4)
        stacks.pop()
        self.assertEqual(stacks.current_node.arr, [1,2,3])

if __name__ == "__main__":
    unittest.main()

