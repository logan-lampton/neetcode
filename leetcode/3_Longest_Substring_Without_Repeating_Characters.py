# Given a string s, find the length of the longest 
# substring
#  without repeating characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

# Constraints:
# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1

        dictionary = {}
        max_length = 0
        left = 0

        for right, char in enumerate(s):
            if char not in dictionary:
                dictionary[char] = 1
            else:
                dictionary[char] += 1
            if dictionary[char] > 1:
                while left < right and dictionary[char] > 1:
                    dictionary[s[left]] -= 1
                    left += 1
            length = right - left + 1
            max_length = max(max_length, length)
        
        return max_length