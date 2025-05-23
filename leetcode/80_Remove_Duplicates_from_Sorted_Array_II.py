# Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice.
# The relative order of the elements should be kept the same.

# Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array
# nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not
# matter what you leave beyond the first k elements.

# Return k after placing the final result in the first k slots of nums.

# Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

# Custom Judge:

# The judge will test your solution with the following code:

# int[] nums = [...]; // Input array
# int[] expectedNums = [...]; // The expected answer with correct length

# int k = removeDuplicates(nums); // Calls your implementation

# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
#     assert nums[i] == expectedNums[i];
# }
# If all assertions pass, then your solution will be accepted.


# Example 1:

# Input: nums = [1,1,1,2,2,3]
# Output: 5, nums = [1,1,2,2,3,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
# Example 2:

# Input: nums = [0,0,1,1,1,1,2,3,3]
# Output: 7, nums = [0,0,1,1,2,3,3,_,_]
# Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).


class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        num_dict = {}

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] not in num_dict:
                num_dict[nums[i]] = 1
            else:
                num_dict[nums[i]] += 1
            if num_dict[nums[i]] > 2:
                nums.remove(nums[i])

# Another way to solve:
    # def removeDuplicates(self, nums: [int]) -> int:
    #     i = len(nums) - 2
    #     j = len(nums) - 1
    #     number_element = 1
        
    #     while i >= 0:
    #         if nums[i] == nums[j]:
    #             if number_element == 1:
    #                 number_element = 2
    #             else:
    #                 nums.pop(i)
    #                 j -= 1
    #         else:
    #             number_element = 1
    #             j = i
    #         i -= 1


# Practice
class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        counter = 1
        insert_index = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                counter += 1
            else:
                counter = 1
            
            if counter <= 2:
                nums[insert_index] = nums[i]
                insert_index += 1
        
        return insert_index