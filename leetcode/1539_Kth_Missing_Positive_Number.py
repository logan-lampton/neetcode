# Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

# Return the kth positive integer that is missing from this array.

# Example 1:
# Input: arr = [2,3,4,7,11], k = 5
# Output: 9
# Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.

# Example 2:
# Input: arr = [1,2,3,4], k = 2
# Output: 6
# Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.

# Constraints:
# 1 <= arr.length <= 1000
# 1 <= arr[i] <= 1000
# 1 <= k <= 1000
# arr[i] < arr[j] for 1 <= i < j <= arr.length


class Solution:
    def findKthPositive(self, arr: [int], k: int) -> int:
        missing = []
        missing_num = 1

        for i in range(len(arr)):
            while arr[i] != missing_num:
                missing.append(missing_num)
                if len(missing) == k:
                    break
                missing_num += 1
            missing_num = arr[i] + 1
            if missing_num > arr[-1]:
                while len(missing) < k:
                    missing.append(missing_num)
                    missing_num += 1
        
        return missing[k - 1]
    

solution = Solution()
print(solution.findKthPositive(arr = [2,3,4,7,11], k = 5))
print(solution.findKthPositive(arr = [1,2,3,4], k = 2))