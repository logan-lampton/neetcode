# Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

# You should preserve the original relative order of the nodes in each of the two partitions.

# Example 1:
# Input: head = [1,4,3,2,5,2], x = 3
# Output: [1,2,2,4,3,5]

# Example 2:
# Input: head = [2,1], x = 2
# Output: [1,2]

# Constraints:
# The number of nodes in the list is in the range [0, 200].
# -100 <= Node.val <= 100
# -200 <= x <= 200

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def partition(self, head: [ListNode], x: int) -> [ListNode]:
        if not head:
            return head
        
        values_less = []
        values_equal_or_more = []

        cur_node = head
        while cur_node:
            if cur_node.val < x:
                values_less.append(cur_node)
            else:
                values_equal_or_more.append(cur_node)
            cur_node = cur_node.next

        if values_less:
            for i in range(len(values_less) - 1):
                values_less[i].next = values_less[i + 1]
            values_less[-1].next = None
        if values_equal_or_more:
            for i in range(len(values_equal_or_more) - 1):
                values_equal_or_more[i].next = values_equal_or_more[i + 1]
            values_equal_or_more[-1].next = None
        
        if values_less and values_equal_or_more:
            values_less[-1].next = values_equal_or_more[0]
        
        if values_less:
            return values_less[0]
        return values_equal_or_more[0]
        