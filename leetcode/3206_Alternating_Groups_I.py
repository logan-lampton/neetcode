# There is a circle of red and blue tiles. You are given an array of integers colors. The color of tile i is represented by colors[i]:

# colors[i] == 0 means that tile i is red.
# colors[i] == 1 means that tile i is blue.
# Every 3 contiguous tiles in the circle with alternating colors (the middle tile has a different color from its left and right tiles) is called an alternating group.

# Return the number of alternating groups.

# Note that since colors represents a circle, the first and the last tiles are considered to be next to each other.

# Example 1:
# Input: colors = [1,1,1]
# Output: 0

# Example 2:
# Input: colors = [0,1,0,0,1]
# Output: 3

# Constraints:
# 3 <= colors.length <= 100
# 0 <= colors[i] <= 1

from typing import List

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        alternating_groups = 0

        for i in range(len(colors)):
            if i == 0:
                if colors[i] != colors[-1] and colors[i] != colors[i + 1]:
                    alternating_groups += 1
            elif i == len(colors) - 1:
                if colors[i] != colors[i - 1] and colors[i] != colors[0]:
                    alternating_groups += 1
            else:
                if colors[i] != colors[i - 1] and colors[i] != colors[i + 1]:
                    alternating_groups += 1
                
        return alternating_groups


solution = Solution()
print(solution.numberOfAlternatingGroups(colors = [1,1,1]))
print(solution.numberOfAlternatingGroups(colors = [0,1,0,0,1]))