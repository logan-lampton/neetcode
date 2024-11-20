# Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.

# If the tree has more than one mode, return them in any order.

# Assume a BST is defined as follows:
# The left subtree of a node contains only nodes with keys less than or equal to the node's key.
# The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
# Both the left and right subtrees must also be binary search trees.

# Example 1:
# Input: root = [1,null,2,2]
# Output: [2]

# Example 2:
# Input: root = [0]
# Output: [0]

# Constraints:
# The number of nodes in the tree is in the range [1, 104].
# -105 <= Node.val <= 105


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: [TreeNode]) -> [int]:
        stack = [root]
        hashmap = {}

        while stack:
            cur_node = stack.pop(0)
            if cur_node.left:
                stack.append(cur_node.left)
            if cur_node.right:
                stack.append(cur_node.right)
            if cur_node.val in hashmap:
                hashmap[cur_node.val] += 1
            else:
                hashmap[cur_node.val] = 1
        
        tuples = []
        max_value = 0
        for key, value in hashmap.items():
            tuples.append((key, value))
            if value > max_value:
                max_value = value
        
        output = []
        max_tuple_amount = max_value

        for cur_tuple in tuples:
            if cur_tuple[1] == max_tuple_amount:
                output.append(cur_tuple[0])
        
        return output
