# You are given the head of a linked list.

# Remove every node which has a node with a greater value anywhere to the right side of it.

# Return the head of the modified linked list.

# Example 1:
# Input: head = [5,2,13,3,8]
# Output: [13,8]
# Explanation: The nodes that should be removed are 5, 2 and 3.
# - Node 13 is to the right of node 5.
# - Node 13 is to the right of node 2.
# - Node 8 is to the right of node 3.

# Example 2:
# Input: head = [1,1,1,1]
# Output: [1,1,1,1]
# Explanation: Every node has value 1, so no nodes are removed.

# Constraints:
# The number of the nodes in the given list is in the range [1, 105].
# 1 <= Node.val <= 105

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = []
        cur_node = head

        while cur_node:
            values.append(cur_node.val)
            cur_node = cur_node.next
        
        final_values = []
        greatest_value = values[-1]

        for i in range(len(values) - 1, - 1, - 1):
            if values[i] < greatest_value:
                continue
            else:
                final_values.append(values[i])
            if values[i] > greatest_value:
                greatest_value = values[i]

        answer_nodes = []
        for i in range(len(final_values) - 1, - 1, - 1):
            answer_nodes.append(ListNode(final_values[i]))
        
        for i in range(len(answer_nodes) - 1):
            answer_nodes[i].next = answer_nodes[i + 1]
        
        return answer_nodes[0]