class Solution(object):
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        def flip_row(A, r):
            for k in range(n): A[r][k] = int(not A[r][k])

        m,n,msf = len(A), len(A[0]),0
        for i in range(m):
            msf += 2**(n-1)
            if A[i][0] == 0: flip_row(A,i)

        for j in range(1,n):
            cnt = 0
            for i in range(m):
                if A[i][j] == 1: cnt += 1
            msf += (2**(n-1-j))*max(cnt, m-cnt)

        return msf

print Solution().matrixScore([[0,0,1,1],[1,0,1,0],[1,1,0,0]])
