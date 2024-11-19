# You are given two 0-indexed integer arrays player1 and player2, representing the number of pins that player 1 and player 2 hit in a bowling game, respectively.

# The bowling game consists of n turns, and the number of pins in each turn is exactly 10.

# Assume a player hits xi pins in the ith turn. The value of the ith turn for the player is:
# 2xi if the player hits 10 pins in either (i - 1)th or (i - 2)th turn.
# Otherwise, it is xi.
# The score of the player is the sum of the values of their n turns.

# Return
# 1 if the score of player 1 is more than the score of player 2,
# 2 if the score of player 2 is more than the score of player 1, and
# 0 in case of a draw.

# Example 1:
# Input: player1 = [5,10,3,2], player2 = [6,5,7,3]
# Output: 1
# Explanation:
# The score of player 1 is 5 + 10 + 2*3 + 2*2 = 25.
# The score of player 2 is 6 + 5 + 7 + 3 = 21.

# Example 2:
# Input: player1 = [3,5,7,6], player2 = [8,10,10,2]
# Output: 2
# Explanation:
# The score of player 1 is 3 + 5 + 7 + 6 = 21.
# The score of player 2 is 8 + 10 + 2*10 + 2*2 = 42.

# Example 3:
# Input: player1 = [2,3], player2 = [4,1]
# Output: 0
# Explanation:
# The score of player1 is 2 + 3 = 5.
# The score of player2 is 4 + 1 = 5.

# Example 4:
# Input: player1 = [1,1,1,10,10,10,10], player2 = [10,10,10,10,1,1,1]
# Output: 2
# Explanation:
# The score of player1 is 1 + 1 + 1 + 10 + 2*10 + 2*10 + 2*10 = 73.
# The score of player2 is 10 + 2*10 + 2*10 + 2*10 + 2*1 + 2*1 + 1 = 75.

# Constraints:
# n == player1.length == player2.length
# 1 <= n <= 1000
# 0 <= player1[i], player2[i] <= 10


class Solution:
    def isWinner(self, player1: [int], player2: [int]) -> int:
        array_len = len(player1)

        def calculate_score(player_array):
            player_score = 0
            previous_10 = -1
            for i in range(array_len):
                cur_score = 0
                if previous_10 >= 0 and i <= (previous_10 + 2):
                    cur_score = (2 * player_array[i])
                else:
                    cur_score = player_array[i]
                player_score += cur_score
                if player_array[i] == 10:
                    previous_10 = i
            return player_score
        
        player1_score = calculate_score(player1)
        player2_score = calculate_score(player2)
        
        if player1_score > player2_score:
            return 1
        elif player1_score < player2_score:
            return 2
        else:
            return 0
        

solution = Solution()
print(solution.isWinner(player1 = [5,10,3,2], player2 = [6,5,7,3]))
print(solution.isWinner(player1 = [3,5,7,6], player2 = [8,10,10,2]))
print(solution.isWinner(player1 = [2,3], player2 = [4,1]))
print(solution.isWinner(player1 = [1,1,1,10,10,10,10], player2 = [10,10,10,10,1,1,1]))