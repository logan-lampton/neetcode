# Given two binary search trees root1 and root2, return a list containing all the integers from both trees sorted in ascending order.

# Example 1:
# Input: root1 = [2,1,4], root2 = [1,0,3]
# Output: [0,1,1,2,3,4]

# Example 2:
# Input: root1 = [1,null,8], root2 = [8,1]
# Output: [1,1,8,8]

# Constraints:
# The number of nodes in each tree is in the range [0, 5000].
# -105 <= Node.val <= 105


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> [int]:
        
        def bfs(root):
            if not root:
                return []
            queue = [root]
            result = []
            while queue:
                node = queue.pop(0)
                result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            return result
        
        list1 = bfs(root1)
        list2 = bfs(root2)

        full_list = list1 + list2

        full_list.sort()

        return full_list
    

# Example
root1 = TreeNode(2)
root1.left = TreeNode(1)
root1.right = TreeNode(4)

root2 = TreeNode(1)
root2.left = TreeNode(0)
root2.right = TreeNode(3)

solution = Solution()
result = solution.getAllElements(root1, root2)
print(result)