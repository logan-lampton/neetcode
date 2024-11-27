# In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.

# You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.

# The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

# If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

# Example 1:
# Input: mat = [[1,2],[3,4]], r = 1, c = 4
# Output: [[1,2,3,4]]

# Example 2:
# Input: mat = [[1,2],[3,4]], r = 2, c = 4
# Output: [[1,2],[3,4]]

# Constraints:
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 100
# -1000 <= mat[i][j] <= 1000
# 1 <= r, c <= 300

class Solution:
    def matrixReshape(self, mat: [[int]], r: int, c: int) -> [[int]]:
        
        combined_array = []
        for row in mat:
            for cell in row:
                combined_array.append(cell)

        if r * c > len(combined_array) or r * c < len(combined_array):
            return mat

        final_matrix = []

        for i in range(0, len(combined_array), c):
            final_matrix.append(combined_array[i:i + c])
        
        return final_matrix

solution = Solution()
print(solution.matrixReshape(mat = [[1,2],[3,4]], r = 1, c = 4))
print(solution.matrixReshape(mat = [[1,2],[3,4]], r = 2, c = 4))