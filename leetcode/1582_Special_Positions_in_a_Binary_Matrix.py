# Given an m x n binary matrix mat, return the number of special positions in mat.

# A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).

# Example 1:
# Input: mat = [[1,0,0],[0,0,1],[1,0,0]]
# Output: 1
# Explanation: (1, 2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.

# Example 2:
# Input: mat = [[1,0,0],[0,1,0],[0,0,1]]
# Output: 3
# Explanation: (0, 0), (1, 1) and (2, 2) are special positions.

# Constraints:
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 100
# mat[i][j] is either 0 or 1.

class Solution:
    def numSpecial(self, mat: [[int]]) -> int:
        special = 0

        row_sums = []
        for row in mat:
            row_sums.append(sum(row))
        
        col_sums = [0] * len(mat[0])
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                col_sums[j] += mat[i][j]
        
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] == 1:
                    if row_sums[i] == 1 and col_sums[j] == 1:
                        special += 1
    
        return special
    

solution = Solution()
print(solution.numSpecial(mat = [[1,0,0],[0,0,1],[1,0,0]]))
print(solution.numSpecial(mat = [[1,0,0],[0,1,0],[0,0,1]]))