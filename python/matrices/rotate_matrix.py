# rotate a given matrix 90 degrees clockwise
# Lessons learned:
#  * You only rotate len(M[layer]) - 1 times for each layer. I originally made the mistake of rotating
#   len(M[layer]) times which caused the first rotation to be overwritten by the last
#  * Asserting that two matrices are equals fails for an unknown reason. You need ot iterate throuh each row
#  * sketch things out. It's easy to get confused


# plan
#  go layer by layer from the outside
#   swap relative positions

# things to watch out for
# be mindful of offset and layer

# edge cases
#  non-square matrix
import unittest


def rotate_matrix(M):
    if len(M) != len(M[0]):
        print("Can only accept square matrices")
        return
    for layer in range(int(len(M)/2)):
        # swap
        first = layer
        last = len(M) - layer - 1

        for i in range(first, last):
            # top
            top = M[first][i]

            # left -> top
            M[first][i] = M[last - i][first]

            # bottom -> left
            M[last-i][first] = M[last][last-i]

            # right -> bottom
            M[last][last - i] = M[i][last]

            # top -> right
            M[i][last] = top

    return M

class TestRotateMatrix(unittest.TestCase):
    def setUp(self):
        self.M = [[1,2,3], [4,5,6], [7,8,9]]

    def test_rotate_matrix(self):
        print(rotate_matrix(self.M))
        result = rotate_matrix(self.M)
        for i in range(len(self.M)):
            assert(self.M[i] == result[i])

if __name__ == "__main__":
    unittest.main()