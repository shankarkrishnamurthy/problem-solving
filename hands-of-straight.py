class Solution(object):
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        hv = {}
        for v in hand: hv[v] = hv.get(v, 0) + 1

        for k in sorted(hv):
            c = hv[k]
            if c <= 0: continue
            for i in range(W):
                if not hv.has_key(k+i) or (k+i in hv and hv[k+i] < c):
                    return False
                else:
                    hv[k+i] -= c
        return True
            
print Solution().isNStraightHand([8], 1)
print Solution().isNStraightHand([1,2,3,6,2,3,4,7,8], 3)
print Solution().isNStraightHand([1,2,3,4,5], 4)
