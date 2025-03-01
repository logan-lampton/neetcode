# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

# Example 1:
# Input: head = [1,1,2]
# Output: [1,2]

# Example 2:
# Input: head = [1,1,2,3,3]
# Output: [1,2,3]

# Constraints:
# The number of nodes in the list is in the range [0, 300].
# -100 <= Node.val <= 100
# The list is guaranteed to be sorted in ascending order.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: [ListNode]) -> [ListNode]:
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head
    

  # Practice:
  # class Solution:
  #   def deleteDuplicates(self, head: [ListNode]) -> [ListNode]:

  #       if not head:
  #           return head
        
  #       seen = set()
  #       seen.add(head.val)
  #       cur_node = head

  #       while cur_node and cur_node.next:
  #           if cur_node.next.val in seen:
  #               cur_node.next = cur_node.next.next
  #           else:
  #               seen.add(cur_node.next.val)
  #               cur_node = cur_node.next

  #       return head