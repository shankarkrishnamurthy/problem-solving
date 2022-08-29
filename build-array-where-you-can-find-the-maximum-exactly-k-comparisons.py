class Solution:
    def numOfArrays(self, n, m, k):
        @lru_cache(None)
        def walk(n,m,k):
            if n == 0: return 1
            if k < 1 or m < k: return 0
            res = 0
            for i in range(k-1,n):
                for j in range(k, m+1):
                    x = walk(i,j-1,k-1)
                    res = (res + x*(j**(n-1-i))) % mod
            #print("NOW ", n, m, k, "=", res)
            return res % mod
        mod = 1000000007
        return walk(n,m,k)
