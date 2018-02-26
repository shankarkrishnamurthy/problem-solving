import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        #nums = heapq.nsmallest(k, nums)
        #return nums[k-1]
        return heapq.nlargest(k, nums)[k-1]

print "Solution: ", Solution().findKthLargest([3,5,2,4,1,6], 5)
print "Solution: ", Solution().findKthLargest([3,2,4,1,6], 2)
print "Solution: ", Solution().findKthLargest([3,6], 1)
print "Solution: ", Solution().findKthLargest([3,2,1,5,6,4], 2)
