# 14. Longest Common Prefix

# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.


class TrieNode:
    def __init__(self):
        self.end = False
        self.children = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()  # Create a new Trie node
            current = current.children[char]  # Move to the next node
        current.end = True  # Mark the last character as the end of a word


class Solution:
    def longestCommonPrefix(self, strs: [str]) -> str:
        trie = Trie()

        if not strs:
            return ""

        for word in strs:
            trie.insert(word)

        prefix = ""
        current = trie.root

        while len(current.children) == 1 and not current.end:
            char = list(current.children.keys())[0]
            prefix += char  # Use concatenation instead of append
            current = current.children[char]

        return prefix
