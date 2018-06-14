class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """

        m = len(A)
        n = len(B)
        if not m or not n: return 0
        dp , ml= [[0]*n for _ in range(m)], 0
        for i in range(m):
            for j in range(n):
                if A[i] == B[j]: 
                    prev = dp[i-1][j-1] if i > 0 and j > 0 else 0
                    curr = 1+ prev
                    dp[i][j] = curr
                    if curr > ml: ml = curr
        return ml
                

print Solution().findLength([],[1,2,3,2,1])
print Solution().findLength([0],[1,2,3,2,1])
print Solution().findLength([3],[1,2,3,2,1])
print Solution().findLength([1,2,3,2,1],[])
print Solution().findLength([1,2,3,2,1],[0])
print Solution().findLength([1,2,3,2,1],[3])
print Solution().findLength([1,2,3,2,1],[3,2,1,4,7])
print Solution().findLength([1,2,3,2,1],[2,1])
print Solution().findLength([1,2,3,2,1],[2,1])
