# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
# representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
# To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should
# be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.


# Example 1:
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

# Example 2:
# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
# Explanation: The arrays we are merging are [1] and [].
# The result of the merge is [1].

# Example 3:
# Input: nums1 = [0], m = 0, nums2 = [1], n = 1
# Output: [1]
# Explanation: The arrays we are merging are [] and [1].
# The result of the merge is [1].
# Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result
# can fit in nums1.


class Solution:
    def merge(self, nums1: [int], m: int, nums2: [int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # make a pointer for moving from the back of the elements added together
        p = m + n - 1
        # make pointers for tracking the index of each list we are combining
        p1 = m - 1
        p2 = n - 1

        # while there are elements in both arrays...
        while p1 >= 0 and p2 >= 0:
            # compare and add the larger element to nums1
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # if nums2 still has elements, add them to nums1
        nums1[: p2 + 1] = nums2[: p2 + 1]

# another method
    # def merge(self, nums1: [int], m: int, nums2: [int], n: int) -> None:
    #     """
    #     Do not return anything, modify nums1 in-place instead.
    #     """
    #     nums1_pointer, nums2_pointer = 0, 0
    #     merged_list = []
    #     while nums1_pointer < m and nums2_pointer < n:
    #         if nums1[nums1_pointer] < nums2[nums2_pointer]:
    #             merged_list.append(nums1[nums1_pointer])
    #             nums1_pointer += 1
    #         else:
    #             merged_list.append(nums2[nums2_pointer])
    #             nums2_pointer += 1
        
    #     while nums1_pointer < m:
    #         merged_list.append(nums1[nums1_pointer])
    #         nums1_pointer += 1
        
    #     while nums2_pointer < n:
    #         merged_list.append(nums2[nums2_pointer])
    #         nums2_pointer += 1

    #     for i in range(len(nums1)):
    #         nums1[i] = merged_list[i]

# Practice
class Solution:
    def merge(self, nums1: [int], m: int, nums2: [int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        nums1_i = m - 1
        nums2_i = n - 1
        combined_i = m + n - 1

        while nums1_i >= 0 and nums2_i >= 0:
            if nums1[nums1_i] > nums2[nums2_i]:
                nums1[combined_i] = nums1[nums1_i]
                nums1_i -= 1
            else:
                nums1[combined_i] = nums2[nums2_i]
                nums2_i -= 1
            combined_i -= 1
        
        while nums2_i >= 0:
            nums1[combined_i] = nums2[nums2_i]
            nums2_i -= 1
            combined_i -= 1

# Practice
class Solution:
    def merge(self, nums1: [int], m: int, nums2: [int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        nums1_index = m - 1
        nums2_index = n - 1

        combined_index = m + n - 1

        while nums1_index >= 0 and nums2_index >= 0:
            if nums1[nums1_index] > nums2[nums2_index]:
                nums1[combined_index] = nums1[nums1_index]
                nums1_index -= 1
            else:
                nums1[combined_index] = nums2[nums2_index]
                nums2_index -= 1
            combined_index -= 1
        
        while nums2_index >= 0:
            nums1[combined_index] = nums2[nums2_index]
            nums2_index -= 1
            combined_index -= 1

# Practice
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_index = m - 1
        nums2_index = n - 1

        combined_index = m + n - 1

        while nums1_index >= 0 and nums2_index >= 0:
            if nums1[nums1_index] > nums2[nums2_index]:
                nums1[combined_index] = nums1[nums1_index]
                nums1_index -= 1
            else:
                nums1[combined_index] = nums2[nums2_index]
                nums2_index -= 1
            combined_index -= 1
            
        while nums2_index >= 0:
            nums1[combined_index] = nums2[nums2_index]
            nums2_index -= 1
            combined_index -= 1