# You are given an integer array nums containing positive integers. We define a function encrypt such that encrypt(x) replaces every digit in x with the largest digit in x. For example, encrypt(523) = 555 and encrypt(213) = 333.

# Return the sum of encrypted elements.

# Example 1:
# Input: nums = [1,2,3]
# Output: 6
# Explanation: The encrypted elements are [1,2,3]. The sum of encrypted elements is 1 + 2 + 3 == 6.

# Example 2:
# Input: nums = [10,21,31]
# Output: 66
# Explanation: The encrypted elements are [11,22,33]. The sum of encrypted elements is 11 + 22 + 33 == 66.

# Constraints:
# 1 <= nums.length <= 50
# 1 <= nums[i] <= 1000


class Solution:
    def sumOfEncryptedInt(self, nums: [int]) -> int:
        answer = 0
        for num in nums:
            if num >= 10:
                string_num = str(num)
                max_num = max(string_num)
                new_num = ""
                for i in range(len(string_num)):
                    new_num += max_num
                answer += int(new_num)
            else:
                answer += num
        return answer


solution = Solution()
print(solution.sumOfEncryptedInt(nums=[10, 21, 31]))
