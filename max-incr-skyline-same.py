class Solution(object):
    def maxIncreaseKeepingSkyline(self, g):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n,m = len(g),len(g[0])
        c,r = [0]*m,[0]*n
        for i,v in enumerate(g):
            r[i] = max(v)
            for j,w in enumerate(v):
                c[j] = max(c[j], w)
        ans = 0
        for i in range(n):
            for j in range(m):
                ans += min(r[i],c[j]) - g[i][j]

        return ans

print Solution().maxIncreaseKeepingSkyline([[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]])
