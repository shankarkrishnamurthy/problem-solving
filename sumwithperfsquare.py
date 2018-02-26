class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        sqlist=[]
        i=1
        while i*i<=n:
            sqlist.append(i*i)
            i+=1
        nlist=[n]
        count=0
        while True:
            temp=set()
            count+=1 
            print nlist
            for e in nlist:
                for v in sqlist:
                    if e==v:
                        return count
                    if e<v:
                        break
                    temp.add(e-v)
                nlist=temp

    def __init__(self):
        self.cnt = 0
    def numSquares2(self, n):
        """
        :type n: int
        :rtype: int
        """
        def do_ns(idx, sum, cnt):
            #print idx, sum, cnt
            if sum <0 or idx < 0:
                return
            if sum == 0:
                #print "min ",cnt
                self.cnt = min (self.cnt, cnt)
            for i in range(idx,0,-1):
                multi = 1
                while multi*i*i<=sum:
                    do_ns(idx-1, sum-i*i*multi, cnt+multi)
                    multi += 1
        idx = 1 
        while idx*idx <= n:
            idx += 1
        self.cnt = n+1
        do_ns(idx,n,0)
        return self.cnt

    def numSquares1(self, n):
        """
        :type n: int
        :rtype: int
        """
        def coinChange(coins, sum):
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
        idx = 1 
        c = []
        while idx*idx <= n:
            c += [ idx*idx ]
            idx += 1
        return coinChange(c, n)

#print Solution().numSquares(1)
print Solution().numSquares(12)
#print Solution().numSquares(13)

