class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        def do_findfactor(n):
            res = set([1])
            i = 2
            while i*i <=n:
                if n % i == 0: res.add(i)
                i+=1
            for i in list(res):
                res.add(n/i)
            return sorted(list(res))
        if n < 2: return 0
        l = do_findfactor(n)
        dp = [n+1]*(len(l))
        dp[0] = 0
        #print l
        for i in range(1,len(l)):
            for j in range(i):
                if l[i] % l[j] != 0: continue
                curr = dp[j] + l[i]/l[j]
                dp[i] = min(dp[i], curr)
                #print l[i], l[j], curr
        return dp[-1]

print Solution().minSteps(0)
print Solution().minSteps(1)
print Solution().minSteps(2)
print Solution().minSteps(36*9)
print Solution().minSteps(1000)
