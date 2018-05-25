class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        h = { 'U': (0,-1), 'D': (0,1), 'L':(-1,0),'R':(1,0) }
        n=init = (0,0)
        for m in moves:
            n = tuple(map(sum, zip(n, h[m])))
            print m,n
        if (0,0) == n: 
            return True
        else:
            return False

print Solution().judgeCircle('UD')
print Solution().judgeCircle('ULDR')
print Solution().judgeCircle('ULDDR')
print Solution().judgeCircle("DURDLDRRLL")
