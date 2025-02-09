# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]

# Example 2:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.

# Constraints:
# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000

from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        def create_hash(array):
            hashtable = {}
            for num in array:
                if num not in hashtable:
                    hashtable[num] = 1
                else:
                    hashtable[num] += 1
            return hashtable
        
        nums1_hash = create_hash(nums1)
        nums2_hash = create_hash(nums2)

        answer = []
        for key, value in nums1_hash.items():
            if key in nums2_hash:
                if value <= nums2_hash[key]:
                    answer.append((key, value))
                else:
                    answer.append((key, nums2_hash[key]))
        
        final_answer = []

        for element in answer:
            key, value = element
            for i in range(value):
                final_answer.append(key)

        return final_answer
    
solution = Solution()
print(solution.intersect(nums1 = [1,2,2,1], nums2 = [2,2]))
print(solution.intersect(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))