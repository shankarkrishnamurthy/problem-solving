class Solution(object):
    def bagOfTokensScore(self, t, P):
        """
        :type tokens: List[int]
        :type P: int
        :rtype: int
        """
        t.sort()
        l,r,pt = 0, len(t), 0
        while l < r:
            if P >= t[l]:
                P -= t[l]
                l += 1
                pt += 1
            elif pt > 0 and r-l > 1:
                pt -= 1
                P += t[r-1]
                r -= 1
            else:
                return pt

        return pt
        
print Solution().bagOfTokensScore([100],50)
print Solution().bagOfTokensScore([100,200],150)
print Solution().bagOfTokensScore([100,200,300,400],200)
