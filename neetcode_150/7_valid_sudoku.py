# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the
# following rules:
#
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:
#
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.
#
#
# Example 1:
#
# Input: board =
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true

class Solution(object):
    def isValidSudoku(self, board):
        # are there repeating numbers (1-9) in:
        # any row
        # any column
        # any 3 x 3 box

        # create hash lists
        hash_row = [set() for _ in range(9)]
        hash_column = [set() for _ in range(9)]
        hash_box = [set() for _ in range(9)]

        # create cells to check
        # can't use row in board, as that would return strings
        for row in range(9):
            for column in range(9):
                cell = board[row][column]
                # make sure the cell is a number between 1 and 9
                if cell != "." and 1 <= int(cell) <= 9:
                    # check if the cell is in any of the hash lists
                    if cell in hash_row[row]:
                        return False
                    elif cell in hash_column[column]:
                        return False
                    # defining what a box is in this check and when adding the cell to the hash_box list below
                    elif cell in hash_box[(row // 3) * 3 + column // 3]:
                        return False
                    # add the cell to the hash lists
                    hash_row[row].add(cell)
                    hash_column[column].add(cell)
                    hash_box[(row // 3) * 3 + column // 3].add(cell)

        return True
