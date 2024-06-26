# A parentheses string is valid if and only if:

# It is the empty string,
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.
# You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.

# For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".
# Return the minimum number of moves required to make s valid.

# Example 1:
# Input: s = "())"
# Output: 1

# Example 2:
# Input: s = "((("
# Output: 3

# Constraints:
# 1 <= s.length <= 1000
# s[i] is either '(' or ')'.

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_p = 0
        unmatched_closed_p = 0

        for p in s:
            if p == "(":
                open_p += 1
            else:
                if open_p > 0:
                    open_p -= 1
                else:
                    unmatched_closed_p += 1
            
        return open_p + unmatched_closed_p

solution = Solution()
print(solution.minAddToMakeValid(s = "())"))
print(solution.minAddToMakeValid(s = "((("))