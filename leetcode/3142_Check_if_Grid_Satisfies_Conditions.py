# You are given a 2D matrix grid of size m x n. You need to check if each cell grid[i][j] is:

# Equal to the cell below it, i.e. grid[i][j] == grid[i + 1][j] (if it exists).
# Different from the cell to its right, i.e. grid[i][j] != grid[i][j + 1] (if it exists).
# Return true if all the cells satisfy these conditions, otherwise, return false.

# Example 1:
# Input: grid = [[1,0,2],[1,0,2]]
# Output: true
# Explanation:
# All the cells in the grid satisfy the conditions.

# Example 2:
# Input: grid = [[1,1,1],[0,0,0]]
# Output: false
# Explanation:
# All cells in the first row are equal.

# Example 3:
# Input: grid = [[1],[2],[3]]
# Output: false
# Explanation:
# Cells in the first column have different values.

# Constraints:
# 1 <= n, m <= 10
# 0 <= grid[i][j] <= 9


class Solution:
    def satisfiesConditions(self, grid: [[int]]) -> bool:
        if len(grid) == 1:
            for i in range(len(grid[0]) - 1):
                if grid[0][i] == grid[0][i + 1]:
                    return False
            return True
        
        for i in range(1, len(grid)):
            for j in range(len(grid[i]) - 1):
                if grid[i][j] == grid[i][j + 1]:
                    return False
            
            for j in range(len(grid[i])):
                if grid[i][j] != grid[i - 1][j]:
                    return False
        
        return True
    


solution = Solution()
print(solution.satisfiesConditions(grid = [[1,0,2],[1,0,2]]))
print(solution.satisfiesConditions(grid = [[1,1,1],[0,0,0]]))
print(solution.satisfiesConditions(grid = [[1],[2],[3]]))