# Given the root of a binary tree, return the postorder traversal of its nodes' values.

# Example 1:
# Input: root = [1,null,2,3]
# Output: [3,2,1]

# Example 2:
# Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
# Output: [4,6,7,5,2,9,8,3,1]

# Example 3:
# Input: root = []
# Output: []

# Example 4:
# Input: root = [1]
# Output: [1]

# Constraints:
# The number of the nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: [TreeNode]) -> [int]:

        if root == None:
            return []

        stack = [root]
        backwards_answer = []
        
        while stack:
            cur_node = stack.pop()
            backwards_answer.append(cur_node.val)
            if cur_node.left:
                stack.append(cur_node.left)
            if cur_node.right:
                stack.append(cur_node.right)
        
        return backwards_answer[::-1]
    

# Practice recursive
class Solution:
    def postorderTraversal(self, root: [TreeNode]) -> [int]:
        answer = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            answer.append(node.val)
        
        dfs(root)
        return answer