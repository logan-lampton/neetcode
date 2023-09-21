# Given the coordinates of four points in 2D space p1, p2, p3 and p4, return true if the four points construct a square.

# The coordinate of a point pi is represented as [xi, yi]. The input is not given in any order.

# A valid square has four equal sides with positive length and four equal angles (90-degree angles).

# Example 1:
# Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
# Output: true

# Example 2:
# Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,12]
# Output: false

# Example 3:
# Input: p1 = [1,0], p2 = [-1,0], p3 = [0,1], p4 = [0,-1]
# Output: true


class Solution:
    def validSquare(self, p1: [int], p2: [int], p3: [int], p4: [int]) -> bool:
        # make a list of the lists
        points = [p1, p2, p3, p4]

        # make sure the points aren't all the same
        if points == [[0, 0], [0, 0], [0, 0], [0, 0]]:
            return False

        # make a list to track distances between the points
        distances = []

        # loop through the points to grab the distance between each x and y point
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                distance_x = points[i][0] - points[j][0]
                distance_y = points[i][1] - points[j][1]
                # square the x and y distances and add them together
                squared_distance = distance_x * distance_x + distance_y * distance_y
                # add the distances to the distances list
                distances.append(squared_distance)

        # sort the distances
        distances.sort()

        # make sure the resulting shape is a square
        # make sure all 4 sides are the same
        # make sure that the two diagonals of the square have equal lengths
        # finally, make sure that a side * 2 is equal to the diagonal
        if (
            distances[0] == distances[1] == distances[2] == distances[3]
            and distances[4] == distances[5]
            and distances[0] * 2 == distances[4]
        ):
            return True
        return False
