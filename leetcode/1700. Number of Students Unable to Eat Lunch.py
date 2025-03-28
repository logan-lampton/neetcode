# The school cafeteria offers circular and square sandwiches at lunch break, referred to by numbers 0 and 1 respectively. All students stand in a queue. Each student either prefers square or circular sandwiches.

# The number of sandwiches in the cafeteria is equal to the number of students. The sandwiches are placed in a stack. At each step:

# If the student at the front of the queue prefers the sandwich on the top of the stack, they will take it and leave the queue.
# Otherwise, they will leave it and go to the queue's end.
# This continues until none of the queue students want to take the top sandwich and are thus unable to eat.

# You are given two integer arrays students and sandwiches where sandwiches[i] is the type of the i​​​​​​th sandwich in the stack (i = 0 is the top of the stack) and students[j] is the preference of the j​​​​​​th student in the initial queue (j = 0 is the front of the queue). Return the number of students that are unable to eat.

# Example 1:
# Input: students = [1,1,0,0], sandwiches = [0,1,0,1]
# Output: 0 

# Example 2:
# Input: students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]
# Output: 3

# Constraints:
# 1 <= students.length, sandwiches.length <= 100
# students.length == sandwiches.length
# sandwiches[i] is 0 or 1.
# students[i] is 0 or 1.


from typing import List

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        counts = [0, 0]
        for sandwich_preference in students:
            counts[sandwich_preference] += 1
        
        remaining = len(sandwiches)

        for sandwich in sandwiches:
            if counts[sandwich] == 0:
                break
            if remaining == 0:
                break
            counts[sandwich] -= 1
            remaining -= 1
        
        return remaining


solution = Solution()
print(solution.countStudents(students = [1,1,0,0], sandwiches = [0,1,0,1]))
print(solution.countStudents(students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]))