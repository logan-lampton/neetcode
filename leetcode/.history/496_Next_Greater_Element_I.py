# The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

# You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

# For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next
# greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

# Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

# Example 1:
# Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
# Output: [-1,3,-1]
# Explanation: The next greater element for each value of nums1 is as follows:
# - 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
# - 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
# - 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.

# Example 2:
# Input: nums1 = [2,4], nums2 = [1,2,3,4]
# Output: [3,-1]
# Explanation: The next greater element for each value of nums1 is as follows:
# - 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
# - 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.


class Solution:
    def nextGreaterElement(self, nums1: [int], nums2: [int]) -> [int]:
        # create a dictionary and a stack
        dictionary = {}
        stack = []

        # make the first number in the stack be the 0 index of nums2
        stack.append(nums2[0])

        # for the index in range nums2[1] through the length of nums2
        for i in range(1, len(nums2)):
            # while there is a stack and the value at nums2[index] is greater than the value of the last element on the stack (so the top of the stack / first to pop off)
            while stack and nums2[i] > stack[-1]:
                # if the element is greater than the top of the stack, add it to the top of the stack (by making the last element in the stack equal to nums2 at that index)
                dictionary[stack[-1]] = nums2[i]
                # remove from the stack
                stack.pop()
            # add the next number from nums2 to the stack
            stack.append(nums2[i])

        # for the remaining elements in the stack
        for element in stack:
            # set the value in the dictionary for that element to -1
            dictionary[element] = -1

        # create result array
        result = []
        # loop through all the indexes in nums1 and add the values associated with them in the dictionary to the result array
        for i in range(len(nums1)):
            result.append(dictionary[nums1[i]])

        return result
