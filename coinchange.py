class Solution(object):
    def __init__(self):
        self.mall = -1
    def coinChange1(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        def do_cc(c, a, anc):
            if a == 0:
                self.mall = min(self.mall, len(anc))
                print anc
                return 
            if len(c)==0:
                return
            for i in range(len(c)):
                cnt = 1
                while c[i]*cnt <= a:
                    do_cc(c[:i]+c[i+1:], a-c[i]*cnt, anc + [c[i]]*cnt)
                    cnt += 1
        self.mall = amount + 1
        do_cc(coins, amount, [])
        return self.mall if self.mall < amount+1 else -1

    def coinChange2(self, coins, sum):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [ sum+1 for x in range(sum+1) ]
        dp[0] = 0
        for s in range(1,sum+1):
            for k in coins:
                cnt = 1
                #while cnt*k <= s:
                if cnt*k <= s:
                    dp[s] = min(dp[s], cnt + dp[s-cnt*k])
                    cnt += 1
        return dp[sum] if dp[sum] < sum+1 else -1
    def coinChange(self,coins,sum):
        print coins, " ", sum
        visited = [False]*sum
        if sum == 0: return 0
        queue = set([sum])
        cnt = 0
        while True:
            cnt += 1
            temp = set()
            for s in queue:
                for i in coins:
                    if s-i == 0:
                        return cnt
                    if s < i :
                        continue
                    if visited[s-i]:
                        continue
                    temp.add(s-i)
                    visited[s-i] = True
            queue = temp
            if not temp:
                return -1

print Solution().coinChange([1, 2, 5], 11)
print Solution().coinChange([3,7,405,436],8839)
print Solution().coinChange([2], 5)
print Solution().coinChange([1], 0)
print Solution().coinChange([27,352,421,198,317,110,461,31,264],5303)
print Solution().coinChange([125,146,125,252,226,25,24,308,50],8402)
