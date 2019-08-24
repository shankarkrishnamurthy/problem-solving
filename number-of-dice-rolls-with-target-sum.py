class Solution(object):
    def numRollsToTarget(self, d, f, target):
        """
        :type d: int
        :type f: int
        :type target: int
        :rtype: int
        """
        if d > target or target > d*f: return 0
        th = {i:1 for i in xrange(1,f+1)}
        while d>1:
            ch = {}
            for t in sorted(th.keys()):
                s = sum([th[x] for x in xrange(t-1,t-f-1,-1) if x in th])
                if s > 0: ch[t] = s
                
            for y in xrange(t+1,t+f+1):
                ch[y] = sum([th[x] for x in xrange(y-1,y-f-1,-1) if x in th])
            th = ch
            d -= 1
        
        return th[target] % (10**9 + 7)

print Solution().numRollsToTarget(d= 10, f = 6, target = 3)
print Solution().numRollsToTarget(d= 1, f = 6, target = 3)
print Solution().numRollsToTarget(d = 2, f = 6, target = 7)
print Solution().numRollsToTarget(d = 3, f = 6, target = 5)
print Solution().numRollsToTarget(d = 30, f = 30, target = 500)
print Solution().numRollsToTarget(30,30, 700)
print Solution().numRollsToTarget(d = 30, f = 30, target = 1000)
