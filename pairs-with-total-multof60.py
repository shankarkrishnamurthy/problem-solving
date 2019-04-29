class Solution(object):
    def numPairsDivisibleBy60(self, t):
        """
        :type t: List[int]
        :rtype: int
        """
        h,res = {},0
        for i in t:
            m = i % 60
            h[m] = h.get(m, 0) + 1
        for i in range(1,30):
            if i in h and (60-i) in h:
                res += h[i] * h[60-i]
        if 30 in h: res += h[30]*(h[30]-1)/2
        if 0 in h: res += h[0]*(h[0]-1)/2
            
        return res

print Solution().numPairsDivisibleBy60([15,63,451,213,37,209,343,319])
print Solution().numPairsDivisibleBy60([30,20,150,100,40])
print Solution().numPairsDivisibleBy60([60,60,60])
