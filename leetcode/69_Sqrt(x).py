# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

# You must not use any built-in exponent function or operator.

# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

# Example 1:
# Input: x = 4
# Output: 2
# Explanation: The square root of 4 is 2, so we return 2.

# Example 2:
# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

# Constraints:
# 0 <= x <= 231 - 1


class Solution:
    def mySqrt(self, x: int) -> int:
        left = 1
        right = x

        while left <= right:
            midpoint = (left + right) // 2
            if midpoint * midpoint == x:
                return midpoint
            if midpoint * midpoint > x:
                right = midpoint - 1
            else:
                left = midpoint + 1
        return right


solution = Solution()
print(solution.mySqrt(x = 4))
print(solution.mySqrt(x = 8))
print(solution.mySqrt(x = 2147395599))