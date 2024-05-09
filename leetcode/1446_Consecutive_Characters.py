# The power of the string is the maximum length of a non-empty substring that contains only one unique character.

# Given a string s, return the power of s.

# Example 1:
# Input: s = "leetcode"
# Output: 2
# Explanation: The substring "ee" is of length 2 with the character 'e' only.

# Example 2:
# Input: s = "abbcccddddeeeeedcba"
# Output: 5
# Explanation: The substring "eeeee" is of length 5 with the character 'e' only.

# Constraints:
# 1 <= s.length <= 500
# s consists of only lowercase English letters.


class Solution:
    def maxPower(self, s: str) -> int:

        max_count = 1
        current_count = 1
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                current_count += 1
                max_count = max(max_count, current_count)
            else:
                current_count = 1

        return max_count


solution = Solution()
print(solution.maxPower(s="leetcode"))
