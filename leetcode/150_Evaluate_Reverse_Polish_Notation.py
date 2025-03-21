# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

# Evaluate the expression. Return an integer that represents the value of the expression.

# Note that:
# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# The input represents a valid arithmetic expression in a reverse polish notation.
# The answer and all the intermediate calculations can be represented in a 32-bit integer.

# Example 1:
# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9

# Example 2:
# Input: tokens = ["4","13","5","/","+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6

# Example 3:
# Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# Output: 22
# Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22

# Constraints:
# 1 <= tokens.length <= 104
# tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].

from typing import List

class Solution:
    def evalRPN(self, tokens: [str]) -> int:

        stack = []

        for token in tokens:
            if token not in {"+", "-", "*", "/"}:
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    stack.append(trunc(a / b))

        return stack[0]

# Practice / somewhat different method:
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for token in tokens:
            if token == "+":
                second_int = stack.pop()
                first_int = stack.pop()
                cur_sum = first_int + second_int
                stack.append(cur_sum)
            elif token == "-":
                second_int = stack.pop()
                first_int = stack.pop()
                cur_sum = first_int - second_int
                stack.append(cur_sum)
            elif token == "*":
                second_int = stack.pop()
                first_int = stack.pop()
                cur_prod = first_int * second_int
                stack.append(cur_prod)
            elif token == "/":
                second_int = stack.pop()
                first_int = stack.pop()
                cur_div = int(first_int / second_int)
                stack.append(cur_div)
            else:
                stack.append(int(token))
            
        return stack[0]


# Practice
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        operators = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x // y if x * y > 0 else -(-x // y)
        }

        for token in tokens:
            if token in operators:
                second_integer = stack.pop()
                first_integer = stack.pop()
                cur_result = operators[token](first_integer, second_integer)
                stack.append(cur_result)
            else:
                stack.append(int(token))
        
        return stack[0]