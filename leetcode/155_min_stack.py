# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
# Implement the MinStack class:
#
# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.
#
#
#
# Example 1:
#
# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
#
# Output
# [null,null,null,null,-3,null,0,-2]

class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))
        """
        :type val: int
        :rtype: None
        """

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()
        """
        :rtype: None
        """

    def top(self):
        return self.stack[-1]
        """
        :rtype: int
        """

    def getMin(self):
        return self.min_stack[-1]
        """
        :rtype: int
        """

# Additional practice / different code:
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.min_stack:
            self.min_stack.append(val)
        elif val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        cur_val = self.stack[-1]
        self.stack.pop()
        if self.min_stack[-1] == cur_val:
            self.min_stack.pop()   
        
    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        return None


# Practice
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or self.min_stack[-1] >= val:
            self.min_stack.append(val)
        
    def pop(self) -> None:
        stack_pop = self.stack[-1]
        self.stack.pop()
        if stack_pop == self.min_stack[-1]:
            self.min_stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]


    def getMin(self) -> int:
        return self.min_stack[-1]