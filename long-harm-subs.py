class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nh = {}
        for i in nums:
            nh[i] = nh.get(i,0) + 1
        mv = 0
        for i in nh:
            if nh.has_key(i-1):
                mv = max(mv, nh[i-1]+nh[i])
        return mv

print Solution().findLHS([1,2,3,4])
print Solution().findLHS([1,3,2,2,5,2,3,7])
            
