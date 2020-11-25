"""
Purpose build a queue using only two stacks
patterns:
* while there's anything to pop, keep popping
lessons learned:
* you don't need to add to reorganize every time anything is added. You only need to do this once the dequeue stack is
empty
"""

class Queue:
    def __init__(self):
        self._enq = []
        self._deq = []

    def enqueue(self, value):
        self._enq.append(value)

    def dequeue(self):
        if not self._deq:
            while self._enq:
                self._deq.append(self._enq.pop())
        if self._deq:
            return self._deq.pop()

def test_dequeue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    assert 1 == queue.dequeue()
    assert 2 == queue.dequeue()
    assert None == queue.dequeue()