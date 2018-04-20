class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        mp, diff =[0], [0]
        for i in range(1,len(prices)):
            diff.append(prices[i] - prices[i-1])
            if diff[i] > 0:
                if diff[i-1] < 0 and i>2: 
                    mp.append(max(mp[i-3] + diff[i], mp[i-2] + diff[i-1] + diff[i], mp[i-2]))
                else: 
                    mp.append(mp[i-1] + diff[i])
            else: mp.append(mp[i-1])
            print (i,mp[i]),
        return mp[len(prices)-1]

"""
print Solution().maxProfit([1,2,3,0,2])
print Solution().maxProfit([3,0,2])
print Solution().maxProfit([2])
print Solution().maxProfit([1,2])
print Solution().maxProfit([1,2,1,3])
print Solution().maxProfit([2,1])
"""
print Solution().maxProfit([6,1,3,2,4,7])
