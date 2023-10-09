# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

# Example 1:
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

# Example 2:
# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation:
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # in order to handle if k is bigger than the length of nums / do the minimum amount of operations
        minimum_k = k % len(nums)

        # set the nums list to =:
        # the original nums list's final k elements as the beginning of the final list
        # the original nums list's elements before -k, as the end of the final list
        nums[:] = nums[-minimum_k:] + nums[:-minimum_k]

        # traditional while k, do for loop, takes too long
        # while k:
        #     last_num = nums[-1]
        #     for i in range(len(nums) - 1, -1, -1):
        #         nums[i] = nums[i - 1]
        #     nums[0] = last_num
        #     k -= 1

        # -----
        # inserting/popping also not a good method time wise, as it is 0N^2
        # for i in range(k):
        #     nums.insert(0, nums.pop())
