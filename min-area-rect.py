class Solution:
    def minAreaRect(self, p):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        def A(x1,x2):
            return abs((x1[0]-x2[0])*(x1[1]-x2[1]))
            
        res = 40000**2+1
        ps = list(tuple(i) for i in p)
        n = len(p)
        for p1 in range(n):
            for p2 in range(p1+1,n):
                ca = A(p[p1],p[p2])
                if ca > 0 and ca < res:
                    p3 = (p[p1][0],p[p2][1])
                    p4 = (p[p2][0],p[p1][1])
                    if p3 in ps and p4 in ps:
                        res = ca
                    #print p1,p2,p3,p4, p[p1],p[p2], A(p[p1],p[p2])
        return 0 if res > 40000**2 else res
        
print Solution().minAreaRect([[1,1],[1,3],[3,1],[3,3],[2,2]])
print Solution().minAreaRect([[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]])
