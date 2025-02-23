# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

# You can use each character in text at most once. Return the maximum number of instances that can be formed.

# Example 1:
# Input: text = "nlaebolko"
# Output: 1

# Example 2:
# Input: text = "loonbalxballpoon"
# Output: 2

# Example 3:
# Input: text = "leetcode"
# Output: 0

# Constraints:
# 1 <= text.length <= 104
# text consists of lower case English letters only.


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        b_count = text.count("b")
        a_count = text.count("a")
        l_count = text.count("l") // 2
        o_count = text.count("o") // 2
        n_count = text.count("n")

        return min(b_count, a_count, l_count, o_count, n_count)


solution = Solution()
print(
    solution.maxNumberOfBalloons(
        text="krhizmmgmcrecekgyljqkldocicziihtgpqwbticmvuyznragqoyrukzopfmjhjjxemsxmrsxuqmnkrzhgvtgdgtykhcglurvppvcwhrhrjoislonvvglhdciilduvuiebmffaagxerjeewmtcwmhmtwlxtvlbocczlrppmpjbpnifqtlninyzjtmazxdbzwxthpvrfulvrspycqcghuopjirzoeuqhetnbrcdakilzmklxwudxxhwilasbjjhhfgghogqoofsufysmcqeilaivtmfziumjloewbkjvaahsaaggteppqyuoylgpbdwqubaalfwcqrjeycjbbpifjbpigjdnnswocusuprydgrtxuaojeriigwumlovafxnpibjopjfqzrwemoinmptxddgcszmfprdrichjeqcvikynzigleaajcysusqasqadjemgnyvmzmbcfrttrzonwafrnedglhpudovigwvpimttiketopkvqw"
    )
)

# Practe/different method:
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        if "b" not in text or "a" not in text or "l" not in text or "o" not in text or "n" not in text:
            return 0

        hashmap = {}

        for char in text:
            if char == "b" or char == "a" or char == "l" or char == "o" or char == "n":
                if char not in hashmap:
                    hashmap[char] = 1
                else:
                    hashmap[char] += 1
        
        number_of_balloons = 0

        while hashmap["b"] > 0 and hashmap["a"] > 0 and hashmap["l"] >= 2 and hashmap["o"] >= 2 and hashmap["n"] > 0:
            number_of_balloons += 1
            hashmap["b"] -= 1
            hashmap["a"] -= 1
            hashmap["l"] -= 2
            hashmap["o"] -= 2
            hashmap["n"] -= 1
        
        return number_of_balloons
