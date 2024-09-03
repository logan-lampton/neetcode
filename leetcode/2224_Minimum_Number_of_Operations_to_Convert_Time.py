# You are given two strings current and correct representing two 24-hour times.

# 24-hour times are formatted as "HH:MM", where HH is between 00 and 23, and MM is between 00 and 59. The earliest 24-hour time is 00:00, and the latest is 23:59.

# In one operation you can increase the time current by 1, 5, 15, or 60 minutes. You can perform this operation any number of times.

# Return the minimum number of operations needed to convert current to correct.

# Example 1:
# Input: current = "02:30", correct = "04:35"
# Output: 3
# Explanation:
# We can convert current to correct in 3 operations as follows:
# - Add 60 minutes to current. current becomes "03:30".
# - Add 60 minutes to current. current becomes "04:30".
# - Add 5 minutes to current. current becomes "04:35".
# It can be proven that it is not possible to convert current to correct in fewer than 3 operations.

# Example 2:
# Input: current = "11:00", correct = "11:01"
# Output: 1
# Explanation: We only have to add one minute to current, so the minimum number of operations needed is 1.

# Constraints:
# current and correct are in the format "HH:MM"
# current <= correct


class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        
        # convert from strings to time in minutes
        def to_minutes(time):
            int_time = 0
            if time[0] == 0:
                int_time = int(time[1]) * 60 + int(time[3:5])
            else:
                int_time = int_time = int(time[0:2]) * 60 + int(time[3:5])
            return int_time

        int_current = to_minutes(current)
        int_correct = to_minutes(correct)
        
        # establish the difference between the times
        to_change = abs(int_current - int_correct)
        
        # continue to run operations until the times are the same/count the number of operations
        changes = 0
        while to_change:
            if to_change >= 60:
                changes += 1
                to_change -= 60
            elif to_change >= 15:
                changes += 1
                to_change -= 15
            elif to_change >= 5:
                changes += 1
                to_change -= 5
            else:
                changes += 1
                to_change -= 1
        
        return changes
    

solution = Solution()
print(solution.convertTime(current = "02:30", correct = "04:35"))
print(solution.convertTime(current = "11:00", correct = "11:01"))