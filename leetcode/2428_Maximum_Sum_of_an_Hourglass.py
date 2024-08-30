# You are given an m x n integer matrix grid.

# We define an hourglass as a part of the matrix with the following form:

# Return the maximum sum of the elements of an hourglass.

# Note that an hourglass cannot be rotated and must be entirely contained within the matrix.

# Example 1:
# Input: grid = [[6,2,1,3],[4,2,1,5],[9,2,8,7],[4,1,2,9]]
# Output: 30
# Explanation: The cells shown above represent the hourglass with the maximum sum: 6 + 2 + 1 + 2 + 9 + 2 + 8 = 30.

# Example 2:
# Input: grid = [[1,2,3],[4,5,6],[7,8,9]]
# Output: 35
# Explanation: There is only one hourglass in the matrix, with the sum: 1 + 2 + 3 + 5 + 7 + 8 + 9 = 35.

# Constraints:
# m == grid.length
# n == grid[i].length
# 3 <= m, n <= 150
# 0 <= grid[i][j] <= 106


class Solution:
    def maxSum(self, grid: [[int]]) -> int:

        max_total = 0

        num_cells_in_row = 0
        for row in grid:
            num_cells_in_row = len(row)
            break
        
        cur_first_row = 0

        def test_rows(row1, row3):
            nonlocal max_total
            top_row = row1
            middle_row = row1 + 1
            bottom_row = row3

            first_row_index = 0
            row_index = 0

            while first_row_index < (num_cells_in_row - 2):
                cur_total = sum(grid[top_row][first_row_index: first_row_index + 3]) + grid[middle_row][first_row_index + 1] + sum(grid[bottom_row][first_row_index: first_row_index + 3])
                if cur_total > max_total:
                    max_total = cur_total
                first_row_index += 1
        
        while cur_first_row < len(grid) - 2:
            test_rows(cur_first_row, cur_first_row + 2)
            cur_first_row += 1

        return max_total


solution = Solution()
print(solution.maxSum(grid = [[6,2,1,3],[4,2,1,5],[9,2,8,7],[4,1,2,9]]))
print(solution.maxSum(grid = [[1,2,3],[4,5,6],[7,8,9]]))