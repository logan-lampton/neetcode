# Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.

# Example 1:
# Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
# Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

# Example 2:
# Input: root = [5,1,7]
# Output: [1,null,5,null,7]

# Constraints:
# The number of nodes in the given tree will be in the range [1, 100].
# 0 <= Node.val <= 1000


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: [TreeNode]) -> [TreeNode]:
        
        def in_order_traversal(node):
            if not node:
                return
            in_order_traversal(node.left)
            self.cur.right = TreeNode(node.val)
            self.cur = self.cur.right
            in_order_traversal(node.right)

        dummy = TreeNode()
        self.cur = dummy

        in_order_traversal(root)
        return dummy.right

# Practice
class Solution:
    def increasingBST(self, root: [TreeNode]) -> [TreeNode]:
        
        ordered_array = []

        def inorder(node, array) -> None:
            if node is None:
                return
            inorder(node.left, array)
            ordered_array.append(node.val)
            inorder(node.right, array)

        inorder(root, ordered_array)

        dummy = TreeNode(-1)
        current_node = dummy

        for val in ordered_array:
            current_node.right = TreeNode(val)
            current_node = current_node.right
        
        return dummy.right