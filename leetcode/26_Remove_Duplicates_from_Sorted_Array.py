# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique
# element appears only once. The relative order of the elements should be kept the same.
# Then return the number of unique elements in nums.
#
# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
#
# Change the array nums such that the first k elements of nums contain the unique elements in the order they were
# present in nums initially. The remaining elements of nums are not important as well as the size of nums.

# Return k.
#
# Example 1:
#
# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).


class Solution(object):
    def removeDuplicates(self, nums):
        # too simple:
        # nums.sort()

        # method 1:
        # i = 0
        # while i < len(nums) - 1:
        #     if nums[i] == nums[i + 1]:
        #         nums.pop(i)
        #     else:
        #         i += 1
        # k = len(nums)
        # return k

        # method 2:
        if not nums:
            return 0

        k = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1

        return k


# Practice:
class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] == nums[i - 1]:
                nums.pop(i)


# Practice
class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        
        insert_index = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[insert_index] = nums[i]
                insert_index += 1
        
        return insert_index

# Practice
class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        if len(nums) == 1:
            return 1
        k = 1
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1
        
        return k