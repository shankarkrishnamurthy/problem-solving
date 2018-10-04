class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        area = 0
        myj = [0]*len(grid)
        for i in xrange(len(grid)-1,-1,-1):
            mxi = 0
            for j in xrange(len(grid)-1,-1,-1):
                if grid[i][j] > 0: area += 1
                mxi = max(mxi, grid[i][j])
                myj[j] = max(myj[j], grid[i][j])
            area += mxi
        for j in myj: area += j
        return area

print Solution().projectionArea([[1,0],[0,2]])# Output: 8
print Solution().projectionArea([[1,1,1],[1,0,1],[1,1,1]]) # Output: 14
print Solution().projectionArea([[2,2,2],[2,1,2],[2,2,2]]) # Output: 21
