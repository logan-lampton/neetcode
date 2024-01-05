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
# def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

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
