# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

# Example 4:
# Input: s = "([])"
# Output: true

# Constraints:
# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.


class Solution:
    def isValid(self, s: str) -> bool:
        dictionary = {")" : "(", "}" : "{", "]" : "["}
        stack = []

        for char in s:
            if stack and char in dictionary:
                if stack[-1] == dictionary[char]:
                    stack.pop()
                else:
                    stack.append(char)
            else:
                stack.append(char)
        
        return not stack


solution = Solution()
print(solution.isValid(s = "()"))
print(solution.isValid(s = "()[]{}"))
print(solution.isValid(s = "(]"))
print(solution.isValid(s = "([])"))


# practice
class Solution:
    def isValid(self, s: str) -> bool:
        dictionary = {')':'(' , '}':'{' , ']': '['}
        stack = []

        for char in s:
            if char == "(" or char == "{" or char == "[":
                stack.append(char)
            elif stack and stack[-1] == dictionary[char]:
                stack.pop()
            else:
                stack.append(char)
        
        return not stack

# Practice
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {")" : "(", "}" : "{", "]" : "["}

        for char in s:
            if char in pairs.values():
                stack.append(char)
            elif stack:
                if stack[-1] == pairs[char]:
                    stack.pop()
                else:
                    stack.append(char)
            else:
                stack.append(char)

        return len(stack) == 0