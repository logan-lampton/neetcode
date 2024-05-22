# You are given an array of unique integers salary where salary[i] is the salary of the ith employee.

# Return the average salary of employees excluding the minimum and maximum salary. Answers within 10-5 of the actual answer will be accepted.

# Example 1:
# Input: salary = [4000,3000,1000,2000]
# Output: 2500.00000
# Explanation: Minimum salary and maximum salary are 1000 and 4000 respectively.
# Average salary excluding minimum and maximum salary is (2000+3000) / 2 = 2500

# Example 2:
# Input: salary = [1000,2000,3000]
# Output: 2000.00000
# Explanation: Minimum salary and maximum salary are 1000 and 3000 respectively.
# Average salary excluding minimum and maximum salary is (2000) / 1 = 2000

# Constraints:
# 3 <= salary.length <= 100
# 1000 <= salary[i] <= 106
# All the integers of salary are unique.

class Solution:
    def average(self, salary: [int]) -> float:
        salary.sort()
        salaries_to_average = salary[1:-1]
        total = 0
        for salary in salaries_to_average:
            total += salary
        return total / len(salaries_to_average)

solution = Solution()
print(solution.average(salary=[48000,59000,99000,13000,78000,45000,31000,17000,39000,37000,93000,77000,33000,28000,4000,54000,67000,6000,1000,11000]))