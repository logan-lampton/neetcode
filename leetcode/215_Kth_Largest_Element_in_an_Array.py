# Given an integer array nums and an integer k, return the kth largest element in the array.
#
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
#
# Can you solve it without sorting?

# Example 1:
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5

# Example 2:
# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4

import heapq

def findKthLargest(self, nums, k):
    # In a max-heap, the max-heap property states that for each node, its value is greater than or equal to the values
    # of its children. This property ensures that the largest element is at the root.
    max_heap = []

    for num in nums:
        if len(max_heap) < k:
            # special heappush method that takes two arguments; the heap you want to push to, and the element you want
            # to add to that heap

            # After adding the element to the heap, the function rearranges the heap's elements to ensure that the heap
            # property is maintained.

            # This process maintains the max-heap property, as the new element num will bubble up to a suitable position
            # in the heap where it's larger than its parent and smaller than its children, thus preserving the max-heap
            # structure.
            heapq.heappush(max_heap, num)

        else:
            if max_heap[0] < num:
                # special method to pop off the head of the heap to remove the smallest value
                heapq.heappop(max_heap)
                # push this larger element to the heap
                heapq.heappush(max_heap, num)

    # the max_heap's first element is the smallest, so it will be the kth smallest element in the array, as all the
    # larger elements will be deeper in the heap
    return max_heap[0]
