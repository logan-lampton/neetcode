# You are given an m x n matrix M initialized with all 0's and an array of operations ops, where ops[i] = [ai, bi] means M[x][y] should be incremented by one for all 0 <= x < ai and 0 <= y < bi.

# Count and return the number of maximum integers in the matrix after performing all the operations.

# Example 1:
# Input: m = 3, n = 3, ops = [[2,2],[3,3]]
# Output: 4
# Explanation: The maximum integer in M is 2, and there are four of it in M. So return 4.

# Example 2:
# Input: m = 3, n = 3, ops = [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]]
# Output: 4

# Example 3:
# Input: m = 3, n = 3, ops = []
# Output: 9

# Constraints:
# 1 <= m, n <= 4 * 104
# 0 <= ops.length <= 104
# ops[i].length == 2
# 1 <= ai <= m
# 1 <= bi <= n


class Solution:
    def maxCount(self, m: int, n: int, ops: [[int]]) -> int:
        if not ops:
            return m * n
        
        ops.sort()
        
        smallest_column = float('inf')

        for op in ops:
            if op[1] < smallest_column:
                smallest_column = op[1]
        
        return ops[0][0] * smallest_column


solution = Solution()
print(solution.maxCount(m = 3, n = 3, ops = [[2,2],[3,3]]))
print(solution.maxCount(m = 3, n = 3, ops = [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]]))
print(solution.maxCount(m = 18, n = 3, ops = [[16,1],[14,3],[14,2],[4,1],[10,1],[11,1],[8,3],[16,2],[13,1],[8,3],[2,2],[9,1],[3,1],[2,2],[6,3]]))