class Solution:
    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        def countcycle(x,y):
            hv, h, h2={}, 1, 0
            while x!=0: hv[x], h, x = h, h+1, x>>1
            while y!=0:
                if y in hv: return hv[y]+h2
                h2, y = h2+1, y>>1
        res = []
        for a,b in queries:
            res.append(countcycle(a,b))
        return res
