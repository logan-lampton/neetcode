# Given a string s consisting of only the characters 'a' and 'b', return true if every 'a' appears before every 'b' in the string. Otherwise, return false.

# Example 1:
# Input: s = "aaabbb"
# Output: true
# Explanation:
# The 'a's are at indices 0, 1, and 2, while the 'b's are at indices 3, 4, and 5.
# Hence, every 'a' appears before every 'b' and we return true.

# Example 2:
# Input: s = "abab"
# Output: false
# Explanation:
# There is an 'a' at index 2 and a 'b' at index 1.
# Hence, not every 'a' appears before every 'b' and we return false.

# Example 3:
# Input: s = "bbb"
# Output: true
# Explanation:
# There are no 'a's, hence, every 'a' appears before every 'b' and we return true.

# Constraints:
# 1 <= s.length <= 100
# s[i] is either 'a' or 'b'.

class Solution:
    def checkString(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] == "b" and s[right] == "a":
                return False
            if s[left] == "a":
                left += 1
            if s[right] == "b":
                right -= 1
        return True

solution = Solution()
print(solution.checkString(s="abab"))