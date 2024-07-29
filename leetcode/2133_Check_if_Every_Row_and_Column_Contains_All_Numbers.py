# An n x n matrix is valid if every row and every column contains all the integers from 1 to n (inclusive).

# Given an n x n integer matrix matrix, return true if the matrix is valid. Otherwise, return false.

# Example 1:
# Input: matrix = [[1,2,3],[3,1,2],[2,3,1]]
# Output: true
# Explanation: In this case, n = 3, and every row and column contains the numbers 1, 2, and 3.
# Hence, we return true.

# Example 2:
# Input: matrix = [[1,1,1],[1,2,3],[1,2,3]]
# Output: false
# Explanation: In this case, n = 3, but the first row and the first column do not contain the numbers 2 or 3.
# Hence, we return false.

# Constraints:
# n == matrix.length == matrix[i].length
# 1 <= n <= 100
# 1 <= matrix[i][j] <= n

class Solution:
    def checkValid(self, matrix: [[int]]) -> bool:
        if len(matrix) == 1:
            return True
            
        for i in range(len(matrix)):
            sorted_row = sorted(matrix[i])
            var = 0
            if var < len(sorted_row):
                if sorted_row[var] + 1 != sorted_row[var + 1]:
                    return False
            var += 1

        for column in range(len(matrix[0])):
            cur_column = []
            row = 0
            while row < len(matrix):
                if matrix[row][column] in cur_column:
                    return False
                cur_column.append(matrix[row][column])
                row += 1
        
        return True

solution = Solution()
print(solution.checkValid(matrix = [[1,2,3],[3,1,2],[2,3,1]]))
print(solution.checkValid(matrix = [[1,1,1],[1,2,3],[1,2,3]]))