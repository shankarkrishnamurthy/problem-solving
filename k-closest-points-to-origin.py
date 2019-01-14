class Solution(object):
    def kClosest(self, p, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        d = []
        for k,i in enumerate(p):
            d.append((i[0]**2 + i[1]**2,k))
        d.sort()
        res = []
        for i in range(K):
            res.append(p[d[i][1]])
        return res

print Solution().kClosest([[1,3],[-2,2]], 1)
print Solution().kClosest([[3,3],[5,-1],[-2,4]], 2)
        
