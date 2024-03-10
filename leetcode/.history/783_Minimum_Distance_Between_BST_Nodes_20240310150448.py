# Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two
# different nodes in the tree.

# Example 1:
# Input: root = [4,2,6,1,3]
# Output: 1

# Example 2:
# Input: root = [1,0,48,null,null,12,49]
# Output: 1

# Constraints:
# The number of nodes in the tree is in the range [2, 100].
# 0 <= Node.val <= 105


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST(self, root: [TreeNode]) -> int:

        min_range = float(inf)
        previous = None

        def find_min(node):
            nonlocal min_range
            nonlocal previous

            if node is None:
                return
            elif node.left:
                find_min(node.left)
            if previous is not None:
                min_range = min(min_range, node.val - previous)
            previous = node.val
            if node.right:
                find_min(node.right)

        find_min(root)
        return min_range
