class Solution:
    def squareFreeSubsets(self, nums: List[int]) -> int:
        @lru_cache(None)
        def getpf(n):
            for j in (4,9,16,25): 
                if n % j == 0: return -1
            res = 0
            for j in pr:
                if n % j == 0: res |= 1<<ph[j]
            return res
        pr=[2,3,5,7,11,13,17,19,23,29] # prime < 30
        n, ph= len(pr), {v:k for k,v in enumerate(pr)}
        dp, m=[0]*(1<<n), 1000000007
        for v in nums:
            bm = getpf(v)
            if bm==-1: continue
            ndp=list(dp)
            ndp[bm] += 1
            for i in range(1<<n):
                if i & bm: continue
                ndp[bm|i] += dp[i] % m
            dp = ndp
            #print(v, 'bitmask', bm, dp)
        return sum(dp) % m
