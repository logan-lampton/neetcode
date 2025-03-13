# Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

# Example 1:
# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.

# Example 2:
# Input: target = 4, nums = [1,4,4]
# Output: 1

# Example 3:
# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0

# Constraints:
# 1 <= target <= 109
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 104


from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_array_len = float('inf')
        cur_sum = 0
        left = 0

        for right in range(len(nums)):
            cur_sum += nums[right]

            while cur_sum >= target:
                cur_array_len = right - left + 1
                if min_array_len > cur_array_len:
                    min_array_len = cur_array_len
                cur_sum -= nums[left]
                left += 1

        if min_array_len == float('inf'):
            return 0
        return min_array_len
    

solution = Solution()
print(solution.minSubArrayLen(target = 7, nums = [2,3,1,2,4,3]))
print(solution.minSubArrayLen(target = 4, nums = [1,4,4]))
print(solution.minSubArrayLen(target = 11, nums = [1,1,1,1,1,1,1,1]))