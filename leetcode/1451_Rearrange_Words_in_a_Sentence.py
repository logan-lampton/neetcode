# Given a sentence text (A sentence is a string of space-separated words) in the following format:

# First letter is in upper case.
# Each word in text are separated by a single space.
# Your task is to rearrange the words in text such that all words are rearranged in an increasing order of their lengths. If two words have the same length, arrange them in their original order.

# Return the new text following the format shown above.

# Example 1:
# Input: text = "Leetcode is cool"
# Output: "Is cool leetcode"
# Explanation: There are 3 words, "Leetcode" of length 8, "is" of length 2 and "cool" of length 4.
# Output is ordered by length and the new first word starts with capital letter.

# Example 2:
# Input: text = "Keep calm and code on"
# Output: "On and keep calm code"
# Explanation: Output is ordered as follows:
# "On" 2 letters.
# "and" 3 letters.
# "keep" 4 letters in case of tie order by position in original text.
# "calm" 4 letters.
# "code" 4 letters.

# Example 3:
# Input: text = "To be or not to be"
# Output: "To be or to be not"

# Constraints:
# text begins with a capital letter and then contains lowercase letters and single space between words.
# 1 <= text.length <= 10^5


class Solution:
    def arrangeWords(self, text: str) -> str:
        word_map = {}
        for word in text.split():
            len_word = len(word)
            if len_word not in word_map:
                if word_map:
                    word_map[len_word] = [word]
                else:
                    word_map[len_word] = [word.lower()]
            else:
                word_map[len_word].append(word)
        
        word_array = []
        for key, value in word_map.items():
            word_array.append((key, value))
        
        word_array.sort()
        answer_in_progress = [word[1] for word in word_array]
        
        answer = ''

        for words in answer_in_progress:
            cur_words = ' '.join(words)
            answer += cur_words
            answer += ' '
        
        final_answer = answer[0].upper() + answer[1:-1]
        
        return final_answer



solution = Solution()
print(solution.arrangeWords(text = "Leetcode is cool"))
print(solution.arrangeWords(text = "Keep calm and code on"))
print(solution.arrangeWords(text = "To be or not to be"))