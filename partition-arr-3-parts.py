from bisect import *
class Solution(object):
    def canThreePartsEqualSum(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        s,r,c = sum(A),0,0
        if s % 3 != 0: return False
        for i,k in enumerate(A):
            r+=k 
            if r == s/3: 
                #print 'i ',i
                r = 0
                c +=1
        if c ==3 and r == 0: return True
        return False

print Solution().canThreePartsEqualSum([0,2,1,-6,6,-7,9,1,2,0,1])
print Solution().canThreePartsEqualSum([0,2,1,-6,6,7,9,-1,2,0,1])
print Solution().canThreePartsEqualSum([3,3,6,5,-2,2,5,1,-9,4])
