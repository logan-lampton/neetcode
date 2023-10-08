# Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.

# Return the maximum product you can get.

# Example 1:
# Input: n = 2
# Output: 1
# Explanation: 2 = 1 + 1, 1 × 1 = 1.

# Example 2:
# Input: n = 10
# Output: 36
# Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.


class Solution:
    def integerBreak(self, n: int) -> int:
        dynamic_programming = [0] * (n + 1)

        dynamic_programming[1] = 1

        for i in range(2, n + 1):
            dynamic_programming[i] = -float("inf")
            for j in range(1, i):
                dynamic_programming[i] = max(
                    dynamic_programming[i], j * (i - j), j * dynamic_programming[i - j]
                )

        print(dynamic_programming)
        return dynamic_programming[n]
