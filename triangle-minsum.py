class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        print triangle,
        r = len(triangle)
        if not r: return 0
        if r and not triangle[0]: return 0
        if r == 1: return triangle[0][0]
        for i in range(r-2,-1,-1):
            cr = triangle[i]
            crn = triangle[i+1]
            for j in range(i,-1,-1):
                cr[j] += min(crn[j], crn[j+1])
        return triangle[0][0]

#print Solution().minimumTotal( [ [2] ])
#print Solution().minimumTotal( [ [] ])
#print Solution().minimumTotal( [ [4], [1,7 ]])
#print Solution().minimumTotal( [ [2], [3,4], [6,5,7], [4,1,8,3] ])
print Solution().minimumTotal( [[-1],[2,3],[1,-1,-1]] )
