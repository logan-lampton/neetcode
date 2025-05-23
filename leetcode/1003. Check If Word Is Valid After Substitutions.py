# Given a string s, determine if it is valid.

# A string s is valid if, starting with an empty string t = "", you can transform t into s after performing the following operation any number of times:

# Insert string "abc" into any position in t. More formally, t becomes tleft + "abc" + tright, where t == tleft + tright. Note that tleft and tright may be empty.
# Return true if s is a valid string, otherwise, return false.

# Example 1:
# Input: s = "aabcbc"
# Output: true
# Explanation:
# "" -> "abc" -> "aabcbc"
# Thus, "aabcbc" is valid.

# Example 2:
# Input: s = "abcabcababcc"
# Output: true
# Explanation:
# "" -> "abc" -> "abcabc" -> "abcabcabc" -> "abcabcababcc"
# Thus, "abcabcababcc" is valid.

# Example 3:
# Input: s = "abccba"
# Output: false
# Explanation: It is impossible to get "abccba" using the operation.

# Constraints:
# 1 <= s.length <= 2 * 104
# s consists of letters 'a', 'b', and 'c'


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in range(len(s)):
            if s[i] == "c" and len(stack) >= 2:
                if stack[-1] == "b" and stack[-2] == "a":
                    stack.pop()
                    stack.pop()
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])
            
        return stack == [] or "".join(stack) == "abc"

solution = Solution()
print(solution.isValid(s = "aabcbc"))
print(solution.isValid(s = "abcabcababcc"))
print(solution.isValid(s = "abccba"))