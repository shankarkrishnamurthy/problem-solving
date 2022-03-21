# Fenwick Tree (or) BIT (or) Binary Indexed Tree
class Solution:
    def goodTriplets(self, nums1, nums2):
        n, res, inv, ft=len(nums1), 0, {}, [0]*(len(nums1)+1)
        def lsofar(v):
            s, v = 0, v+1
            while v > 0:
                s += ft[v]
                v -= v & (-v)
            return s
        def add(v):
            v += 1
            while v < len(ft):
                ft[v] += 1
                v += v & (-v)
        for i in range(n): inv[nums2[i]] = i
        for i in range(n):
            mid = inv[nums1[i]]
            l = lsofar(mid)
            r = n - (i + mid - l) - 1
            res += l * r
            add(mid)
        return res
