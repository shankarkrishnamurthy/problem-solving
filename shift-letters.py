class Solution(object):
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        l = len(shifts)
        res,nsh,cumul=[],[0]*l,0
        for i in range(l-1, -1,-1):
            cumul += shifts[i]
            nsh[i] = cumul
        for i,v in enumerate(S):
            idx = ord(v) - 97
            nv = (idx + nsh[i]) % 26
            res.append(chr(nv + 97))
        return ''.join(res)

print Solution().shiftingLetters("a",[0])
print Solution().shiftingLetters("ad",[3,20])
print Solution().shiftingLetters("abc",[3,5,9])
