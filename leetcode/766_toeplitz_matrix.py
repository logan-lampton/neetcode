# Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.
#
# A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.
#
#
#
# Example 1:
# Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
# Output: true
# Explanation:
# In the above grid, the diagonals are:
# "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
# In each diagonal all elements are the same, so the answer is True.

class Solution(object):
    def isToeplitzMatrix(self, matrix):

        # enumerate matrix to have both the indexes and rows
        for i, row in enumerate(matrix):
            # look at the numbers in each row
            for num in range(len(row) - 1):
                # make sure that we don't get an index error, so make sure the index is 1 less than the len of
                # the matrix
                if i < len(matrix) -1:
                    # compare the numbers to their diagonals
                    if row[num] != matrix[i + 1][num + 1]:
                        return False
        return True
