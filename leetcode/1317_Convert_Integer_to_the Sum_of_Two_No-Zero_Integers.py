# No-Zero integer is a positive integer that does not contain any 0 in its decimal representation.

# Given an integer n, return a list of two integers [a, b] where:

# a and b are No-Zero integers.
# a + b = n
# The test cases are generated so that there is at least one valid solution. If there are many valid solutions, you can return any of them.

# Example 1:
# Input: n = 2
# Output: [1,1]
# Explanation: Let a = 1 and b = 1.
# Both a and b are no-zero integers, and a + b = 2 = n.

# Example 2:
# Input: n = 11
# Output: [2,9]
# Explanation: Let a = 2 and b = 9.
# Both a and b are no-zero integers, and a + b = 9 = n.
# Note that there are other valid answers as [8, 3] that can be accepted.

# Constraints:
# 2 <= n <= 104


class Solution:
    def getNoZeroIntegers(self, n: int) -> [int]:
        for i in range(n):
            if i > 0 and '0' not in str((n - i)) and '0' not in str(i):
                return [i, n - i]
            

solution = Solution()
print(solution.getNoZeroIntegers(n = 2))
print(solution.getNoZeroIntegers(n = 11))