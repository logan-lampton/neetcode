# Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

# Example 1:
# Input: head = [1,2,3,4]
# Output: [2,1,4,3]

# Example 2:
# Input: head = []
# Output: []

# Example 3:
# Input: head = [1]
# Output: [1]

# Example 4:
# Input: head = [1,2,3]
# Output: [2,1,3]

# Constraints:
# The number of nodes in the list is in the range [0, 100].
# 0 <= Node.val <= 100


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: [ListNode]) -> [ListNode]:

        if not head:
            return head

        nodes = []
        cur_node = head

        while cur_node:
            nodes.append(cur_node)
            cur_node = cur_node.next
        
        for i in range(1, len(nodes), 2):
            temp = nodes[i]
            nodes[i] = nodes[i - 1]
            nodes[i - 1] = temp
        
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        
        nodes[-1].next = None

        return nodes[0]