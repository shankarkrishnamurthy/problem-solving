class Solution:
    def findValidSplit(self, nums):
        @lru_cache(None)
        def isPrime(n):
            for i in range(2,int(math.sqrt(n))+1):
                if n % i != 0: continue
                else: return False
            return True

        @lru_cache(None)
        def pFactHash(n):
            res = defaultdict(int)
            for i in range(2,int(math.sqrt(n))+1):
                if isPrime(i):
                    while n % i == 0: 
                        n //= i
                        res[i]+=1
                if n == 1: break
            if n != 1: 
                if isPrime(n): res[n] += 1
            return res

        ps, dp, cs, gs=set(), [], set(), defaultdict(int)
        for i in nums: 
            dp.append(pFactHash(i))
            for k in dp[-1]: gs[k] += dp[-1][k]

        for i in range(len(nums)-1):
            dh = dp[i]
            for p in dh:
                if gs[p] > dh[p]: cs.add(p)
                else:
                    if p in cs: cs.remove(p)
                gs[p] -= dh[p]
            if not cs: return i
        return -1
 
