class Solution(object):
    def minSwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        print ' A ', A
        print ' B ', B
        ans = 0
        n,s=[0],[1]
        for i in range(1,len(A)):
            n1 = n2 = s1 = s2 = None
            if A[i-1] < A[i] and B[i-1] < B[i]: 
                n1,s2 = n[-1], s[-1]+1
            if B[i-1] < A[i] and A[i-1] < B[i]: 
                s1,n2 = n[-1]+1, s[-1]

            if n1!=None and n2!=None: sn,nn = min(s1,s2), min(n1,n2)
            elif n1!=None: nn,sn = n1, s2
            else: nn,sn = n2, s1

            n.append(nn)
            s.append(sn)
        print ' n ', n
        print ' s ', s

        return min(n[-1],s[-1])

print Solution().minSwap([1,3,5,4], [1,2,3,7])
print Solution().minSwap([0,7,8,10,10,11,12,13,19,18],[4,4,5,7,11,14,15,16,17,20])
