# Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

# Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited. Return false otherwise.

# Example 1:
# Input: path = "NES"
# Output: false
# Explanation: Notice that the path doesn't cross any point more than once.

# Example 2:
# Input: path = "NESWW"
# Output: true
# Explanation: Notice that the path visits the origin twice.

# Constraints:
# 1 <= path.length <= 104
# path[i] is either 'N', 'S', 'E', or 'W'.


def isPathCrossing(path: str) -> bool:
    visited = {(0, 0): 1}
    current = (0, 0)

    for i in range(len(path)):
        if path[i] == "N":
            current = tuple(map(lambda i, j: i + j, current, (1, 0)))
        elif path[i] == "E":
            current = tuple(map(lambda i, j: i + j, current, (0, 1)))
        elif path[i] == "S":
            current = tuple(map(lambda i, j: i - j, current, (1, 0)))
        elif path[i] == "W":
            current = tuple(map(lambda i, j: i - j, current, (0, 1)))
        if current in visited:
            return True
        else:
            visited[current] = 1

    return False
