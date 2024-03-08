# A binary tree is uni-valued if every node in the tree has the same value.

# Given the root of a binary tree, return true if the given tree is uni-valued, or false otherwise.

# Example 1:
# Input: root = [1,1,1,1,1,null,1]
# Output: true

# Example 2:
# Input: root = [2,2,2,5,2]
# Output: false

# Constraints:
# The number of nodes in the tree is in the range [1, 100].
# 0 <= Node.val < 100


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        
        queue = []
        if root:
            queue.append(root)
        while queue:
            for _ in queue:
                node = queue.pop(0)
                if node.val != root.val:
                    return False
                else:
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
        return True