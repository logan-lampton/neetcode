# Given the root of a binary tree, return its maximum depth.
#
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest
# leaf node.

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: 3

# Example 2:
# Input: root = [1,null,2]
# Output: 2

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# ---- Recursive Solution ----

class Solution(object):
    def maxDepth_r(self, root):
        if not root:
            return 0

        # call the function recursively on the left side
        left_depth = self.maxDepth_r(root.left)
        # call the function recursively on the right side
        right_depth = self.maxDepth_r(root.right)

        # return the larger value of the two calls (+1 for the root)
        return max(left_depth, right_depth) + 1


# ---- Solution using stack ----

class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0

        depth = 0
        # queue begins with the root node inside
        queue = [root]

        while queue:
            level_depth = len(queue)

            for _ in range(level_depth):
                # dequeue the front node
                node = queue.pop(0)

                # if there is a node on the left, enqueue it (add it to the queue)
                if node.left:
                    queue.append(node.left)
                # if there is a node on the right, enqueue it
                if node.right:
                    queue.append(node.right)

            depth += 1

        return depth



