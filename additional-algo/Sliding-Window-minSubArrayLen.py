# Sliding Window - minSubArrayLen
# Write a function called minSubArrayLen which accepts two parameters - an array of positive integers and a positive
# integer.
#
# This function should return the minimal length of a contiguous subarray of which the sum is greater than or equal to
# the integer passed to the function. If there isn't one, return 0 instead.

# Examples:
#
# minSubArrayLen([2,3,1,2,4,3], 7) // 2 -> because [4,3] is the smallest subarray
# minSubArrayLen([2,1,6,5,4], 9) // 2 -> because [5,4] is the smallest subarray
# minSubArrayLen([3,1,7,11,2,9,8,21,62,33,19], 52) // 1 -> because [62] is greater than 52
# minSubArrayLen([1,4,16,22,5,7,8,9,10],39) // 3
# minSubArrayLen([1,4,16,22,5,7,8,9,10],55) // 5
# minSubArrayLen([4, 3, 3, 8, 1, 2, 3], 11) // 2
# minSubArrayLen([1,4,16,22,5,7,8,9,10],95) // 0

class Solution(object):
    def minSubArrayLen(self, target, nums):
        if not nums:
            return 0

        min_length = len(nums) + 1  # Initialize min_length to a value greater than the array length
        left = 0
        current_sum = 0

        for right in range(len(nums)):
            current_sum += nums[right]

            while current_sum >= target:
                min_length = min(min_length, right - left + 1)
                current_sum -= nums[left]
                left += 1

        if min_length > len(nums):  # Check if no subarray found
            return 0

        return min_length
