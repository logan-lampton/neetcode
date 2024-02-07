# Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

# Implement the MyQueue class:
# void push(int x) Pushes element x to the back of the queue.
# int pop() Removes the element from the front of the queue and returns it.
# int peek() Returns the element at the front of the queue.
# boolean empty() Returns true if the queue is empty, false otherwise.

# Notes:
# You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
# Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.

# Example 1:
# Input
# ["MyQueue", "push", "push", "peek", "pop", "empty"]
# [[], [1], [2], [], [], []]
# Output
# [null, null, null, 1, 1, false]

# Explanation
# MyQueue myQueue = new MyQueue();
# myQueue.push(1); // queue is: [1]
# myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
# myQueue.peek(); // return 1
# myQueue.pop(); // return 1, queue is [2]
# myQueue.empty(); // return false

# Constraints:
# 1 <= x <= 9
# At most 100 calls will be made to push, pop, peek, and empty.
# All the calls to pop and peek are valid.


class MyQueue:
    def __init__(self):
        self.enque_stack = []
        self.deque_stack = []
        self.front = None

    def push(self, x: int):
        if not self.enque_stack:
            self.front = x
        self.enque_stack.append(x)

    def pop(self):
        if not self.deque_stack:
            while self.enque_stack:
                self.deque_stack.append(self.enque_stack.pop())
        return self.deque_stack.pop()

    def peek(self):
        if self.deque_stack:
            return self.deque_stack[-1]
        return self.front

    def empty(self):
        return not self.enque_stack and not self.deque_stack


# Another strategy I later wrote:
# class MyQueue:

#     def __init__(self):
#         self.front = []
#         self.back = []


#     def push(self, x: int) -> None:
#         self.back.append(x)


#     def pop(self) -> int:

#         while self.back:
#             self.front.append(self.back.pop())

#         answer = self.front.pop()

#         while self.front:
#             self.back.append(self.front.pop())

#         return answer


#     def peek(self) -> int:
#         return self.back[0]


#     def empty(self) -> bool:
#         return not self.front and not self.back
