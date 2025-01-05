# Write a program to count the number of days between two dates.

# The two dates are given as strings, their format is YYYY-MM-DD as shown in the examples.

# Example 1:
# Input: date1 = "2019-06-29", date2 = "2019-06-30"
# Output: 1

# Example 2:
# Input: date1 = "2020-01-15", date2 = "2019-12-31"
# Output: 15

# Constraints:
# The given dates are valid dates between the years 1971 and 2100.


class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        def isLeapYear(year):
            return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

        # Convert string dates into year, month, and day
        year1, month1, day1 = map(int, date1.split("-"))
        year2, month2, day2 = map(int, date2.split("-"))

        # Function to count the total number of days from year 0 to a given date
        def daysFromStart(year, month, day):
            months_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            total_days = 0

            # Add days for complete years before the given year
            for y in range(year):
                total_days += 366 if isLeapYear(y) else 365

            # Add days for complete months in the current year
            for m in range(month - 1):
                total_days += months_days[m]
                if m == 1 and isLeapYear(year):  # Add 1 day for February in a leap year
                    total_days += 1

            # Add days for the current month
            total_days += day

            return total_days

        # Get the total days for both dates
        days1 = daysFromStart(year1, month1, day1)
        days2 = daysFromStart(year2, month2, day2)

        # The difference in days
        return abs(days1 - days2)
    

solution = Solution()
print(solution.daysBetweenDates(date1 = "2019-06-29", date2 = "2019-06-30"))
print(solution.daysBetweenDates(date1 = "2020-01-15", date2 = "2019-12-31"))