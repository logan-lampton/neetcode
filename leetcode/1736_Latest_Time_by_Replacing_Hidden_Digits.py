# You are given a string time in the form of  hh:mm, where some of the digits in the string are hidden (represented by ?).

# The valid times are those inclusively between 00:00 and 23:59.

# Return the latest valid time you can get from time by replacing the hidden digits.

# Example 1:
# Input: time = "2?:?0"
# Output: "23:50"
# Explanation: The latest hour beginning with the digit '2' is 23 and the latest minute ending with the digit '0' is 50.

# Example 2:
# Input: time = "0?:3?"
# Output: "09:39"
# Example 3:
# Input: time = "1?:22"
# Output: "19:22"

# Constraints:
# time is in the format hh:mm.
# It is guaranteed that you can produce a valid time from the given string.


class Solution:
    def maximumTime(self, time: str) -> str:
        
        if time[0] == '?':
            if time[1] > '3' and time[1] != '?':
                time = '1' + time[1:]
            else:
                time = '2' + time[1:]
        if time[1] == '?':
            if time[0] == '2':
                time = time[0] + '3' + time[2:]
            else:
                time = time[0] + '9' + time[2:]
        if time[3] == '?':
            time = time[0:3] + '5' + time[4:]
        if time[4] == '?':
            time = time[:4] + '9'
        
        return time

solution = Solution()
print(solution.maximumTime(time = "2?:?0"))
print(solution.maximumTime(time = "0?:3?"))
print(solution.maximumTime(time = "1?:22"))