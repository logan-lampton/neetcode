# A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself. A divisor of an integer x is an integer that can divide x evenly.

# Given an integer n, return true if n is a perfect number, otherwise return false.

# Example 1:
# Input: num = 28
# Output: true
# Explanation: 28 = 1 + 2 + 4 + 7 + 14
# 1, 2, 4, 7, and 14 are all divisors of 28.

# Example 2:
# Input: num = 7
# Output: false

# Constraints:
# 1 <= num <= 108

import math

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num < 5:
            return False
            
        divisor_addition = 1

        for digit in range(2, int(math.sqrt(num)) + 1):
            if num % digit == 0:
                divisor_addition += digit + num // digit

        return divisor_addition == num
    

solution = Solution()
print(solution.checkPerfectNumber(num = 28))
print(solution.checkPerfectNumber(num = 7))