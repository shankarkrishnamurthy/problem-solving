class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2: return 0
        res,high,low=0,0,0
        for i in range(1,len(prices)):
            if prices[i] < prices[i-1]:
                if high > low: res += prices[high] - prices[low]
                low = i
            else:
                high = i
        res += prices[high]-prices[low] if high > low else 0
        return res

print Solution().maxProfit([1,2,3,4,5])
print Solution().maxProfit([7,5,3,1])
print Solution().maxProfit([7,3,5,8,4])
