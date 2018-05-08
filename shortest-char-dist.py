class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        cil = [i for i,v in enumerate(S) if v == C]
        res = []
        for i,v in enumerate(S):
            d = min([abs(k-i) for k in cil])
            res.append(d)
        return res

print Solution().shortestToChar("loveleetcode", 'e')
print Solution().shortestToChar("le", 'e')
