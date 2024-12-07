# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

# Example 1:
# Input: s = "aba"
# Output: true

# Example 2:
# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.

# Example 3:
# Input: s = "abc"
# Output: false

# Constraints:
# 1 <= s.length <= 105
# s consists of lowercase English letters.


class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left <= right:
            if s[left] != s[right]:
                string1 = s[:left] + s[left + 1 :]
                string2 = s[:right] + s[right + 1 :]
                return string1 == string1[::-1] or string2 == string2[::-1]
            left += 1
            right -= 1
        
        return True
    

solution = Solution()
print(solution.validPalindrome(s = "aba"))
print(solution.validPalindrome(s = "abca"))
print(solution.validPalindrome(s = "abc"))