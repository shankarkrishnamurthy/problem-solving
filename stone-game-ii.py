class Solution(object):
    def __init__(self):
        self.dp={}
    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        def minimax(k,m):
            if k >= len(piles): return 0
            if (k,m) in self.dp: return self.dp[(k,m)]
            v=[]
            for i in range(1,2*m+1):
                 v.append(minimax(k+i,max(i,m)))
            ans = A[k] - min(v)
            self.dp[(k,m)] = ans
            return ans
        A,n = piles,len(piles)
        for i in xrange(n-2,-1,-1): A[i] += A[i+1]
        return minimax(0,1)


print(Solution().stoneGameII([2,7,9,4,4]))
print(Solution().stoneGameII([8,9,5,4,5,4,1,1,9,3,1,10,5,9,6,2,7,6,6,9]))

