# Given two arrays of unique digits nums1 and nums2, return the smallest number that contains at least one digit from each array.

# Example 1:
# Input: nums1 = [4,1,3], nums2 = [5,7]
# Output: 15
# Explanation: The number 15 contains the digit 1 from nums1 and the digit 5 from nums2. It can be proven that 15 is the smallest number we can have.

# Example 2:
# Input: nums1 = [3,5,2,6], nums2 = [3,1,7]
# Output: 3
# Explanation: The number 3 contains the digit 3 which exists in both arrays.

# Constraints:
# 1 <= nums1.length, nums2.length <= 9
# 1 <= nums1[i], nums2[i] <= 9
# All digits in each array are unique.

class Solution:
    def minNumber(self, nums1: [int], nums2: [int]) -> int:
        sorted_1 = sorted(nums1)
        sorted_2 = sorted(nums2)
        if sorted_1[0] < sorted_2[0]:
            string_sum = int(str(sorted_1[0]) + str(sorted_2[0]))
        else:
            string_sum = int(str(sorted_2[0]) + str(sorted_1[0]))
        nums2_set = set(nums2)
        for num in sorted_1:
            if num in nums2_set and num < string_sum:
                return num
        return string_sum

solution = Solution()
print(solution.minNumber(nums1 = [4,1,3], nums2 = [5,7]))
print(solution.minNumber(nums1 = [3,5,2,6], nums2 = [3,1,7]))