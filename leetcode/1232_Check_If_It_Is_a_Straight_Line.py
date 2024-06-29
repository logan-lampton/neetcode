# You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

# Example 1:
# Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
# Output: true

# Example 2:
# Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
# Output: false

# Constraints:
# 2 <= coordinates.length <= 1000
# coordinates[i].length == 2
# -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
# coordinates contains no duplicate point.

class Solution:
    def checkStraightLine(self, coordinates: [[int]]) -> bool:
        if len(coordinates) < 2:
            return True
        
        # Calculate the slope using the first two points
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]
        
        # Calculate the differences
        dx = x1 - x0
        dy = y1 - y0
        
        for i in range(2, len(coordinates)):
            x, y = coordinates[i]
            # Check if the cross product is zero, which means the points are collinear
            if dx * (y - y0) != dy * (x - x0):
                return False
        
        return True
    
solution = Solution()
print(solution.checkStraightLine(coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]))
print(solution.checkStraightLine(coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]))