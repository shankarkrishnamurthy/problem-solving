class Solution(object):
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        ssf = [0]*len(A)
        if len(A) == 1: return A[0]
        for r in range(len(A)-1,-1,-1):
            cssf = [0]*len(A)
            for c in range(len(A)):
                print r,c ,ssf[c],A[r][c]
                cssf[c] = A[r][c] + min(ssf[c], ssf[c-1] if c>0 else 101,ssf[c+1] if c < len(A)-1 else 101)
            ssf = cssf
        return min(ssf)
        
#print Solution().minFallingPathSum([[1,2,3],[4,5,6],[7,8,9]])
#print Solution().minFallingPathSum([[-11,13],[8,-9]])
print Solution().minFallingPathSum([[-19,57],[-40,-5]])
