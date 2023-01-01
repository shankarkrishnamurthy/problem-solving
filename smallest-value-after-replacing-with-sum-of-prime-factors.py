class Solution:
    def smallestValue(self, n):
        @lru_cache(None)
        def isPrime(n):
            for i in range(2,int(math.sqrt(n))+1):
                if n % i != 0: continue
                else: return  False
            return True

        def pfact(n):
            pf, mn = [], int(math.sqrt(n))+1
            for i in range(2,mn):
                if isPrime(i):
                    while n % i == 0:
                        pf.append(i)
                        n = n//i
                if n == 1: break
                i += 1
            if n != 1: pf.append(n)
            return pf
        pf = pfact(n)
        #print(n, pf)
        newn = sum(pf)
        while newn != n:
            n = newn
            pf=pfact(n)
            #print(n, pf)
            newn = sum(pf)
        return newn
