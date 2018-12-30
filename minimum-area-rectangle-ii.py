import math
class Solution(object):
    def minAreaFreeRect(self, p):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        def isra(p1,p2,p3):
            print p1,p2,p3
            d1 = (abs(p2[0]-p1[0]))**2 + (abs(p2[1] - p1[1]))**2
            d2 = abs(p2[0] - p3[0])**2 + abs(p2[1] - p3[1])**2
            d3 = abs(p3[0] - p1[0])**2 + abs(p3[1] - p1[1])**2
            if d1 + d2 == d3: # p2
                p4 = (p1[0]+p3[0]-p2[0],p1[1]+p3[1]-p2[1])
                a = d1*d2
            elif d2 + d3 == d1: # p3
                p4 = (p1[0]+p2[0]-p3[0],p1[1]+p2[1]-p3[1])
                a = d2*d3
            elif d1 + d3 == d2: # p1
                p4 = (p2[0]+p3[0]-p1[0],p2[1]+p3[1]-p1[1])
                a = d1*d3
            else: return (None,0)
            if p4 not in ps: return (None,0)
            return (p4,math.sqrt(a))

        res = 80000**2+1
        ps = list(tuple(i) for i in sorted(p))
        print ps
        n = len(p)
        for p1 in range(n):
            for p2 in range(p1+1,n):
                for p3 in range(p2+1,n):
                    rc,ar = isra(ps[p1],ps[p2],ps[p3])
                    if rc and ar > 0:
                        res = min(res,ar)

        return 0 if res > 80000**2 else res
        

print Solution().minAreaFreeRect([[1,2],[2,1],[1,0],[0,1]])
print Solution().minAreaFreeRect([[0,1],[2,1],[1,1],[1,0],[2,0]])
print Solution().minAreaFreeRect([[0,3],[1,2],[3,1],[1,3],[2,1]])
print Solution().minAreaFreeRect([[3,1],[1,1],[0,1],[2,1],[3,3],[3,2],[0,2],[2,3]])
