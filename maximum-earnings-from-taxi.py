from heapq import *
class Solution:
    def maxTaxiEarnings(self, n, r):
        rl, cmax = [], 0
        for i,v in enumerate(r):
            rl.append((v[0],1,i))
        heapify(rl)
        while len(rl) > 0:
            s,t,i = heappop(rl)
            if t:
                e,p = r[i][1], r[i][2]
                heappush(rl, (e, 0, cmax + e-s+p))
            else:
                cmax = max(cmax, i)
        return cmax

print(Solution().maxTaxiEarnings(5,[[2,5,4],[1,5,1]]))
print(Solution().maxTaxiEarnings(20, [[1,6,1],[3,10,2],[10,12,3],[11,12,2],[12,15,2],[13,18,1]]))
        
