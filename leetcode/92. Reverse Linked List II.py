# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

# Example 1:
# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]

# Example 2:
# Input: head = [5], left = 1, right = 1
# Output: [5]

# Constraints:
# The number of nodes in the list is n.
# 1 <= n <= 500
# -500 <= Node.val <= 500
# 1 <= left <= right <= n


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: [ListNode], left: int, right: int) -> [ListNode]:
        
        if not head or left == right:
            return head

        dummy_head = ListNode(0, head)  # Dummy node to handle edge cases
        before_sublist = dummy_head  # Pointer to node before the sublist to be reversed

        # Move before_sublist to the node just before the `left` position
        for _ in range(left - 1):
            before_sublist = before_sublist.next

        current_node = before_sublist.next  # First node in the sublist to be reversed

        # Reverse the sublist using in-place swapping
        for _ in range(right - left):
            temp_node = current_node.next  # Node to be moved forward
            current_node.next = temp_node.next  # Remove temp_node from the current position
            temp_node.next = before_sublist.next  # Insert temp_node at the front of sublist
            before_sublist.next = temp_node  # Update the head of the sublist

        return dummy_head.next  # Return the new head of the list

# Practice
class Solution:
    def reverseBetween(self, head: [ListNode], left: int, right: int) -> [ListNode]:
        
        if not head or left == right:
            return head

        prev_node = None
        cur_node = head

        for _ in range(left - 1):
            prev_node = cur_node
            cur_node = cur_node.next
        
        start_node = cur_node
        reverse_prev = None

        for _ in range(right - left + 1):
            next_node = cur_node.next
            cur_node.next = reverse_prev
            reverse_prev = cur_node
            cur_node = next_node
        
        if prev_node:
            prev_node.next = reverse_prev
        else:
            head = reverse_prev
        
        start_node.next = cur_node
        
        return head