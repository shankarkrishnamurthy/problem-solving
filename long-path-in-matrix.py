class Solution(object):
    def __init__(self):
        self.dp, self.m, self.n=[],0,0
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        def tracepath(matrix, coordinate):
            i,j = coordinate
            if self.dp[i][j] == 0:
                maxcur = 0
                for k,l in [(i,j+1),(i,j-1),(i+1,j),(i-1,j)]:
                    if k >= 0 and k < len(matrix) and l >= 0 and l < len(matrix[0]) and matrix[k][l] > matrix[i][j]:
                        #print (i,j)," => ",k,",",
                        val = tracepath(matrix,(k,l))
                        maxcur = val+1 if maxcur < val+1 else maxcur
                self.dp[i][j] = maxcur if maxcur>1 else 1
            return self.dp[i][j]
            
        if not matrix: return 0
        self.m = len(matrix)
        maxpath, self.n = 0, len(matrix[0])
        self.dp = [[0]*self.n for _ in range(self.m)]
        for i in range(self.m):
            for j in range(self.n):
                #print "start @", (i,j), ": ",
                curr = tracepath(matrix,(i,j))
                maxpath =curr if curr > maxpath else maxpath
                #print "curr ", curr, "max ",maxpath
        return maxpath

print Solution().longestIncreasingPath([[3,4,5],[3,2,6],[2,2,1]])
print Solution().longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]])
print Solution().longestIncreasingPath([[1]])
print Solution().longestIncreasingPath([[]])
