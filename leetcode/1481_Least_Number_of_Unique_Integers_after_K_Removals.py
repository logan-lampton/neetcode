# Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.

# Example 1:
# Input: arr = [5,5,4], k = 1
# Output: 1
# Explanation: Remove the single 4, only 5 is left.

# Example 2:
# Input: arr = [4,3,1,1,3,3,2], k = 3
# Output: 2
# Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.

# Constraints:
# 1 <= arr.length <= 10^5
# 1 <= arr[i] <= 10^9
# 0 <= k <= arr.length


class Solution:
    def findLeastNumOfUniqueInts(self, arr: [int], k: int) -> int:
        dictionary = {}
        for num in arr:
            if num not in dictionary:
                dictionary[num] = 1
            else:
                dictionary[num] += 1
        
        dict_len = len(dictionary)
        remaining_k = k
        sorted_dict = sorted(dictionary.items(), key=lambda item: item[1])
        
        for i in range(len(sorted_dict)):
            if remaining_k >= sorted_dict[i][1]:
                dict_len -= 1
                remaining_k -= sorted_dict[i][1]
            else:
                break
        
        return dict_len


solution = Solution()
print(solution.findLeastNumOfUniqueInts(arr = [5,5,4], k = 1))
print(solution.findLeastNumOfUniqueInts(arr = [4,3,1,1,3,3,2], k = 3))