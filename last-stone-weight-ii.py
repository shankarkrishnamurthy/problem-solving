class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        dp,s={0:0},sum(stones)
        for i in stones:
            for x in dp.keys():
                dp[i+x]=dp.get(i+x,0) + 1
        #print dp
        return min([abs(s-2*i) for i in dp])
        
print Solution().lastStoneWeightII([2,1,4,1,8,7])
