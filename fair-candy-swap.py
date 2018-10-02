class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        #print A,B
        sa = sum(A)
        sb = sum(B)
        sm,bi = (A,B) if sa < sb else (B,A)
        swap = False if sa < sb else True
        di = abs(sa - sb)
        bset = set(bi)
        for v in sm:
            lv = di/2 + v
            if lv in bset: return [lv, v] if swap else [v, lv]
        
print Solution().fairCandySwap([1,1],[2,2]) # Output: [1,2]
print Solution().fairCandySwap([1,2],[2,3]) # Output: [1,2]
print Solution().fairCandySwap([2],[1,3]) # Output: [2,3]
print Solution().fairCandySwap([1,2,5],[2,4]) #output: 5,4
