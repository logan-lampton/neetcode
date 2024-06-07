# Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

# Given a balanced string s, split it into some number of substrings such that:

# Each substring is balanced.
# Return the maximum number of balanced strings you can obtain.

# Example 1:
# Input: s = "RLRRLLRLRL"
# Output: 4
# Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.

# Example 2:
# Input: s = "RLRRRLLRLL"
# Output: 2
# Explanation: s can be split into "RL", "RRRLLRLL", each substring contains same number of 'L' and 'R'.
# Note that s cannot be split into "RL", "RR", "RL", "LR", "LL", because the 2nd and 5th substrings are not balanced.

# Example 3:
# Input: s = "LLLLRRRR"
# Output: 1
# Explanation: s can be split into "LLLLRRRR".

# Constraints:
# 2 <= s.length <= 1000
# s[i] is either 'L' or 'R'.
# s is a balanced string.

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        left = 0
        substring_total = 0

        for right in range(1, len(s)):
            if s[left:right + 1].count("L") == s[left:right + 1].count("R"):
                substring_total += 1
                left = right + 1
                right += 2
            else:
                right += 1
        
        return substring_total

solution = Solution()
print(solution.balancedStringSplit(s="RLRRLLRLRL"))
print(solution.balancedStringSplit(s="RLRRRLLRLL"))
print(solution.balancedStringSplit(s="LLLLRRRR"))