# Given the root of a binary tree, return the inorder traversal of its nodes' values.

# Example 1:
# Input: root = [1,null,2,3]
# Output: [1,3,2]

# Example 2:
# Input: root = []
# Output: []

# Example 3:
# Input: root = [1]
# Output: [1]

# Constraints:
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: [TreeNode]) -> [int]:

        if not root:
            return []

        stack = []
        answer = []
        current_node = root

        while stack or current_node:
            while current_node:
                stack.append(current_node)
                current_node = current_node.left

            working_on_node = stack.pop()
            answer.append(working_on_node.val)

            current_node = working_on_node.right

        return answer


node3 = TreeNode(3)
node2 = TreeNode(2, left=node3)
node1 = TreeNode(1, right=node2)

solution = Solution()
print(solution.inorderTraversal(root=node1))


# Practice
class Solution:
    def inorderTraversal(self, root: [TreeNode]) -> [int]:
        values = []
        stack = []
        cur_node = root

        while cur_node or stack:
            while cur_node:
                stack.append(cur_node)
                cur_node = cur_node.left
            
            cur_node = stack.pop()
            values.append(cur_node.val)

            cur_node = cur_node.right
        
        return values