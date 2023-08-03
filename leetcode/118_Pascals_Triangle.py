# Given an integer numRows, return the first numRows of Pascal's triangle.
#
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
#
# Example 1:
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

class Solution(object):
    def generate(self, numRows):
        pascal = [[1]]
        i = 0
        while i < numRows - 1:
            # previous is the last row generated so far
            previous = pascal[-1]
            # start the next row with a list of 1, we will then append to the list
            next_row = [1]
            # for the length of the previous pascal row, add the number in the list to its following number
            for j in range(len(previous) - 1):
                next_row.append(previous[j] + previous[j+1])
            # then append 1 to the end of the next row, as all rows end in the number 1
            next_row.append(1)
            # append the full next_row list to the existing pascal's triangle
            pascal.append(next_row)
            # go to the next row
            i += 1
        return pascal
