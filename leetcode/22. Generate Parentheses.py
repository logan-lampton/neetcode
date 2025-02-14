# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# Example 1:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

# Example 2:
# Input: n = 1
# Output: ["()"]

# Constraints:
# 1 <= n <= 8

from typing import List;

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def backtrack(open_count, closed_count, cur_string):
            if open_count > n:
                return
            elif closed_count > n:
                return
            elif open_count < closed_count:
                return
            elif open_count == n and closed_count == n:
                combinations.append(cur_string)
                return
            backtrack(open_count + 1, closed_count, cur_string + "(")
            backtrack(open_count, closed_count + 1, cur_string + ")")

        combinations = []
        backtrack(0, 0, "")

        return combinations


solution = Solution()
print(solution.generateParenthesis(n=3))
print(solution.generateParenthesis(n=1))