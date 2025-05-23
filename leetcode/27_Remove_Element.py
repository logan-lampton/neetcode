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
    
# Practice
class Solution:
    def removeElement(self, nums: [int], val: int) -> int:
        
        for i in range(len(nums) - 1, - 1, - 1):
            if nums[i] == val:
                nums[i] = ""
        
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == "":
                nums.pop(i)

# Practice
class Solution:
    def removeElement(self, nums: [int], val: int) -> int:

        left = 0

        for right in range(len(nums)):
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1
        
        return left

# Practice
class Solution:
    def removeElement(self, nums: [int], val: int) -> int:

        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        
        return k