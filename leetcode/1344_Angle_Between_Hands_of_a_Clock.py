# Given two numbers, hour and minutes, return the smaller angle (in degrees) formed between the hour and the minute hand.

# Answers within 10-5 of the actual value will be accepted as correct.

# Example 1:
# Input: hour = 12, minutes = 30
# Output: 165

# Example 2:
# Input: hour = 3, minutes = 30
# Output: 75

# Example 3:
# Input: hour = 3, minutes = 15
# Output: 7.5

# Constraints:
# 1 <= hour <= 12
# 0 <= minutes <= 59

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        angle_dict = {12 : 0, 1 : 5, 2 : 10, 3 : 15, 4 : 20, 5 : 25, 6 : 30, 7 : 35, 8 : 40, 9 : 45, 10 : 50, 11 : 55 }
        
        percent_of_sixty = minutes / 60

        additional_hour_angle = 5 * percent_of_sixty

        hour_angle = angle_dict[hour] + additional_hour_angle

        difference = abs(hour_angle - minutes) * 6
        if difference > (360 / 2):
            return 360 - difference
        return difference
    

solution = Solution()
print(solution.angleClock(hour = 12, minutes = 30))
print(solution.angleClock(hour = 3, minutes = 30))
print(solution.angleClock(hour = 3, minutes = 15))
print(solution.angleClock(hour = 1, minutes = 57))