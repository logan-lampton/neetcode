# An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

# You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

# To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

# Return the modified image after performing the flood fill.

# Example 1:
# Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]
# Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
# Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.

# Example 2:
# Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
# Output: [[0,0,0],[0,0,0]]
# Explanation: The starting pixel is already colored 0, so no changes are made to the image.

# Constraints:
# m == image.length
# n == image[i].length
# 1 <= m, n <= 50
# 0 <= image[i][j], color < 216
# 0 <= sr < m
# 0 <= sc < n

def floodFill(self, image: [[int]], sr: int, sc: int, color: int) -> [[int]]:
    initial_color = image[sr][sc]

    if initial_color == color:
        return image

    def dfs(row, column):
        if row < 0 or row >= len(image) or column < 0 or column >= len(image[0]) or image[row][column] != initial_color:
            return
        image[row][column] = color
        dfs(row - 1, column)
        dfs(row + 1, column)
        dfs(row, column - 1)
        dfs(row, column + 1)
    
    dfs(sr, sc)
    return image


# def floodFill(image: [[int]], sr: int, sc: int, color: int) -> [[int]]:
#     original_color = image[sr][sc]

#     if original_color == color:
#         return image

#     def dfs(row, col):
#         if image[row][col] == original_color:
#             image[row][col] = color
#             if row >= 1:
#                 dfs(row - 1, col)
#             if row + 1 < len(image):
#                 dfs(row + 1, col)
#             if col >= 1:
#                 dfs(row, col - 1)
#             if col + 1 < len(image[0]):
#                 dfs(row, col + 1)

#     dfs(sr, sc)

#     return image
