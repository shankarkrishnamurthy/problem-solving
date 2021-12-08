from heapq import *
class Solution:
    def kthSmallest(self, m, k):
        n,vis,hl,c = len(m),set((0,0)),[(m[0][0],0,0)],0
        while hl and c < k:
            (v,a,b),c = heappop(hl),c+1
            if a < n-1 and (a+1,b) not in vis:
                heappush(hl, (m[a+1][b],a+1,b))
                vis.add((a+1,b))
            if b < n-1 and (a,b+1) not in vis:
                heappush(hl, (m[a][b+1],a,b+1))
                vis.add((a,b+1))
        
        return v

print(Solution().kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8))
print(Solution().kthSmallest([[-5]], 1))
