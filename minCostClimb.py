class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if len(cost) == 1 or len(cost) ==2:
            return cost[len(cost)-1]
        cost.append(0)
        dp=[]
        dp.insert(0,cost[0])
        dp.insert(1,cost[1])
        for i in range(2, len(cost)):
            dp.insert(i,min(dp[i-1], dp[i-2]) + cost[i])
        return dp[len(cost)-1]

print Solution().minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
print Solution().minCostClimbingStairs([1])
print Solution().minCostClimbingStairs([1,1])
print Solution().minCostClimbingStairs([1,1,2,1,2])
