class Solution:
    def distinctPrimeFactors(self, nums: List[int]):
        ps = set()
        @lru_cache(None)
        def prime(i):
            for j in range(2, int(sqrt(i))+1):
                if i % j == 0: return False
            return True
        for i in nums:
            if prime(i): 
                ps.add(i)
                continue
            for j in range(2, int(sqrt(i))+1):
                #print(i, j, prime(j))
                q,r=divmod(i,j)
                if r != 0: continue
                if prime(j): ps.add(j)
                if prime(q): ps.add(q)
        print(ps)
        return len(ps)
