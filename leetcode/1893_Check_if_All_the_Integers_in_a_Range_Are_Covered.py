# You are given a 2D integer array ranges and two integers left and right. Each ranges[i] = [starti, endi] represents an inclusive interval between starti and endi.

# Return true if each integer in the inclusive range [left, right] is covered by at least one interval in ranges. Return false otherwise.

# An integer x is covered by an interval ranges[i] = [starti, endi] if starti <= x <= endi.

# Example 1:
# Input: ranges = [[1,2],[3,4],[5,6]], left = 2, right = 5
# Output: true
# Explanation: Every integer between 2 and 5 is covered:
# - 2 is covered by the first range.
# - 3 and 4 are covered by the second range.
# - 5 is covered by the third range.

# Example 2:
# Input: ranges = [[1,10],[10,20]], left = 21, right = 21
# Output: false
# Explanation: 21 is not covered by any range.

# Constraints:
# 1 <= ranges.length <= 50
# 1 <= starti <= endi <= 50
# 1 <= left <= right <= 50


class Solution:
    def isCovered(self, ranges: [[int]], left: int, right: int) -> bool:
        answer_range = []
        for num in range(left, right + 1):
            answer_range.append(num)
        
        for i in range(len(ranges)):
            for num in range(ranges[i][0], ranges[i][1] + 1):
                if num in answer_range:
                    answer_range.remove(num)
        
        if len(answer_range) == 0:
            return True
        return False
    

solution = Solution()
print(solution.isCovered(ranges = [[1,2],[3,4],[5,6]], left = 2, right = 5))
print(solution.isCovered(ranges = [[1,10],[10,20]], left = 21, right = 21))