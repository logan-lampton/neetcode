# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the
# array such that nums[i] == nums[j] and abs(i - j) <= k.

# Example 1:
# Input: nums = [1,2,3,1], k = 3
# Output: true

# Example 2:
# Input: nums = [1,0,1,1], k = 1
# Output: true

# Example 3:
# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false


class Solution:
    def containsNearbyDuplicate(self, nums: [int], k: int) -> bool:
        # create an dictionary to track the latest occurrence of each number
        number_and_index = {}

        # select both the index and number of each number in nums
        for i, num in enumerate(nums):
            # check if the number has been encountered in the array
            if num in number_and_index:
                # check if the absolute value of i - the last index of the number are less than or equal to k
                if abs(i - number_and_index[num] <= k):
                    return True
            # update the index in the dictionary to the latest occurrence of the number
            number_and_index[num] = i
        # after the for loop, if the answer hasn't returned True, return False
        return False
