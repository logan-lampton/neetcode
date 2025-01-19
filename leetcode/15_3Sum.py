# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that 
# i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.

# Example 2:
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.

# Example 3:
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.

# Constraints:
# 3 <= nums.length <= 3000
# -105 <= nums[i] <= 105

# class Solution:
#     def threeSum(self, nums: [int]) -> [[int]]:
        
#         nums.sort()

#         triplets = set()

#         # need three integers to form a triplet
#         for i in range(len(nums) - 2):
#             if i > 0 and nums[i] == nums[i - 1]:
#                 continue
#             firstNum = nums[i]
#             j = i + 1
#             k = len(nums) - 1
#             while j < k:
#                 secondNum = nums[j]
#                 thirdNum = nums[k]

#                 potentialSum = firstNum + secondNum + thirdNum

#                 if potentialSum > 0:
#                     k -= 1
#                 elif potentialSum < 0:
#                     j += 1
#                 else:
#                     triplets.add((firstNum, secondNum, thirdNum))
#                     j += 1
#                     k -= 1

#         return triplets
    

# Review / different solution:
class Solution:
  def threeSum(self, nums: [int]) -> [[int]]:
      answer = []
      nums.sort()

      for i in range(len(nums)):
          if i > 0 and nums[i] == nums[i - 1]:
              continue
          
          middle = i + 1
          right = len(nums) - 1

          while middle < right:
              cur_total = nums[i] + nums[middle] + nums[right]

              if cur_total == 0:
                  answer.append([nums[i], nums[middle], nums[right]])
                  middle += 1
                  while nums[middle] == nums[middle - 1] and middle < right:
                      middle += 1
              elif cur_total < 0:
                  middle += 1
              else:
                  right -= 1
          
      return answer


solution = Solution()
print(solution.threeSum(nums = [-1,0,1,2,-1,-4]))
print(solution.threeSum(nums = [0,1,1]))
print(solution.threeSum(nums = [0,0,0]))