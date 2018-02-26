class Solution(object):
    def wordBreak(self, str, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        def do_wb(s,e):
            for i in range(s,e):
                for j in range(i):
                    if wd.has_key(str[j:i]) and dp[j]:
                        dp[i] = True
                        break
            print dp
            return dp[e-1]

        l = len(str)
        wd = dict([(v,1) for v in wordDict])
        dp = [False]*(l+1)
        dp[0] = True
        return do_wb(0,l+1)
        
print Solution().wordBreak("a", ["b"])
print Solution().wordBreak("x", ["x"])
print Solution().wordBreak("leetcode", ["leet", "code"])
print Solution().wordBreak("agflm", ["a", "gf", "lm", "gfl", "l"])
print Solution().wordBreak("angflm", ["a", "gf", "lm", "gfl", "l"])

