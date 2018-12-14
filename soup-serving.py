class Solution(object):
    def soupServings(self, N):
        """
        :type N: int
        :rtype: float
        """
        if N > 7000 : return 1.0
        dp,ans = { (N,N): 1.0 },0
        while dp:
            new = {}
            print dp
            for a,b in dp:
                if a<=0 or b <=0:
                    if a == b: ans += 0.5 * dp[(a,b)]
                    elif a < b: ans += dp[(a,b)]
                else:
                    val = dp[(a,b)]*0.25
                    for i,j in [(100,0),(75,25),(50,50),(25,75)]:
                        new[(a-i,b-j)] = new.get((a-i,b-j),0)+val
            dp = new
        return ans

print Solution().soupServings(1)
"""
print Solution().soupServings(50)
print Solution().soupServings(200)
print Solution().soupServings(2000)
print Solution().soupServings(5000)
print Solution().soupServings(7000)
"""
