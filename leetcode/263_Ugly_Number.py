# An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

# Given an integer n, return true if n is an ugly number.

# Example 1:
# Input: n = 6
# Output: true
# Explanation: 6 = 2 × 3

# Example 2:
# Input: n = 1
# Output: true
# Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.

# Example 3:
# Input: n = 14
# Output: false
# Explanation: 14 is not ugly since it includes the prime factor 7.

# Constraints:
# -231 <= n <= 231 - 1


class Solution:
    def isUgly(self, n: int) -> bool:
        if n < 1:
            return False

        for divisor in [2, 3, 5]:
            while n % divisor == 0:
                n //= divisor
        
        return n == 1
    

solution = Solution()
print(solution.isUgly(n = 6))
print(solution.isUgly(n = 1))
print(solution.isUgly(n = 14))