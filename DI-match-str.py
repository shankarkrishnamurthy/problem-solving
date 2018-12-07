class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        res = [] 
        l,r = 0, len(S)
        for v in S:
            if v == "I": 
                res.append(l)
                l += 1
            else:
                res.append(r)
                r -= 1
        return res+[l]

print Solution().diStringMatch("IDID")
print Solution().diStringMatch("III")
print Solution().diStringMatch("DDI")
