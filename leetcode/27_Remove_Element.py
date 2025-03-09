class Solution:
    def removeElement(self, nums: [int], val: int) -> int:
        i = 0

        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1


# Practice
class Solution:
    def removeElement(self, nums: [int], val: int) -> int:
        
        front_index = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[front_index] = nums[i]
                front_index += 1
        
        return front_index