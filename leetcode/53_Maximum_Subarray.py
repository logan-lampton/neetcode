# Given an integer array nums, find the subarray with the largest sum, and return its sum.

# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.

# Example 2:
# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.

# Example 3:
# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

# Constraints:
# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104


def maxSubArray(nums: [int]) -> int:
    dp = [nums[0]] * len(nums)

    for i in range(1, len(nums)):
        # if the sum of the number before and current number are greater than the current number
        if nums[i] + dp[i - 1] >= nums[i]:
            dp[i] = nums[i] + dp[i - 1]
        else:
            dp[i] = nums[i]

    return max(dp)

# additional practice:
def maxSubArray(self, nums: [int]) -> int:
        
        dp = [nums[0]] * len(nums)

        for i in range(1, len(nums)):
            cur_num = nums[i]
            prev_dp = dp[i - 1]
            if cur_num + prev_dp >= cur_num:
                dp[i] = cur_num + prev_dp
            else:
                dp[i] = cur_num
        
        max_sum = dp[0]

        for pos_sum in dp:
            if pos_sum > max_sum:
                max_sum = pos_sum
        
        return max_sum
