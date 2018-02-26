class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        if l == 0: return 0
        dp = [0]*(l+1)
        dp[0] = 1
        for i in range(1,l+1):
            if i > 1:
                if int(s[i-2:i]) <= 26 and dp[i-2] > 0 and int(s[i-2:i]) > 0:
                    dp[i] += dp[i-2]
                if int(s[i-1:i]) <= 26 and dp[i-1] > 0 and int(s[i-1:i]) > 0:
                    dp[i] += dp[i-1]
            else:
                if int(s[i-1:i]) <= 26 and dp[i-1] > 0 and int(s[i-1:i]) > 0:
                    dp[i] += dp[i-1]
        return dp[i]

print Solution().numDecodings("10")
print Solution().numDecodings("")
print Solution().numDecodings("1")
print Solution().numDecodings("12")
print Solution().numDecodings("122")
print Solution().numDecodings("1223")
