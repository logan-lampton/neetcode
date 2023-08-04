# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
#
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
#
#
#
#
# Example 1:
#
# Input: rowIndex = 3
# Output: [1,3,3,1]
# Example 2:
#
# Input: rowIndex = 0
# Output: [1]

class Solution(object):
    def getRow(self, rowIndex):
        row = [1]
        i = 0
        while i < rowIndex:
            next_row = [1]
            for j in range(len(row) - 1):
                next_num = row[j] + row[j + 1]
                next_row.append(next_num)
            next_row.append(1)
            row = next_row
            i += 1
        return row
