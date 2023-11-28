# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Example 2:
# Input: nums = [0]
# Output: [0]

# Constraints:
# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1


def moveZeroes(nums) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    zero_count = 0
    n = len(nums)

    for i in range(n):
        if nums[i] != 0:
            nums[zero_count] = nums[i]
            zero_count += 1

    while zero_count < n:
        nums[zero_count] = 0
        zero_count += 1

    return nums
