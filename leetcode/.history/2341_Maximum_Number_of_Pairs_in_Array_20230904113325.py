# You are given a 0-indexed integer array nums. In one operation, you may do the following:

# Choose two integers in nums that are equal.
# Remove both integers from nums, forming a pair.
# The operation is done on nums as many times as possible.

# Return a 0-indexed integer array answer of size 2 where answer[0] is the number of pairs that are formed
# and answer[1] is the number of leftover integers in nums after doing the operation as many times as possible.


# Example 1:
# Input: nums = [1,3,2,1,3,2,2]
# Output: [3,1]
# Explanation:
# Form a pair with nums[0] and nums[3] and remove them from nums. Now, nums = [3,2,3,2,2].
# Form a pair with nums[0] and nums[2] and remove them from nums. Now, nums = [2,2,2].
# Form a pair with nums[0] and nums[1] and remove them from nums. Now, nums = [2].
# No more pairs can be formed. A total of 3 pairs have been formed, and there is 1 number leftover in nums.

# Example 2:
# Input: nums = [1,1]
# Output: [1,0]
# Explanation: Form a pair with nums[0] and nums[1] and remove them from nums. Now, nums = [].
# No more pairs can be formed. A total of 1 pair has been formed, and there are 0 numbers leftover in nums.

# Example 3:
# Input: nums = [0]
# Output: [0,1]
# Explanation: No pairs can be formed, and there is 1 number leftover in nums.


class Solution:
    def numberOfPairs(self, nums: [int]) -> [int]:
        #         Using dictionary
        pairs = {}

        for num in nums:
            if num not in pairs:
                pairs[num] = 1
            else:
                pairs[num] += 1

        number_of_pairs = 0
        remaining_numbers = 0

        for key, value in pairs.items():
            if value % 2 != 0:
                number_of_pairs += value // 2
                remaining_numbers += value % 2
            else:
                number_of_pairs += value // 2

        output = [number_of_pairs, remaining_numbers]

        return output


#         Using Two Pointer / Sliding Window
#         nums.sort()

#         start=0
#         end=1
#         count=0
#         n=len(nums)

#         while start>=0 and end<=n-1:
#             if nums[start]==nums[end]:

#                 nums.pop(start)
#                 nums.pop(end-1)

#                 count+=1
#                 start=0
#                 end=1

#             else:
#                 start+=1
#                 end+=1

#             n=len(nums)

#         return [count,len(nums)]
