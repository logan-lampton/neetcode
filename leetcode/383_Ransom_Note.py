# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

# Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false

# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false

# Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true

# Constraints:
# 1 <= ransomNote.length, magazine.length <= 105
# ransomNote and magazine consist of lowercase English letters.


def canConstruct(ransomNote: str, magazine: str) -> bool:
    for letter in ransomNote:
        if letter in magazine:
            magazine = magazine.replace(letter, "", 1)
        else:
            return False

    return True

# Practice:
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap = {}
        for char in magazine:
            if char not in hashmap:
                hashmap[char] = 1
            else:
                hashmap[char] += 1
        
        for char in ransomNote:
            if char not in hashmap or hashmap[char] == 0:
                return False
            hashmap[char] -= 1
        
        return True


# Practice:
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_hash = {}
        for char in magazine:
            if char not in magazine_hash:
                magazine_hash[char] = 1
            else:
                magazine_hash[char] += 1
        
        for char in ransomNote:
            if char not in magazine_hash:
                return False
            elif magazine_hash[char] == 0:
                return False
            else:
                magazine_hash[char] -= 1
        
        return True