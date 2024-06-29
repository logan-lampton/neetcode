# Given a 0-indexed integer array nums of size n, find the maximum difference between nums[i] and nums[j] (i.e., nums[j] - nums[i]), such that 0 <= i < j < n and nums[i] < nums[j].

# Return the maximum difference. If no such i and j exists, return -1.

# Example 1:
# Input: nums = [7,1,5,4]
# Output: 4
# Explanation:
# The maximum difference occurs with i = 1 and j = 2, nums[j] - nums[i] = 5 - 1 = 4.
# Note that with i = 1 and j = 0, the difference nums[j] - nums[i] = 7 - 1 = 6, but i > j, so it is not valid.

# Example 2:
# Input: nums = [9,4,3,2]
# Output: -1
# Explanation:
# There is no i and j such that i < j and nums[i] < nums[j].

# Example 3:
# Input: nums = [1,5,2,10]
# Output: 9
# Explanation:
# The maximum difference occurs with i = 0 and j = 3, nums[j] - nums[i] = 10 - 1 = 9.

# Constraints:
# n == nums.length
# 2 <= n <= 1000
# 1 <= nums[i] <= 109

class Solution:
    def maximumDifference(self, nums: [int]) -> int:
        left = 0
        right = 1
        max_dif = -1
        while right < len(nums):
            if nums[left] < nums[right]:
                cur_dif = nums[right] - nums[left]
                if max_dif < cur_dif:
                    max_dif = cur_dif
                right += 1
            else:
                if left + 1 == right:
                    left += 1
                    right += 1
                else:
                    left += 1
        return max_dif

solution = Solution()
print(solution.maximumDifference(nums = [7,1,5,4]))
print(solution.maximumDifference(nums = [9,4,3,2]))
print(solution.maximumDifference(nums = [1,5,2,10]))