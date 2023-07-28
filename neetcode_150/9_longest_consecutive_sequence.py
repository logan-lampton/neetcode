class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        # sort the nums list and keep the same list (as opposed to sorted(nums))
        nums.sort()
        current_length = 1
        max_length = 1

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                continue
            if nums[i] + 1 == nums[i + 1]:
                current_length += 1
            if nums[i] + 1 != nums[i + 1] and nums[i] != nums[i+ 1]:
                current_length = 1
            if max_length < current_length:
                max_length = current_length
        return max_length
