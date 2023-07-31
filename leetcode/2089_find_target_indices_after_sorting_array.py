# You are given a 0-indexed integer array nums and a target element target.
#
# A target index is an index i such that nums[i] == target.
#
# Return a list of the target indices of nums after sorting nums in non-decreasing order. If there are no target
# indices, return an empty list. The returned list must be sorted in increasing order.

class Solution(object):
    def targetIndices(self, nums, target):
        sorted_nums = sorted(nums)
        output = []
        for i in range(len(sorted_nums)):
            if sorted_nums[i] == target:
                output.append(i)
        return output
