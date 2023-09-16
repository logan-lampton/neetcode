# You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0
# represents water.

# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water,
# and there is exactly one island (i.e., one or more connected land cells).

# The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island.
# One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100.
# Determine the perimeter of the island.

# Example 1:
# Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
# Output: 16
# Explanation: The perimeter is the 16 yellow stripes in the image above.

# Example 2:
# Input: grid = [[1]]
# Output: 4

# Example 3:
# Input: grid = [[1,0]]
# Output: 4


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # set a variable for the number of perimeters
        perimeter = 0

        # loop through each cell in the grid, rows and columns
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    # test the 4 sides for a perimeter:
                    # TOP
                    # if i == 0, so the top row, it must have a perimeter
                    # if the row before had a 0 in that column, then it must have a perimeter
                    if i == 0 or grid[i - 1][j] == 0:
                        perimeter += 1
                    # LEFT SIDE
                    # if j is the first column, or the column before in that row was 0, it must have a perimeter
                    if j == 0 or grid[i][j - 1] == 0:
                        perimeter += 1
                    # BOTTOM
                    # if the last row or the following row are 0, it must have a perimeter
                    if i == len(grid) - 1 or grid[i + 1][j] == 0:
                        perimeter += 1
                    # RIGHT SIDE
                    # if j is the last column or the column after is 0, it must have a perimeter
                    if j == len(grid[i]) - 1 or grid[i][j + 1] == 0:
                        perimeter += 1

        return perimeter
