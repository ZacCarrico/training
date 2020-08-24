# if there is a zero in a matrix, set the matrix's entire row and column to zero for that index
# plan:
# go through the matrix and record where the zeros are
# change the rows and columns of the matrix to zero where they are

# time: O(N^2), space: O(N)
# Lessons learned:
#  you can' use M[:][1] = 0 to set all rows in col 1 to zero
import unittest

def matrix_indices_to_zero(M):
    zero_rows = []
    zero_cols = []

    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[i][j] == 0:
                zero_rows.append(i)
                zero_cols.append(j)

    for row in zero_rows:
        for col in range(len(M[0])):
            M[row][col] = 0

    for col in zero_cols:
        for row in range(len(M)):
            M[row][col] = 0

    return M

class TestMatrixIndecesToZero(unittest.TestCase):
    def setUp(self) -> None:
        self.M = [[1,2,3], [4,0,6],[7,8,9]]
    def test_matrix_indeces_to_zero(self):
        assert(matrix_indices_to_zero(self.M) == [[1,0,3], [0,0,0],[7,0,9]])

if __name__ == "__main__":
    unittest.main()
