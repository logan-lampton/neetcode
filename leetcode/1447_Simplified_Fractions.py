# Given an integer n, return a list of all simplified fractions between 0 and 1 (exclusive) such that the denominator is less-than-or-equal-to n. You can return the answer in any order.

# Example 1:
# Input: n = 2
# Output: ["1/2"]
# Explanation: "1/2" is the only unique fraction with a denominator less-than-or-equal-to 2.

# Example 2:
# Input: n = 3
# Output: ["1/2","1/3","2/3"]

# Example 3:
# Input: n = 4
# Output: ["1/2","1/3","1/4","2/3","3/4"]
# Explanation: "2/4" is not a simplified fraction because it can be simplified to "1/2".

# Constraints:
# 1 <= n <= 100

class Solution:
    def simplifiedFractions(self, n: int) -> [str]:

        def coprime(val1, val2):
            min_val = min(val1, val2)
            for i in range(2, min_val + 1):
                if val1 % i == val2 % i == 0:
                    return False
            return True

        answer = []

        for num in range(1, n):
            for denom in range(num + 1, n + 1):
                if coprime(num, denom):
                    answer.append(f"{num}/{denom}")
        
        return answer
    
solution = Solution()
print(solution.simplifiedFractions(n = 2))
print(solution.simplifiedFractions(n = 3))
print(solution.simplifiedFractions(n = 4))