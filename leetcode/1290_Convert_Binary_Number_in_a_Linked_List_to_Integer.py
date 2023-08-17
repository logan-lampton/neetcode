# Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0
# or 1. The linked list holds the binary representation of a number.

# Return the decimal value of the number in the linked list.

# The most significant bit is at the head of the linked list.

# Example 1:
# Input: head = [1,0,1]
# Output: 5
# Explanation: (101) in base 2 = (5) in base 10
# Example 2:
#
# Input: head = [0]
# Output: 0

# Definition for singly - linked list:
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def getDecimalValue(self, head):
        # integers are in base 10;
        # the int method can take the num and base (2, for binary) as arguments to convert to integers
        # int(num, 2)

        binary_string = ''

        while head:
            binary_string += str(head.val)
            head = head.next

        answer = int(binary_string, 2)

        return answer


# Testing the solution:

# Create a binary linked list:
linked_list = ListNode(1)
linked_list.next = ListNode(0)
linked_list.next.next = ListNode(1)

# Create an instance of the Solution class:
solution = Solution()

# Call the getDecimalValue function/print the result:
result = solution.getDecimalValue(linked_list)
print(result)
