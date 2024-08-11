# A bit flip of a number x is choosing a bit in the binary representation of x and flipping it from either 0 to 1 or 1 to 0.

# For example, for x = 7, the binary representation is 111 and we may choose any bit (including any leading zeros not shown) and flip it. We can flip the first bit from the right to get 110, flip the second bit from the right to get 101, flip the fifth bit from the right (a leading zero) to get 10111, etc.
# Given two integers start and goal, return the minimum number of bit flips to convert start to goal.

# Example 1:
# Input: start = 10, goal = 7
# Output: 3
# Explanation: The binary representation of 10 and 7 are 1010 and 0111 respectively. We can convert 10 to 7 in 3 steps:
# - Flip the first bit from the right: 1010 -> 1011.
# - Flip the third bit from the right: 1011 -> 1111.
# - Flip the fourth bit from the right: 1111 -> 0111.
# It can be shown we cannot convert 10 to 7 in less than 3 steps. Hence, we return 3.

# Example 2:
# Input: start = 3, goal = 4
# Output: 3
# Explanation: The binary representation of 3 and 4 are 011 and 100 respectively. We can convert 3 to 4 in 3 steps:
# - Flip the first bit from the right: 011 -> 010.
# - Flip the second bit from the right: 010 -> 000.
# - Flip the third bit from the right: 000 -> 100.
# It can be shown we cannot convert 3 to 4 in less than 3 steps. Hence, we return 3.

# Constraints:
# 0 <= start, goal <= 109


class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        start_bin = bin(start)[2:]
        goal_bin = bin(goal)[2:]
        
        leading_zeros = 0
        shorter = 0
        longer = 0

        if len(start_bin) > len(goal_bin):
            longer = start_bin
            shorter = goal_bin
        else:
            longer = goal_bin
            shorter = start_bin

        leading_zeros = len(longer) - len(shorter)

        string_zeros = ""
        for _ in range(leading_zeros):
            string_zeros += "0"
        
        final_start = start_bin
        final_goal = goal_bin

        if start_bin == shorter:
            final_start = string_zeros + start_bin
        else:
            final_goal = string_zeros + goal_bin
        
        changes = 0
        for i in range(len(longer)):
            if final_start[i] != final_goal[i]:
                changes += 1
        
        return changes


solution = Solution()
print(solution.minBitFlips(start = 10, goal = 7))
print(solution.minBitFlips(start = 3, goal = 4))