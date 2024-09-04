# Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.

# The words in paragraph are case-insensitive and the answer should be returned in lowercase.

# Example 1:
# Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
# Output: "ball"
# Explanation: 
# "hit" occurs 3 times, but it is a banned word.
# "ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
# Note that words in the paragraph are not case sensitive,
# that punctuation is ignored (even if adjacent to words, such as "ball,"), 
# and that "hit" isn't the answer even though it occurs more because it is banned.

# Example 2:
# Input: paragraph = "a.", banned = []
# Output: "a"

# Constraints:
# 1 <= paragraph.length <= 1000
# paragraph consists of English letters, space ' ', or one of the symbols: "!?',;.".
# 0 <= banned.length <= 100
# 1 <= banned[i].length <= 10
# banned[i] consists of only lowercase English letters.


class Solution:
    def mostCommonWord(self, paragraph: str, banned: [str]) -> str:
        hash_table = {}

        paragraph = paragraph.lower()
        cleaned_paragraph = ""
        symbols = "!?',;."

        for char in paragraph:
            if char in symbols or char == " ":
                cleaned_paragraph += " "
            else:
                cleaned_paragraph += char
        
        words = cleaned_paragraph.split()
        
        for word in words:
            if word not in hash_table:
                hash_table[word] = 1
            else:
                hash_table[word] += 1
        
        greatest_key = None
        greatest_occurance = 0

        for key, value in hash_table.items():
            if key not in banned:
                if value > greatest_occurance:
                    greatest_occurance = value
                    greatest_key = key
        
        return greatest_key
    

solution = Solution()
print(solution.mostCommonWord(paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]))
print(solution.mostCommonWord(paragraph = "a.", banned = []))