# Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum integer common to both arrays. If there is no common integer amongst nums1 and nums2, return -1.

# Note that an integer is said to be common to nums1 and nums2 if both arrays have at least one occurrence of that integer.

# Example 1:
# Input: nums1 = [1,2,3], nums2 = [2,4]
# Output: 2
# Explanation: The smallest element common to both arrays is 2, so we return 2.

# Example 2:
# Input: nums1 = [1,2,3,6], nums2 = [2,3,4,5]
# Output: 2
# Explanation: There are two common elements in the array 2 and 3 out of which 2 is the smallest, so 2 is returned.

# Constraints:
# 1 <= nums1.length, nums2.length <= 105
# 1 <= nums1[i], nums2[j] <= 109
# Both nums1 and nums2 are sorted in non-decreasing order.

class Solution:
    def getCommon(self, nums1: [int], nums2: [int]) -> int:
        dictionary1 = {}
        dictionary2 = {}
        for i in range(len(nums1)):
            if nums1[i] not in dictionary1:
                dictionary1[nums1[i]] = i
        for j in range(len(nums2)):
            if nums2[j] in dictionary1:
                return nums2[j] 
        return -1

solution = Solution()
print(solution.getCommon(nums1 = [1,2,3], nums2 = [2,4]))
print(solution.getCommon(nums1 = [1,2,3,6], nums2 = [2,3,4,5]))