class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        h={'b':0,'a':0,'n':0,'l':0,'o':0}
        for i in text: h[i] = h.get(i,0)+1
        res = min(h['b'],h['a'],h['n'],h['l']/2,h['o']/2)
        return res
            
        
print Solution().maxNumberOfBalloons("loonbalxballpoon")
print Solution().maxNumberOfBalloons("nlaebolko")
print Solution().maxNumberOfBalloons("nlaeblko")
print Solution().maxNumberOfBalloons("leetcode")
