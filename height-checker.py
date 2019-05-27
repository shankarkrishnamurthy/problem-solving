class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        hs,res = sorted(heights),0
        for i,v in enumerate(heights):
            if v != hs[i]: res+=1
        return res
            

print Solution().heightChecker([1,1,4,2,1,3])
print Solution().heightChecker([1,2,1,2,1,1,1,2,1])
