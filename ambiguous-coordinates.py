import itertools as it
class Solution(object):
    def ambiguousCoordinates(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        def getvall(n):
            l = []
            if n[0] != '0' or (len(n) == 1): l.append(n)
            for d in range(1,len(n)):
                i,m = n[:d], n[d:]
                if i[0] == '0' and len(i) > 1: continue
                if m[-1] == '0': continue
                l.append(i+'.'+m)
            return l

        res = []
        S = S[1:len(S)-1]
        for c in range(1,len(S)):
            v1 = getvall(S[:c])
            #print '1.str ', S[:c], ' ans ', v1
            if not v1: continue
            v2 = getvall(S[c:])
            #print '2.str ', S[c:], ' ans ', v2
            if not v2: continue
            res += ['('+v[0]+','+' '+v[1]+')' for v in it.product(v1,v2)]
        return res

        
print Solution().ambiguousCoordinates("(123)")
print Solution().ambiguousCoordinates("(00011)")
print Solution().ambiguousCoordinates("(0123)")
print Solution().ambiguousCoordinates("(100)")
print Solution().ambiguousCoordinates("(0000001)")
