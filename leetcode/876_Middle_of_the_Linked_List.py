# Given the head of a singly linked list, return the middle node of the linked list.

# If there are two middle nodes, return the second middle node.

# Example 1:

# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.
# Example 2:

# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
# Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

# Constraints:

# The number of nodes in the list is in the range [1, 100].
# 1 <= Node.val <= 100


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: [ListNode]) -> [ListNode]:
        count = 1
        current_node = head

        while current_node.next:
            count += 1
            current_node = current_node.next

        current_node = head

        for _ in range(int(count // 2)):
            current_node = current_node.next


# Version using an array that I came up with:
# def middleNode(self, head: [ListNode]) -> [ListNode]:

#     curr = head
#     full_array = []

#     while curr:
#         next_node = curr.next
#         full_array.append(curr.val)
#         curr = next_node

#     target = len(full_array) // 2 + 1

#     curr = head

#     for i in range(target - 1):
#         next_node = curr.next
#         curr = next_node

#     return curr

# Practice
class Solution:
    def middleNode(self, head: [ListNode]) -> [ListNode]:
        cur_node = head
        length = 0

        while cur_node:
            length += 1
            cur_node = cur_node.next
        
        this_node = head
        seen_nodes = 0
        target_length = length // 2

        while seen_nodes < target_length:
            seen_nodes += 1
            this_node = this_node.next

        return this_node


# Practice
class Solution:
    def middleNode(self, head: [ListNode]) -> [ListNode]:
        length = 0
        cur_node = head

        while cur_node:
            length += 1
            cur_node = cur_node.next
        
        cur_length_node = head
        check_length = 0
        
        while check_length < (length // 2):
            check_length += 1
            cur_length_node = cur_length_node.next
        
        return cur_length_node