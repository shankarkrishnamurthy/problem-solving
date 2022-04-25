class Solution:
    def getPermutation(self, n, k):
        fl = [1,1,2,6,24,120,720,5040,40320,362880]
        res, rl = "", list(map(str, range(1,n+1)))
        k -= 1
        for i in range(n-1,-1,-1):
            j, r = divmod(k, fl[i])
            res += rl.pop(j)
            k = r
        return res
