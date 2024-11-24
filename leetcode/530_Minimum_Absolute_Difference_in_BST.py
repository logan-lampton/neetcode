# Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

# Example 1:
# Input: root = [4,2,6,1,3]
# Output: 1

# Example 2:
# Input: root = [1,0,48,null,null,12,49]
# Output: 1

# Constraints:
# The number of nodes in the tree is in the range [2, 104].
# 0 <= Node.val <= 105


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: [TreeNode]) -> int:
        values = []
        stack = [root]
        while stack:
            cur_node = stack.pop(0)
            if cur_node.left:
                stack.append(cur_node.left)
            if cur_node.right:
                stack.append(cur_node.right)
            values.append(cur_node.val)
        
        sorted_values = sorted(values)

        min_value = sorted_values[1] - sorted_values[0]
        for i in range(2, len(sorted_values)):
            cur_dif = sorted_values[i] - sorted_values[i - 1]
            if cur_dif < min_value:
                min_value = cur_dif
        
        return min_value
