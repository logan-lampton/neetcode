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
    

# more naive
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        longest_substring_len = 1
        left = 0
        right = 1

        while right < len(s):
            if s[right] not in s[left:right]:
                cur_substring_len = right - left + 1
                if cur_substring_len > longest_substring_len:
                    longest_substring_len = cur_substring_len
                right += 1
            else:
                left += 1
                right = left + 1
        
        return longest_substring_len


# approach with set
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substring_len = 0
        left = 0
        right = 0
        char_set = set()

        while right < len(s):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            char_set.add(s[right])

            cur_substring_len = right - left + 1
            if cur_substring_len > longest_substring_len:
                longest_substring_len = cur_substring_len
            
            right += 1


# Practice:
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        cur_hash = {}
        longest_substring = 0
        lower_index = 0

        for i, char in enumerate(s):
            if char in cur_hash and cur_hash[char] >= lower_index:
                lower_index = cur_hash[char] + 1
            cur_hash[char] = i
            cur_length = i - lower_index + 1
            if cur_length > longest_substring:
                longest_substring = cur_length

        return longest_substring
