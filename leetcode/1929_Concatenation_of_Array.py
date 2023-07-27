class Solution(object):
    def getConcatenation(self, nums):
        # add nums to the end of nums
        nums.extend(nums)
        return nums
