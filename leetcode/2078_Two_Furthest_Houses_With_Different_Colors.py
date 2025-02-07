# There are n houses evenly lined up on the street, and each house is beautifully painted. You are given a 0-indexed integer array colors of length n, where colors[i] represents the color of the ith house.

# Return the maximum distance between two houses with different colors.

# The distance between the ith and jth houses is abs(i - j), where abs(x) is the absolute value of x.

# Example 1:
# Input: colors = [1,1,1,6,1,1,1]
# Output: 3
# Explanation: In the above image, color 1 is blue, and color 6 is red.
# The furthest two houses with different colors are house 0 and house 3.
# House 0 has color 1, and house 3 has color 6. The distance between them is abs(0 - 3) = 3.
# Note that houses 3 and 6 can also produce the optimal answer.

# Example 2:
# Input: colors = [1,8,3,8,3]
# Output: 4
# Explanation: In the above image, color 1 is blue, color 8 is yellow, and color 3 is green.
# The furthest two houses with different colors are house 0 and house 4.
# House 0 has color 1, and house 4 has color 3. The distance between them is abs(0 - 4) = 4.

# Example 3:
# Input: colors = [0,1]
# Output: 1
# Explanation: The furthest two houses with different colors are house 0 and house 1.
# House 0 has color 0, and house 1 has color 1. The distance between them is abs(0 - 1) = 1.

# Constraints:
# n == colors.length
# 2 <= n <= 100
# 0 <= colors[i] <= 100
# Test data are generated such that at least two houses have different colors.

class Solution:
    def maxDistance(self, colors: [int]) -> int:
        max_distance = 1
        for i in range(len(colors)):
            if colors[0] != colors[i]:
                max_distance = max(max_distance, i)
        for i in range(len(colors)):
            if colors[len(colors) - 1] != colors[i]:
                max_distance = max(max_distance, len(colors) - 1 - i)
        return max_distance

solution = Solution()
print(solution.maxDistance(colors = [1,1,1,6,1,1,1]))
print(solution.maxDistance(colors = [1,8,3,8,3]))
print(solution.maxDistance(colors = [0,1]))

# Additional practice:
class Solution:
    def maxDistance(self, colors: [int]) -> int:
        left = 0
        right = len(colors) - 1

        first_house = colors[0]
        last_house = colors[len(colors) - 1]

        while colors[right] == first_house and colors[left] == last_house:
            left += 1
            right -= 1 
        
        if left > right:
            return left
        else:
            return right