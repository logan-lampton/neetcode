# Given a binary array nums, return the maximum number of consecutive 1's in the array.

# Example 1:
# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

# Example 2:
# Input: nums = [1,0,1,1,0,1]
# Output: 2

# Constraints:
# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.


class Solution:
    def findMaxConsecutiveOnes(self, nums: [int]) -> int:
        max_consecutive_ones = 0
        cur_consecutive_ones = 0
        for number in nums:
            if number == 1:
                cur_consecutive_ones += 1
            else:
                cur_consecutive_ones = 0
            if cur_consecutive_ones > max_consecutive_ones:
                max_consecutive_ones = cur_consecutive_ones
        return max_consecutive_ones


solution = Solution()
print(solution.findMaxConsecutiveOnes(nums = [1,1,0,1,1,1]))
print(solution.findMaxConsecutiveOnes(nums = [1,0,1,1,0,1]))