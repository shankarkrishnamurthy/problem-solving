import numpy as np
class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        s1 = '#' + s1
        s2 = '#' + s2
        m = len(s1)
        n = len(s2)
        dp = [[0]*(n) for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                #print i,j, s1[i], s2[j]
                if i ==0 and j ==0: 
                    dp[i][j] = 0
                elif i ==0:
                    dp[i][j] = dp[i][j-1] + ord(s2[j])
                elif j == 0:
                    dp[i][j] = dp[i-1][j] + ord(s1[i])
                else:
                    if s1[i] == s2[j]:
                        dp[i][j] = dp[i-1][j-1]
                    else:
                        dp[i][j] = min(dp[i-1][j] + ord(s1[i]), dp[i][j-1]+ord(s2[j]))
        #print np.array(dp)
        return dp[m-1][n-1]
    
print Solution().minimumDeleteSum("", "")
print Solution().minimumDeleteSum("at", "ta")
print Solution().minimumDeleteSum("sea", "eat")
print Solution().minimumDeleteSum("delete", "leet")
