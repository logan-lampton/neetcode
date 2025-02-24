# Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

# Example 1:
# Input: nums = [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.

# Example 2:
# Input: nums = [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

# Constraints:
# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.


from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hashmap = {}
        cur_sum = 0
        max_length = 0

        for i, num in enumerate(nums):
            if num == 1:
                cur_sum += 1
            else:
                cur_sum -= 1
            if cur_sum == 0:
                max_length = i + 1
            if cur_sum in hashmap:
                cur_length = i - hashmap[cur_sum]
                if max_length < cur_length:
                    max_length = cur_length
            else:
                hashmap[cur_sum] = i
        
        return max_length
    

solution = Solution()
print(solution.findMaxLength(nums = [0,1]))
print(solution.findMaxLength(nums = [0,1,0]))