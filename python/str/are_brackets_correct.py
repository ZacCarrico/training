# return True if the brackets are used correctly and False if not
# eg. "([])" -> True
# eg. "([)]" -> False
# lessons learned:
# * use a stack
# * popping makes it easier for the final return to check that all the brackets are matched (ie 'not left_chars')
# * remember to check for whether you're trying to add a right bracket before any left bracket (ie 'not left_chars')
import unittest


def are_brackets_correct(s):
    left_chars = []
    lookup = {'(': ')', '[': ']'}
    for c in s:
        if c in lookup:
            left_chars.append(c)
        elif not left_chars or lookup[left_chars.pop()] != c:
            return False
    return not left_chars

class TestAreBracketsCorrect(unittest.TestCase):
    def test_are_brackets_correct(self):
        assert(are_brackets_correct("([])") == True)
        assert (are_brackets_correct("([)]") == False)

if __name__ == "__main__":
    unittest.main()