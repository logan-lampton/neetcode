# valid parentheses question using a hash map

class Solution(object):
    def isValid(self, s):
        stack = []
        hash_map = {"(": ")", "{": "}", "[": "]"}

        for char in s:
            # If it's an opening bracket, push it onto the stack
            if char in hash_map:
                stack.append(char)
            # if it's a closing bracket
            else:
                if not stack or hash_map[stack.pop()] != char:
                    return False

        # stack must be empty at the end to be True
        if not stack:
            return True
