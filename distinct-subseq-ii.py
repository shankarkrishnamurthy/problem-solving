class Solution:
    def distinctSubseqII(self, S):
        """
        :type S: str
        :rtype: int
        """
        dp = [0]
        prev = dict()
        for i,v in enumerate(S):
            c = dp[i]*2+1
            if v in prev:
                c -= (dp[prev[v]]+1)
            dp.append(c)
            prev[v] = i
        print dp
        return dp[len(S)] % (10**9+7)
 
print Solution().distinctSubseqII("abc")
print Solution().distinctSubseqII("aba")
print Solution().distinctSubseqII("aaa")
print Solution().distinctSubseqII("lee")
