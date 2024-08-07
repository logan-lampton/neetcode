# Given the head of a linked list head, in which each node contains an integer value.

# Between every pair of adjacent nodes, insert a new node with a value equal to the greatest common divisor of them.

# Return the linked list after insertion.

# The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.

# Example 1:
# Input: head = [18,6,10,3]
# Output: [18,6,6,2,10,1,3]
# Explanation: The 1st diagram denotes the initial linked list and the 2nd diagram denotes the linked list after inserting the new nodes (nodes in blue are the inserted nodes).
# - We insert the greatest common divisor of 18 and 6 = 6 between the 1st and the 2nd nodes.
# - We insert the greatest common divisor of 6 and 10 = 2 between the 2nd and the 3rd nodes.
# - We insert the greatest common divisor of 10 and 3 = 1 between the 3rd and the 4th nodes.
# There are no more adjacent nodes, so we return the linked list.

# Example 2:
# Input: head = [7]
# Output: [7]
# Explanation: The 1st diagram denotes the initial linked list and the 2nd diagram denotes the linked list after inserting the new nodes.
# There are no pairs of adjacent nodes, so we return the initial linked list.

# Constraints:
# The number of nodes in the list is in the range [1, 5000].
# 1 <= Node.val <= 1000


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertGreatestCommonDivisors(self, head: [ListNode]) -> [ListNode]:
        current = head
        every_other = True

        def find_gcd(value1, value2):
            while value1 != 0  and value2 != 0:
                if value1 > value2:
                    value1 %= value2
                else:
                    value2 %= value1
            return value1 + value2

        while current and current.next:
            if every_other:
                new_node = ListNode(val=find_gcd(current.val, current.next.val), next=current.next)
                current.next = new_node
                current = current.next
                every_other = False
            else:
                current = current.next
                every_other = True
        return head

node4 = ListNode(val=3, next=None)
node3 = ListNode(val=10, next=node4)
node2 = ListNode(val=6, next=node3)
node1 = ListNode(val=18, next=node2)

solution = Solution()
answer = solution.insertGreatestCommonDivisors(node1)

current = answer
printed_answer = []
while current:
    printed_answer.append(current.val)
    current = current.next
print(printed_answer)
