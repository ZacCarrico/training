# sort a stack using one other stack, but no other data structures
# lessons learned:
# * requires a nested while loop, thus O(N^2)
# * the nested while loop is non-intuitive b/c it makes the first attempted step moving things from the temporary stack
#  rather than making the first attempted step moving things from the primary stack to the temporary stack

def sort_stack(stack):
    tmp_stack = []
    while stack:
        tmp = stack.pop()
        while tmp_stack and tmp_stack[-1] > tmp:
            stack.append(tmp_stack.pop())
        tmp_stack.append(tmp)

    while tmp_stack:
        stack.append(tmp_stack.pop())

class TestSortStack(unittest.TestCase)