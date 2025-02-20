# A pangram is a sentence where every letter of the English alphabet appears at least once.

# Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

# Example 1:
# Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
# Output: true
# Explanation: sentence contains at least one of every letter of the English alphabet.

# Example 2:
# Input: sentence = "leetcode"
# Output: false

# Constraints:
# 1 <= sentence.length <= 1000
# sentence consists of lowercase English letters.

def checkIfPangram(sentence: str) -> bool:
    
    hash_map = {}
    for i in range(len(sentence)):
        if sentence[i] not in hash_map:
            hash_map[sentence[i]] = 1 
        if len(hash_map) == 26:
            return True
    return False

# practice/different method:
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet = "abcdefghijklmnopqrstuvwxyz"

        for char in alphabet:
            if char not in sentence:
                return False
        return True
