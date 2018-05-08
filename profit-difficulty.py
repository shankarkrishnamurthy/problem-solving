from bisect import *
class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        def biright(l, item, keyfunc):
            lo = 0
            hi = len(l)
            while lo < hi:
                mid = (lo+hi)//2
                if keyfunc(l[mid]) > keyfunc(item):
                    hi = mid
                else:
                    lo = mid+1
            return hi


        pl = []
        dp = [(v,profit[i]) for i,v in enumerate(difficulty)]
        dp.sort()
        print dp
        for i in range(1,len(dp)):
            if dp[i][1] < dp[i-1][1]: dp[i] = (dp[i][0],dp[i-1][1])
        for w in worker:
            idx = biright(dp, (w,0), lambda x: x[0])
            if idx == 0: 
                pl.append(0)
                continue
            pl.append(dp[idx-1][1])
        return sum(pl)

print Solution().maxProfitAssignment([68,35,52,47,86], [67,17,1,81,3], [92,10,85,84,82])

        
        
