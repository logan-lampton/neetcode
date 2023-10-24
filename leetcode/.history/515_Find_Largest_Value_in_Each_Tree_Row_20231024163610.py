# Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

# Example 1:
# Input: root = [1,3,2,5,3,null,9]
# Output: [1,3,9]

# Example 2:
# Input: root = [1,2,3]
# Output: [1,3]

# Constraints:
# The number of nodes in the tree will be in the range [0, 104].
# -231 <= Node.val <= 231 - 1


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: [TreeNode]) -> [int]:
        max_level_values = []
        if root is None:
            return max_level_values
        queue = []
        queue.append(root)

        while queue:
            size = len(queue)
            level_max = float("-inf")

            while size > 0:
                curr_node = queue.pop(0)
                level_max = max(curr_node.val, level_max)

                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
                size -= 1

            max_level_values.append(level_max)

        return max_level_values
