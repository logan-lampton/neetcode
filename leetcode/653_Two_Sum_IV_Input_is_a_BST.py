# Given the root of a binary search tree and an integer k, return true if there exist two elements in 
# the BST such that their sum is equal to k, or false otherwise.

# Example 1:
# Input: root = [5,3,6,2,4,null,7], k = 9
# Output: true

# Example 2:
# Input: root = [5,3,6,2,4,null,7], k = 28
# Output: false

# Constraints:
# The number of nodes in the tree is in the range [1, 104].
# -104 <= Node.val <= 104
# root is guaranteed to be a valid binary search tree.
# -105 <= k <= 105


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        queue = []
        val_hash = {}

        if root:
            queue.append(root)
        
        while queue:
            for _ in range(len(queue)):
                node = queue.pop()
                val_hash[node] = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        if len(val_hash) <= 1:
            return False

        sorted_vals = sorted(val_hash.values())

        left = 0
        right = len(sorted_vals) - 1

        while left < right:
            if sorted_vals[left] + sorted_vals[right] == k:
                return True
            elif sorted_vals[left] + sorted_vals[right] < k:
                left += 1
            else:
                right -= 1
            
        return False
