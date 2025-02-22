# You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.

# Return a list answer of size 2 where:
# answer[0] is a list of all players that have not lost any matches.
# answer[1] is a list of all players that have lost exactly one match.
# The values in the two lists should be returned in increasing order.

# Note:
# You should only consider the players that have played at least one match.
# The testcases will be generated such that no two matches will have the same outcome.

# Example 1:
# Input: matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
# Output: [[1,2,10],[4,5,7,8]]
# Explanation:
# Players 1, 2, and 10 have not lost any matches.
# Players 4, 5, 7, and 8 each have lost one match.
# Players 3, 6, and 9 each have lost two matches.
# Thus, answer[0] = [1,2,10] and answer[1] = [4,5,7,8].

# Example 2:
# Input: matches = [[2,3],[1,3],[5,4],[6,4]]
# Output: [[1,2,5,6],[]]
# Explanation:
# Players 1, 2, 5, and 6 have not lost any matches.
# Players 3 and 4 each have lost two matches.
# Thus, answer[0] = [1,2,5,6] and answer[1] = [].

# Constraints:
# 1 <= matches.length <= 105
# matches[i].length == 2
# 1 <= winneri, loseri <= 105
# winneri != loseri
# All matches[i] are unique.


class Solution:
    def findWinners(self, matches: [[int]]) -> [[int]]:
        
        only_wins = []
        one_loss = []
        answer = [only_wins, one_loss]
        losses = {}

        for match in matches:
            if match[0] not in losses:
                losses[match[0]] = 0
            if match[1] not in losses:
                losses[match[1]] = 1
            elif match[1] in losses:
                losses[match[1]] += 1

        for key, value in losses.items():
            if value == 1:
                one_loss.append(key)
            elif value == 0:
                only_wins.append(key)
        
        only_wins.sort()
        one_loss.sort()

        return answer


solution = Solution()
print(solution.findWinners(matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]))
print(solution.findWinners(matches = [[2,3],[1,3],[5,4],[6,4]]))

# Practice:
from typing import List

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        all_wins = []
        one_loss = []
        hashmap = {}
        for winner, loser in matches:
            if winner not in hashmap:
                hashmap[winner] = [1, 0]
            elif winner in hashmap:
                hashmap[winner][0] += 1
            if loser not in hashmap:
                hashmap[loser] = [0, 1]
            elif loser in hashmap:
                hashmap[loser][1] += 1        
        
        for key, value in hashmap.items():
            if value[1] == 0:
                all_wins.append(key)
            elif value[1] == 1:
                one_loss.append(key)
        
        all_wins.sort()
        one_loss.sort()
        
        return [all_wins, one_loss]