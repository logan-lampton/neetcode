# Given two positive integers a and b, return the number of common factors of a and b.

# An integer x is a common factor of a and b if x divides both a and b.

# Example 1:
# Input: a = 12, b = 6
# Output: 4
# Explanation: The common factors of 12 and 6 are 1, 2, 3, 6.

# Example 2:
# Input: a = 25, b = 30
# Output: 2
# Explanation: The common factors of 25 and 30 are 1, 5.

# Constraints:
# 1 <= a, b <= 1000


class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        smallest = min(a, b)
        common_factors = 0
        num_counter = 1
        for i in range(smallest):
            if a % num_counter == 0 and b % num_counter == 0:
                common_factors += 1
            num_counter += 1
        return common_factors


solution = Solution()
print(solution.commonFactors(a=12, b=6))
