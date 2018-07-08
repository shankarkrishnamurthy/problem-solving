class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if not n: True
        l = -1
        for i,v in enumerate(flowerbed):
            if not v: continue

            if l == -1:
                ra = i - 2
                la = 0
            else:
                ra = i - 2
                la = l + 2
            if ra - la >= 0: n -= (ra - la)/2 + 1
            l = i

        if l == -1:
            ra = len(flowerbed)-1
            la = 0
            n -= (ra - la)/2 + 1
        else:
            if l != len(flowerbed)-1:
                la = l + 2
                ra = len(flowerbed)-1
                if ra - la >= 0: n -= (ra - la)/2 + 1
            
        #print "n = ",n
        return n <= 0
            
        
print Solution().canPlaceFlowers([1,0,0,1], 1)
print Solution().canPlaceFlowers([1,0,0,0,0], 3)
print Solution().canPlaceFlowers([1,0,0,0,0], 2)
print Solution().canPlaceFlowers([0,0,0,0,0], 3)
print Solution().canPlaceFlowers([1,0,0,0,1], 1)
print Solution().canPlaceFlowers([1,0,0,0,1], 2)
