class Solution(object):
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        def myrev(A, n):
            while n > 1:
                #print A, n,
                ma = max(A[:n])
                while n>1 and A[n-1] == ma:
                    n -= 1
                    ma = max(A[:n])
                if n < 2: return

                k = A.index(ma)
                #print ' k ', k+1
                if k > 0: res.append(k+1)
                rv = A[:k+1][::-1] + A[k+1:n]
                res.append(n)
                A = rv[::-1] + A[n+1:]
                n -= 1

        res = []
        myrev(A,len(A))
        return res

print Solution().pancakeSort([3,2,4,1])
print Solution().pancakeSort([1,2,3])
