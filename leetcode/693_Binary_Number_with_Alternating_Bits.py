# Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.

# Example 1:
# Input: n = 5
# Output: true
# Explanation: The binary representation of 5 is: 101

# Example 2:
# Input: n = 7
# Output: false
# Explanation: The binary representation of 7 is: 111.

# Example 3:
# Input: n = 11
# Output: false
# Explanation: The binary representation of 11 is: 1011.

# Constraints:
# 1 <= n <= 231 - 1


class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        bin_n = bin(n)
        for i in range(3, len(bin_n)):
            if bin_n[i] == bin_n[i - 1]:
                return False
        return True
    

solution = Solution()
print(solution.hasAlternatingBits(n = 5))
print(solution.hasAlternatingBits(n = 7))
print(solution.hasAlternatingBits(n = 11))