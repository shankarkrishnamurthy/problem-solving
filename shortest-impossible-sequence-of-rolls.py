class Solution:
    def shortestSequence(self, r, k):
        cur, sfs = set(), 0
        for v in r:
            cur.add(v)
            if len(cur) == k:
                sfs += 1 # seen full sequence
                cur = set()
        return sfs+1
