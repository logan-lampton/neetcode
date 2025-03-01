# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Example 2:
# Input: head = [1,2]
# Output: [2,1]

# Example 3:
# Input: head = []
# Output: []

# Constraints:
# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: [ListNode]) -> [ListNode]:
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev


# Practice:
class Solution:
    def reverseList(self, head: [ListNode]) -> [ListNode]:
        
        prev = None
        cur_node = head

        while cur_node:
            # save the next node, to point to a little later
            next_node = cur_node.next
            # set cur_node to point to prev node
            cur_node.next = prev
            # move prev node forward
            prev = cur_node
            # move cur_node forward
            cur_node = next_node
        
        return prev