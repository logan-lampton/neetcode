# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

# Example 1:
# Input: root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: true

# Example 2:
# Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
# Output: false

# Constraints:
# The number of nodes in the root tree is in the range [1, 2000].
# The number of nodes in the subRoot tree is in the range [1, 1000].
# -104 <= root.val <= 104
# -104 <= subRoot.val <= 104

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: [TreeNode], subRoot: [TreeNode]) -> bool:
        
        def identical(tree1, tree2):
            if not tree1 and not tree2:
                return True

            if not tree1 or not tree2:
                return False

            if tree1.val != tree2.val:
                return False

            left_identical = identical(tree1.left, tree2.left)
            right_identical = identical(tree1.right, tree2.right)
            
            return left_identical and right_identical
            
        def dfs(node):
            if not node:
                return False

            if node.val == subRoot.val and identical(node, subRoot):
                return True

            return dfs(node.left) or dfs(node.right)
        
        return dfs(root)