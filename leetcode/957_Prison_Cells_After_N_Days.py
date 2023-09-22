# There are 8 prison cells in a row and each cell is either occupied or vacant.

# Each day, whether the cell is occupied or vacant changes according to the following rules:

# If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
# Otherwise, it becomes vacant.
# Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.

# You are given an integer array cells where cells[i] == 1 if the ith cell is occupied and cells[i] == 0 if the ith cell is vacant,
# and you are given an integer n.

# Return the state of the prison after n days (i.e., n such changes described above).

# Example 1:

# Input: cells = [0,1,0,1,1,0,0,1], n = 7
# Output: [0,0,1,1,0,0,0,0]
# Explanation: The following table summarizes the state of the prison on each day:
# Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
# Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
# Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
# Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
# Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
# Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
# Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
# Day 7: [0, 0, 1, 1, 0, 0, 0, 0]

# Example 2:
# Input: cells = [1,0,0,1,0,0,1,0], n = 1000000000
# Output: [0,0,1,1,1,1,1,0]


class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        # create a function to calculate the cells updating for any given day
        def calculate_day(cells):
            cells_for_day = [0] * len(cells)
            for i in range(1, len(cells) - 1):
                if cells[i - 1] == cells[i + 1]:
                    cells_for_day[i] = 1
                else:
                    cells_for_day[i] = 0
            return cells_for_day

        # make a dictionary to hold all the days
        seen = {}

        # loop through the days
        while n > 0:
            # make the cells list into a tuple so that it can be used as a key
            current_cells = tuple(cells)
            # if the current cells are in the seen dictionary, set n to be the remainer of the dictionary at current cells - n
            if current_cells in seen:
                n %= seen[current_cells] - n
            seen[current_cells] = n

            # if n is greater than or equal to 1, subtract 1 and reassign cells to be the result of running the calculate_day function on cells
            if n >= 1:
                n -= 1
                cells = calculate_day(cells)

        return cells

        # time limit exceeded simple code
        # for day in range(n):
        #     cells_for_day = [0] * len(cells)
        # for i in range(1, len(cells) - 1):
        #     if cells[i - 1] == cells[i + 1]:
        #         cells_for_day[i] = 1
        #     else:
        #         cells_for_day[i] = 0
        # cells = cells_for_day
        # return cells
