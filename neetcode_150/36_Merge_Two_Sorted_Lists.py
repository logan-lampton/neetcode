# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two
# lists.

# Return the head of the merged linked list.

# Example 1:
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Example 2:
# Input: list1 = [], list2 = []
# Output: []

# Example 3:
# Input: list1 = [], list2 = [0]
# Output: [0]


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        # make dummy ListNode, to test any edgecases with the tail of the list
        dummy = ListNode()
        tail = dummy

        # while both lists have values (are non-Null, and therefore both True), we compare them
        while list1 and list2:
            # if the current list1 value is less than the current list2 value
            if list1.val < list2.val:
                # make the next value of tail into list1
                tail.next = list1
                # reset the pointer of list1 to the next list1 value
                list1 = list1.next
            else:
                # if list2.value is less, set the next tail value to list2 value
                tail.next = list2
                # then set the point for list2 to the next list2 value
                list2 = list2.next
            # no matter what, we want to set the tail pointer to be the new tail.next value, whether that is list1 or
            # list2, depending on which was smaller
            tail = tail.next

        # once the lists are fully compared, we want to see if one of the lists still has values;
        # if one of the lists does, we want to add those values to the end of the combined list
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next
