# An alphabetical continuous string is a string consisting of consecutive letters in the alphabet. In other words, it is any substring of the string "abcdefghijklmnopqrstuvwxyz".

# For example, "abc" is an alphabetical continuous string, while "acb" and "za" are not.
# Given a string s consisting of lowercase letters only, return the length of the longest alphabetical continuous substring.

# Example 1:
# Input: s = "abacaba"
# Output: 2
# Explanation: There are 4 distinct continuous substrings: "a", "b", "c" and "ab".
# "ab" is the longest continuous substring.

# Example 2:
# Input: s = "abcde"
# Output: 5
# Explanation: "abcde" is the longest continuous substring.

# Constraints:
# 1 <= s.length <= 105
# s consists of only English lowercase letters.

class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        left = 0
        longest_substring = 1
        current_substring = 1
        for right in range(1, len(s)):
            if ord(s[left]) + 1 == ord(s[right]):
                current_substring += 1
            else:
                longest_substring = max(current_substring, longest_substring)
                current_substring = 1
            left += 1
            right += 1

        return max(longest_substring, current_substring)

solution = Solution()
print(solution.longestContinuousSubstring(s="abacaba"))
print(solution.longestContinuousSubstring(s="abcde"))