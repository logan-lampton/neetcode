# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Example 1:
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]

# Example 2:
# Input: head = [1], n = 1
# Output: []

# Example 3:
# Input: head = [1,2], n = 1
# Output: [1]

# Constraints:
# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: [ListNode], n: int) -> [ListNode]:
        
        nodes = []
        cur_node = head

        while cur_node:
            nodes.append(cur_node)
            cur_node = cur_node.next
        
        target_index = len(nodes) - n

        if target_index == 0:
            return head.next

        prev_node = nodes[target_index - 1]
        if prev_node.next.next:
            prev_node.next = prev_node.next.next
        else:
            prev_node.next = None
        
        return head