class Solution(object):
    def containsDuplicate(self, nums):
        # hash set
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False