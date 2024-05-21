# Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD, return the day number of the year.

# Example 1:
# Input: date = "2019-01-09"
# Output: 9
# Explanation: Given date is the 9th day of the year in 2019.

# Example 2:
# Input: date = "2019-02-10"
# Output: 41

# Constraints:
# date.length == 10
# date[4] == date[7] == '-', and all other date[i]'s are digits
# date represents a calendar date between Jan 1st, 1900 and Dec 31th, 2019.

class Solution:
    def dayOfYear(self, date: str) -> int:

        days_in_month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
        
        day = date[-2] + date[-1]
        month = date[-5] + date[-4]
        year = date[0:4]
        
        day_int = int(day)
        month_int = int(month)
        year_int = int(year)
        
        if year_int % 4 == 0:
            if year_int % 100 == 0:
                if year_int % 400 == 0:
                    days_in_month[2] = 29
            else:
                days_in_month[2] = 29

        month_count = month_int - 1
        days_in_year = 0
        for value in days_in_month.values():
            if month_count:
                days_in_year += value
                month_count -= 1
        
        return days_in_year + day_int


solution = Solution()
print(solution.dayOfYear(date="2019-02-10"))