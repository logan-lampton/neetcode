# You are given an array of strings words and a string chars.

# A string is good if it can be formed by characters from chars (each character can only be used once).

# Return the sum of lengths of all good strings in words.

# Example 1:
# Input: words = ["cat","bt","hat","tree"], chars = "atach"
# Output: 6
# Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.

# Example 2:
# Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
# Output: 10
# Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.

# Constraints:
# 1 <= words.length <= 1000
# 1 <= words[i].length, chars.length <= 100
# words[i] and chars consist of lowercase English letters.

class Solution:
    def countCharacters(self, words: [str], chars: str) -> int:
        dictionary = {}
        len_of_good_strings = 0
        for char in chars:
            if char not in dictionary:
                dictionary[char] = 1
            else:
                dictionary[char] += 1
        
        for word in words:
            dictionary_copy = dictionary.copy()
            for letter in word:
                if letter in dictionary_copy and dictionary_copy[letter] != 0:
                    dictionary_copy[letter] -= 1
                else:
                    len_of_good_strings -= len(word)
                    break
            len_of_good_strings += len(word)
                
        return len_of_good_strings

solution = Solution()
print(solution.countCharacters(words=["hello","world","leetcode"], chars="welldonehoneyr"))