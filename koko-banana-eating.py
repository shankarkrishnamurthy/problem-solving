class Solution(object):
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        #print piles, 'H',H
        l,r = 1, max(piles)
        if H >= sum(piles): return 1
        if r == l: 
            h = H / len(piles)
            K = ((piles[0]-1)/h + 1)
        while r > l:
            hrs = H
            K = (l+r)/2
            #print l, r, K,
            for i in range(0,len(piles)):
                hrs -= (piles[i]-1)/K + 1

            #print 'hrs ', hrs
            if hrs < 0:
                l = K+1
            else:
                r = K
            K = l

        return  K

print Solution().minEatingSpeed([30,11,23,4,20],5)
print Solution().minEatingSpeed([30,11,23,4,20],6)
print Solution().minEatingSpeed([3,6,7,11],8)
print Solution().minEatingSpeed([1],1)
print Solution().minEatingSpeed([10],2)
print Solution().minEatingSpeed([11],3)
print Solution().minEatingSpeed([11],3)
print Solution().minEatingSpeed([11],1)
print Solution().minEatingSpeed([11,11,11],3)
print Solution().minEatingSpeed([11,11,11],6)
print Solution().minEatingSpeed([332484035, 524908576, 855865114, 632922376, 222257295, 690155293, 112677673, 679580077, 337406589, 290818316, 877337160, 901728858, 679284947, 688210097, 692137887, 718203285, 629455728, 941802184], 823855818)
