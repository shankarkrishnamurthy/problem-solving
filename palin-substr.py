class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp,cnt = [[0]*len(s) for x in s],0
        for sz in range(1,len(s)+1):
            for i in range(0,len(s)-sz+1):
                if sz == 1:
                    dp[i][i] = 1
                    cnt += 1
                    continue
                j = i + sz -1
                if s[i:i+1] == s[j:j+1]:
                    if j-i < 3 or (j - i > 2 and dp[i+1][j-1] == 1):
                        dp[i][j] = 1
                        cnt += 1
                #print i, j, dp
        return cnt

#print Solution().countSubstrings("abba")
#print Solution().countSubstrings("aaa")
print Solution().countSubstrings("abc")
print Solution().countSubstrings("")
print Solution().countSubstrings("x")
