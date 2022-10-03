#Fenwick Tree or BIT 
class FenwickTree:
    def _update(o, i, v):
        while i < len(o.bit):
            o.bit[i] += v
            i += i & -i
    def _query(o, i):
        if i == 0: return 0
        s = 0
        while i:
            s += o.bit[i]
            i -= i & -i
        return s
    def __init__(o, n):o.bit = [0]*(n+1)
    def update(o, index, val): o._update(index+1, val)
    def countSoFar(o, i): return o._query(i+1)
    
class Solution:
    def numberOfPairs(self, nums1, nums2, diff):
        res, ft, ofs = 0, FenwickTree(60001), 30000
        for a,b in zip(nums1, nums2):
            res += ft.countSoFar(ofs + a - b + diff)
            ft.update(ofs + a - b, 1)
        return res
