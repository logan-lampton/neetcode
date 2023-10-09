# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

# Example 2:
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]

# Example 3:
# Input: nums = [], target = 0
# Output: [-1,-1]


class Solution:
    def searchRange(self, nums: [int], target: int) -> [int]:
        high = 0
        number_of_target = 0
        for i in range(len(nums)):
            if nums[i] == target:
                high = i
                number_of_target += 1

        if number_of_target:
            answer = [high - (number_of_target - 1), high]
        else:
            answer = [-1, -1]

        return answer

        # an answer below, but wanted a better runtime / still with O(log n) runtime complexity.
        # answer = []

        # if target in nums:
        #     for i in range(len(nums)):
        #         if nums[i] == target:
        #             answer.append(i)
        # else:
        #     answer = [-1, -1]

        # answer = [answer[0], answer[-1]]

        # return answer
