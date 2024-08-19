# Design a stack that supports increment operations on its elements.

# Implement the CustomStack class:

# CustomStack(int maxSize) Initializes the object with maxSize which is the maximum number of elements in the stack.
# void push(int x) Adds x to the top of the stack if the stack has not reached the maxSize.
# int pop() Pops and returns the top of the stack or -1 if the stack is empty.
# void inc(int k, int val) Increments the bottom k elements of the stack by val. If there are less than k elements in the stack, increment all the elements in the stack.

# Example 1:

# Input
# ["CustomStack","push","push","pop","push","push","push","increment","increment","pop","pop","pop","pop"]
# [[3],[1],[2],[],[2],[3],[4],[5,100],[2,100],[],[],[],[]]
# Output
# [null,null,null,2,null,null,null,null,null,103,202,201,-1]

# Constraints:
# 1 <= maxSize, x, k <= 1000
# 0 <= val <= 100
# At most 1000 calls will be made to each method of increment, push and pop each separately.

class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)
        print(self.stack)
    
    def pop(self) -> int:
        if self.stack:
            self.stack.pop()
            print(self.stack)
            return self.stack
        return -1
    
    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, len(self.stack))):
            self.stack[i] += val
            print(self.stack)


stk = CustomStack(3)
stk.push(1)
stk.push(2)
stk.pop()
stk.push(2)
stk.push(3)
stk.push(4)
stk.increment(5, 100)
stk.increment(2, 100)
stk.pop()
stk.pop()
stk.pop()
stk.pop()