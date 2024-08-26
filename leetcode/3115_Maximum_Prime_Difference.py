# You are given an integer array nums.

# Return an integer that is the maximum distance between the indices of two (not necessarily different) prime numbers in nums.

# Example 1:
# Input: nums = [4,2,9,5,3]
# Output: 3
# Explanation: nums[1], nums[3], and nums[4] are prime. So the answer is |4 - 1| = 3.

# Example 2:
# Input: nums = [4,8,2,8]
# Output: 0
# Explanation: nums[2] is prime. Because there is just one prime number, the answer is |2 - 2| = 0.

# Constraints:
# 1 <= nums.length <= 3 * 105
# 1 <= nums[i] <= 100
# The input is generated such that the number of prime numbers in the nums is at least one.


class Solution:
    def maximumPrimeDifference(self, nums: [int]) -> int:

        indexes = []

        for i in range(len(nums)):
            if nums[i] == 1:
                continue
            found_divisor = False
            if nums[i] == 2:
                indexes.append(i)
            for num in range(2, nums[i]):
                if nums[i] % num == 0:
                    found_divisor = True
                    continue
            if not found_divisor:
                indexes.append(i)
        
        return indexes[-1] - indexes[0]
    


solution = Solution()
print(solution.maximumPrimeDifference(nums = [4,2,9,5,3]))
print(solution.maximumPrimeDifference(nums = [4,8,2,8]))