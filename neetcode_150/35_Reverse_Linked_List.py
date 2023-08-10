# Given the head of a singly linked list, reverse the list, and return the reversed list.
#
# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Example 2:
# Input: head = [1,2]
# Output: [2,1]

# Example 3:
# Input: head = []
# Output: []

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseList(self, head):
        # the last element of the singly linked list is None, so it is the first in the reverse
        new_list = None
        current = head

        # current == True as long as it is not the last value (None)
        while current:
            # point the next_node to current.next
            next_node = current.next
            # point current.next to the new list
            current.next = new_list
            # update new_list to point at current, so that it's always pointing to the new head of the reversed list
            new_list = current
            current = next_node

        return new_list
