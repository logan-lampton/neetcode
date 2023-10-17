# You have n binary tree nodes numbered from 0 to n - 1 where node i has two children leftChild[i] and rightChild[i], return true if and only if
# all the given nodes form exactly one valid binary tree.

# If node i has no left child then leftChild[i] will equal -1, similarly for the right child.

# Note that the nodes have no values and that we only use the node numbers in this problem.

# Example 1:
# Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
# Output: true

# Example 2:
# Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]
# Output: false

# Example 3:
# Input: n = 2, leftChild = [1,0], rightChild = [-1,-1]
# Output: false

# Constraints:
# n == leftChild.length == rightChild.length
# 1 <= n <= 104
# -1 <= leftChild[i], rightChild[i] <= n - 1


class Solution:
    def validateBinaryTreeNodes(
        self, n: int, leftChild: [int], rightChild: [int]
    ) -> bool:
        # set of numbers we expect to see in the tree
        nodeSet = {i for i in range(n)}

        # loop through both child lists and remove any values that appear from the set.  If a value appears more than once, return false
        for i in range(n):
            if leftChild[i] != -1:
                if leftChild[i] in nodeSet:
                    nodeSet.discard(leftChild[i])
                else:
                    return False
            if rightChild[i] != -1:
                if rightChild[i] in nodeSet:
                    nodeSet.discard(rightChild[i])
                else:
                    return False

        # if there is only one element remaining in the set(meaning it did not appear in the list of children), that is our root.  If there are more or less than 1 element, return false.
        if len(nodeSet) != 1:
            return False
        root = nodeSet.pop()

        # starting at the root node, push any children of that node into the stack and increment the number of nodes encountered
        node_stack = [root]
        visited_count = 0

        while node_stack:
            cur_node = node_stack.pop()
            if leftChild[cur_node] != -1:
                node_stack.append(leftChild[cur_node])
                visited_count += 1
            if rightChild[cur_node] != -1:
                node_stack.append(rightChild[cur_node])
                visited_count += 1

        # # if we encountered every node, return True. Otherwise return False.
        return visited_count == n - 1
