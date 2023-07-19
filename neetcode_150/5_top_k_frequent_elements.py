# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in
# any order.

class Solution(object):
    def topKFrequent(self, nums, k):
        # use bucket sort
        # hash map:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        print(freq)

        for num in nums:
            #  the count.get will return 0, if there is the num isn't already in the hash map
            count[num] = 1 + count.get(num, 0)
        for num, char in count.items():
            # num appears char times
            freq[char].append(num)
        result = []
        # length of freq, starting at the last index, going to 0 index, decrementing -1
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result
