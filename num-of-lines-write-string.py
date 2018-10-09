class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        def getwidth(c): return widths[ord(c)-ord('a')]
        l,w = 1,0
        for v in S:
            cw = getwidth(v)
            if w + cw > 100:
                w = cw
                l += 1
            else:
                w += cw
        return [l,w]

print Solution().numberOfLines([10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], "abcdefghijklmnopqrstuvwxyz")
print Solution().numberOfLines([4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], "bbbcccdddaaa")
                
            
            
