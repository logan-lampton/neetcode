# You are given an 8 x 8 matrix representing a chessboard. There is exactly one white rook represented by 'R', some number of white bishops 'B', and some number of black pawns 'p'. Empty squares are represented by '.'.

# A rook can move any number of squares horizontally or vertically (up, down, left, right) until it reaches another piece or the edge of the board. A rook is attacking a pawn if it can move to the pawn's square in one move.

# Note: A rook cannot move through other pieces, such as bishops or pawns. This means a rook cannot attack a pawn if there is another piece blocking the path.

# Return the number of pawns the white rook is attacking.

# Example 1:
# Input: board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
# Output: 3
# Explanation:
# In this example, the rook is attacking all the pawns.

# Example 2:
# Input: board = [[".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
# Output: 0
# Explanation:
# The bishops are blocking the rook from attacking any of the pawns.

# Example 3:
# Input: board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]
# Output: 3
# Explanation:
# The rook is attacking the pawns at positions b5, d6, and f5.

# Constraints:
# board.length == 8
# board[i].length == 8
# board[i][j] is either 'R', '.', 'B', or 'p'
# There is exactly one cell with board[i][j] == 'R'


class Solution:
    def numRookCaptures(self, board: [[str]]) -> int:
        rook = None

        # Finding the position of the rook
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'R':
                    rook = (i, j)
                    break
            if rook:
                break

        # Initialize count of captured pawns
        pawns_hit = 0
        
        # Check in all four directions (up, down, left, right)
        
        # Check upwards
        for i in range(rook[0] - 1, -1, -1):
            if board[i][rook[1]] == 'B':  # Bishop blocks the way
                break
            if board[i][rook[1]] == 'p':  # Pawn can be captured
                pawns_hit += 1
                break
        
        # Check downwards
        for i in range(rook[0] + 1, len(board)):
            if board[i][rook[1]] == 'B':
                break
            if board[i][rook[1]] == 'p':
                pawns_hit += 1
                break
        
        # Check left
        for j in range(rook[1] - 1, -1, -1):
            if board[rook[0]][j] == 'B':
                break
            if board[rook[0]][j] == 'p':
                pawns_hit += 1
                break
        
        # Check right
        for j in range(rook[1] + 1, len(board[0])):
            if board[rook[0]][j] == 'B':
                break
            if board[rook[0]][j] == 'p':
                pawns_hit += 1
                break
        
        return pawns_hit


solution = Solution()
print(solution.numRookCaptures(board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]))
print(solution.numRookCaptures(board = [[".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]))
print(solution.numRookCaptures(board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]))