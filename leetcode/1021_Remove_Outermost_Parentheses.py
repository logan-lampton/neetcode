# A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses
# strings, and + represents string concatenation.

# For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
# A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it into
#  s = A + B, with A and B nonempty valid parentheses strings.

# Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk, where Pi are
#  primitive valid parentheses strings.

# Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.

# Example 1:
# Input: s = "(()())(())"
# Output: "()()()"
# Explanation:
# The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
# After removing outer parentheses of each part, this is "()()" + "()" = "()()()".

# Example 2:
# Input: s = "(()())(())(()(()))"
# Output: "()()()()(())"
# Explanation:
# The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
# After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".

# Example 3:
# Input: s = "()()"
# Output: ""
# Explanation:
# The input string is "()()", with primitive decomposition "()" + "()".
# After removing outer parentheses of each part, this is "" + "" = "".

# Constraints:
# 1 <= s.length <= 105
# s[i] is either '(' or ')'.
# s is a valid parentheses string.


class Solution:
    def removeOuterParentheses(self, s: str) -> str:

        stack = []
        p_open = 0

        for char in s:
            if char == ")":
                p_open -= 1
            if p_open > 0:
                stack.append(char)
            if char == "(":
                p_open += 1

        return "".join(stack)


# Practice:
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        answer = []
        for char in s:
            if char == "(":
                if stack:
                    answer.append(char)
                stack.append(char)
            else:
                stack.pop()
                if stack:
                    answer.append(char)
        
        return "".join(answer)
    

# Practice
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        answer = ""

        for char in s:
            if char == "(":
                if stack:
                    answer += char
                stack.append(char)
            else:
                stack.pop()
                if stack:
                    answer += char

        return answer
    
# Practice
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        
        stack = []
        open_par = 0

        for char in s:
            if char == "(" and open_par > 0:
                stack.append(char)
            if char == ")" and open_par > 1:
                stack.append(char)
            if char == "(":
                open_par += 1
            else:
                open_par -= 1
        
        return "".join(stack)