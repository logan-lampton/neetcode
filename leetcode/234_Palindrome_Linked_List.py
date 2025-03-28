# Given the head of a singly linked list, return true if it is a
# palindrome or false otherwise.

# Example 1:
# Input: head = [1,2,2,1]
# Output: true

# Example 2:
# Input: head = [1,2]
# Output: false

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: [ListNode]) -> bool:
        # convert linked list to list of values
        values = []
        while head:
            values.append(head.val)
            head = head.next

        # left and right pointers
        left = 0
        right = len(values) - 1

        # compare the lists to return True or False
        while left < right:
            if values[left] != values[right]:
                return False
            left += 1
            right -= 1

        return True

    # Slow/Fast Method:
    # slow = head
    # fast = head

    # while fast and fast.next:
    #     fast = fast.next.next
    #     slow = slow.next

    # prev = None
    # curr = slow
    # while curr:
    #     next_node = curr.next
    #     curr.next = prev
    #     prev = curr
    #     curr = next_node

    # while prev:
    #     if head.val != prev.val:
    #         return False
    #     head = head.next
    #     prev = prev.next

    # return True

# Practice
class Solution:
    def isPalindrome(self, head: [ListNode]) -> bool:
        values = []

        cur_node = head
        while cur_node:
            values.append(cur_node.val)
            cur_node = cur_node.next
        
        left = 0
        right = len(values) - 1

        while left < right:
            if values[left] != values[right]:
                return False
            left += 1
            right -= 1
        
        return True