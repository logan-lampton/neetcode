# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k
# closest points to the origin (0, 0).

# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

# Example 1:
# Input: points = [[1,3],[-2,2]], k = 1
# Output: [[-2,2]]
# Explanation:
# The distance between (1, 3) and the origin is sqrt(10).
# The distance between (-2, 2) and the origin is sqrt(8).
# Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
# We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].

# Example 2:
# Input: points = [[3,3],[5,-1],[-2,4]], k = 2
# Output: [[3,3],[-2,4]]
# Explanation: The answer [[-2,4],[3,3]] would also be accepted.

import math

# class Solution(object):
#     def kClosest(self, points, k):

#         closest_points = []

#         for point in points:
#             distance = math.sqrt((0 - point[0]) ** 2 + (0 - point[1]) ** 2)
#             if len(closest_points) < k:
#                 closest_points.append((distance, point))
#                 closest_points.sort()  # Sort the list
#             else:
#                 if distance < closest_points[-1][0]:
#                     closest_points.pop()
#                     closest_points.append((distance, point))
#                     closest_points.sort()  # Sort the list

#         return [point for _, point in closest_points]


# New Solution I came up with
class Solution:
    def kClosest(self, points: [[int]], k: int) -> [[int]]:

        points_distances = []

        for i in range(len(points)):
            first_cord = (0 - points[i][0]) ** 2
            second_cord = (0 - points[i][1]) ** 2
            distance = math.sqrt(first_cord + second_cord)
            points_distances.append((distance, points[i]))

        points_distances.sort()

        answer = []
        for i in range(k):
            answer.append(points_distances[i][1])
