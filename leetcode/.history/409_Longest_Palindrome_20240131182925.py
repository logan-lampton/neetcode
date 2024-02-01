# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

# Example 1:
# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

# Example 2:
# Input: s = "a"
# Output: 1
# Explanation: The longest palindrome that can be built is "a", whose length is 1.

# Constraints:
# 1 <= s.length <= 2000
# s consists of lowercase and/or uppercase English letters only.


class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashtable = {}

        for char in s:
            if char not in hashtable:
                hashtable[char] = 1
            else:
                hashtable[char] += 1

        length_sum = 0

        for value in hashtable.values():
            if value % 2 == 0:
                length_sum += value
            elif value % 2 != 0:
                length_sum += value - 1

        if length_sum < len(s):
            length_sum += 1

        print(length_sum)
