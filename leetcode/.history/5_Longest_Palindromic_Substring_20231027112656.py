# Given a string s, return the longest palindromic substring in s.

# Example 1:
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

# Example 2:
# Input: s = "cbbd"
# Output: "bb"

# Constraints:
# 1 <= s.length <= 1000
# s consist of only digits and English letters.


class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_length = 0
        begin_idx = 0
        end_idx = 0

        for i in range(len(s)):
            # checking for even palindromic string
            left = i - 1
            right = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > max_length:
                    max_length = right - left + 1
                    begin_idx = left
                    end_idx = right
                left -= 1
                right += 1

            # checking for odd palindromic string
            left = i - 1
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > max_length:
                    max_length = right - left + 1
                    begin_idx = left
                    end_idx = right
                left -= 1
                right += 1

        return s[begin_idx : end_idx + 1]
