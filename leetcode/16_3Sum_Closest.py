# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

# Return the sum of the three integers.

# You may assume that each input would have exactly one solution.

# Example 1:
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

# Example 2:
# Input: nums = [0,0,0], target = 1
# Output: 0
# Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).

# Constraints:
# 3 <= nums.length <= 500
# -1000 <= nums[i] <= 1000
# -104 <= target <= 104


class Solution:
    def threeSumClosest(self, nums: [int], target: int) -> int:
        nums.sort()
        closest_value = float('inf')
        min_diff = float('inf')

        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                cur_sum = nums[i] + nums[left] + nums[right]
                if cur_sum == target:
                    return cur_sum
                if cur_sum < target:
                    left += 1
                else:
                    right -= 1
                cur_diff = abs(cur_sum - target)
                if cur_diff < min_diff:
                    min_diff = cur_diff
                    closest_value = cur_sum
        
        return closest_value
                

solution = Solution()
print(solution.threeSumClosest(nums = [-1,2,1,-4], target = 1))
print(solution.threeSumClosest(nums = [0,0,0], target = 1))