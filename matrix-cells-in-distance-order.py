class Solution(object):
    def allCellsDistOrder(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        res = []
        for i in xrange(R):
            for j in xrange(C):
                res.append((abs(i-r0)+abs(j-c0),[i,j]))
        res.sort()
        return [x[1] for x in res]

print Solution().allCellsDistOrder(1,2,0,0)
print Solution().allCellsDistOrder(2,2,0,1)
print Solution().allCellsDistOrder(2,3,1,2)
