from heapq import *
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        print nums,k
        freq={}
        for v in nums:
            freq[v] = freq.get(v, 0) + 1
        
        return nlargest(k, freq, key=lambda x: freq[x])
            
        
print Solution().topKFrequent([1], 1)
print Solution().topKFrequent([], 0)
print Solution().topKFrequent([1,1,1,2,2,3], 2)
