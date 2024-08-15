# Given a date string in the form Day Month Year, where:

# Day is in the set {"1st", "2nd", "3rd", "4th", ..., "30th", "31st"}.
# Month is in the set {"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"}.
# Year is in the range [1900, 2100].
# Convert the date string to the format YYYY-MM-DD, where:

# YYYY denotes the 4 digit year.
# MM denotes the 2 digit month.
# DD denotes the 2 digit day.

# Example 1:
# Input: date = "20th Oct 2052"
# Output: "2052-10-20"

# Example 2:
# Input: date = "6th Jun 1933"
# Output: "1933-06-06"

# Example 3:
# Input: date = "26th May 1960"
# Output: "1960-05-26"

# Constraints:
# The given dates are guaranteed to be valid, so no error handling is necessary.


class Solution:
    def reformatDate(self, date: str) -> str:
        split_date = date.split()
        month_dict = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6, "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12}
        year = split_date[2]
        month = month_dict[split_date[1]]
        day = split_date[0][:-2]
        if month < 10:
            month = f"0{month}"
        if len(day) == 1:
            day = f"0{day}"
        answer = f"{year}-{month}-{day}"
        return answer


solution = Solution()
print(solution.reformatDate(date = "20th Oct 2052"))
print(solution.reformatDate(date = "6th Jun 1933"))
print(solution.reformatDate(date = "26th May 1960"))