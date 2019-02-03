# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[Interval]
        :type B: List[Interval]
        :rtype: List[Interval]
        """
        i,j = 0,0
        res = []
        while i < len(A) and j < len(B):
            As,Ae = (A[i].start,'B','A'),(A[i].end,'E','A')
            Bs,Be = (B[j].start,'B','B'),(B[j].end,'E','B')
            if Ae[0] < Bs[0]:
                i+=1
                continue
            if Be[0] < As[0]:
                j+=1
                continue
            
            a = sorted([As,Ae,Bs,Be])
            res.append([a[1][0],a[2][0]])
            if a[2][2] == 'B': j += 1
            else: i += 1
            
        return res
            
print Solution().intervalIntersection([[0,2],[5,10],[13,23],[24,25]],[[1,5],[8,12],[15,24],[25,26]])
print Solution().intervalIntersection([[0,10]],[[0,3],[5,6],[9,11]])
