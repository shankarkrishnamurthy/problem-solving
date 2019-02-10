class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        c = 0
        res = []
        n = len(A)
        while n:
            a = A[n-1] % 10
            k = K % 10
            K = K/10 
            res.append((a+k+c) % 10)
            c = (a+k+c) / 10
            n -= 1
        while K > 0:
            k = K % 10
            K = K/10 
            res.append((k+c) % 10)
            c = (k+c) / 10
        if c>0:
            res.append(c)
        return res[::-1]
        
print Solution().addToArrayForm([0], 10000)
#print Solution().addToArrayForm([1,0], 9999)
#print Solution().addToArrayForm([0], 0)
#print Solution().addToArrayForm([1,2,0,0], 34)
#print Solution().addToArrayForm([2,7,4],181)
#print Solution().addToArrayForm([2,1,5], 806)
#print Solution().addToArrayForm([9,9,9,9,9,9,9,9,9,9], 1)
