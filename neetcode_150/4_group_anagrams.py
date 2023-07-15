class Solution(object):
    def groupAnagrams(self, strs):
        # hash map
        # mapping charCount to the list of anagrams
        # defaultdict(list) is built into python and helps us avoid an edgecase; count be written as: res = {}
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for char in s:
                # subtracting the ASCII character from the ASCII char of "a", so "a" = index 0, "b" = index 1, etc.
                count[ord(char) - ord("a")] += 1
            # change list to a tuple, as lists can't be keys (Python-specific)
            res[tuple(count)].append(s)
        return res.values()

# Takes O(m * n) time