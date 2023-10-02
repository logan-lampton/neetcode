# An array is monotonic if it is either monotone increasing or monotone decreasing.

# An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

# Given an integer array nums, return true if the given array is monotonic, or false otherwise.

# Example 1:
# Input: nums = [1,2,2,3]
# Output: true

# Example 2:
# Input: nums = [6,5,4,4]
# Output: true

# Example 3:
# Input: nums = [1,3,2]
# Output: false


class Solution:
    def isMonotonic(self, nums: [int]) -> bool:
        # set variable for decreasing and increasing at True
        decreasing = True
        increasing = True

        # Iterate through nums, starting at 1 index comparing it to the 0 index and so on
        for i in range(1, len(nums)):
            # if nums[i] is less than the number before it, set increasing to False
            if nums[i] < nums[i - 1]:
                increasing = False
            # if nums[i] is greater than the number before it, set decreasing to False
            elif nums[i] > nums[i - 1]:
                decreasing = False
            # if the number is not greater than or less than, it can't be monotonic, so break the loop
            if not increasing and not decreasing:
                break

        # by the end of the loop, if the nums were either all decreasing or increasing, return True
        if decreasing or increasing:
            return True
