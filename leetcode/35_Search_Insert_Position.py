class Solution:
    def searchInsert(self, nums: [int], target: int) -> int:
        output = len(nums)

        for i, num in enumerate(nums):
            if num >= target:
                output = i
                break

        return output


# Given a sorted array of distinct integers and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.


# Example 1:
# Input: nums = [1,3,5,6], target = 5
# Output: 2

# Example 2:
# Input: nums = [1,3,5,6], target = 2
# Output: 1

# Example 3:
# Input: nums = [1,3,5,6], target = 7
# Output: 4


# alternate binary search method:
# start = 0
# end = len(nums)-1
# while start <= end:
#     mid = (start + end)//2
#     if nums[mid] == target:
#         return mid
#     elif nums[mid] > target:
#         end = mid - 1
#     else:
#         start = mid + 1
# return end+1
