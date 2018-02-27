class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        val = [[1 for j in range(n)] for i in range(m)]
        print val
        for i in range(1, m):
            for j in range(1,n):
                val[i][j] = val[i-1][j] + val[i][j-1]
        return val[m-1][n-1]

print "val: ", Solution().uniquePaths(3,7)

