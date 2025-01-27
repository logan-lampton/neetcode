# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Example 2:
# Input: nums = [1], k = 1
# Output: [1]

# Constraints:
# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.

import heapq

class Solution:
    def topKFrequent(self, nums: [int], k: int) -> [int]:
        num_frequency = {}
        
        for num in nums:
            if num not in num_frequency:
                num_frequency[num] = 1
            else:
                num_frequency[num] += 1
        
        heap = []

        for num, count in num_frequency.items():
            if len(heap) < k:
                heapq.heappush(heap, (count, num))
            elif count > heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap, (count, num))
        
        answer = []
        for count, num in heap:
            answer.append(num)
        return answer


solution = Solution()
print(solution.topKFrequent(nums = [1,1,1,2,2,3], k = 2))
print(solution.topKFrequent(nums = [1], k = 1))