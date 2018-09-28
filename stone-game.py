import numpy as np
class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        dp = [[0]*len(piles) for i in range(len(piles))]
        for sz in range(1,len(piles)+1):
            for i in range(sz,len(piles)+1):
                st = i-sz
                en = i-1
                if st >= en:
                    dp[st][st] = piles[st]
                else:
                    dp[st][en] = max(piles[st]-dp[st+1][en],piles[en]-dp[st][en-1])
        #print 'dp ', np.array(dp)
        return dp[0][-1] > 0

print Solution().stoneGame([5,3]) # true
print Solution().stoneGame([5,3,4,5]) # true
