class Solution(object):
    def maxSumTwoNoOverlap(self, A, L, M):
        """
        :type A: List[int]
        :type L: int
        :type M: int
        :rtype: int
        """
        n,msf,Ls,Ms = len(A),0,[],[]
        for i in xrange(1,len(A)): A[i] += A[i-1]
        #print A, 'L', L, 'M ',M
        for i in xrange(n-L+1): Ls.append((A[i+L-1]-A[i-1] if i > 0 else A[i+L-1], i))
        for i in xrange(n-M+1): Ms.append((A[i+M-1]-A[i-1] if i > 0 else A[i+M-1], i))
        for i in Ls:
            for j in Ms:
                if j[1]+M-1 < i[1] or i[1]+L-1 < j[1]:
                    if i[0] + j[0] > msf:
                        msf = i[0] + j[0]
        return msf

print Solution().maxSumTwoNoOverlap([0,6,5,2,2,5,1,9,4],1,2)
print Solution().maxSumTwoNoOverlap([3,8,1,3,2,1,8,9,0],3,2)
print Solution().maxSumTwoNoOverlap([2,1,5,6,0,9,5,0,3,8], 4, 3)
