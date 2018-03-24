class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        sums = {0:1}
        for v in nums:
            currsum = {}
            for s in sums:
                ns1 = s + v
                ns2 = s - v
                if ns1 in currsum:
                    currsum[ns1] += sums.get(s, 1)
                else:
                    currsum[ns1] = sums.get(s, 1)
                if ns2 in currsum:
                    currsum[ns2] += sums.get(s, 1)
                else:
                    currsum[ns2] = sums.get(s, 1)
            print currsum
            sums = currsum    
        return sums.get(S,0)

#print Solution().findTargetSumWays([1,1,1,1],2)
print Solution().findTargetSumWays([0,0],0)
print Solution().findTargetSumWays([1,0],1)
#print Solution().findTargetSumWays([1,1,1,1,1],3)
