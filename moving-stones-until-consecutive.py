class Solution(object):
    def numMovesStones(self, x, y, z):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        def findmin(i,j,k):
            if j-i == 1 and k-j ==1: return 0
            if j-i<=2 or k-j<=2: return 1
            return 2
        a,b,c = sorted([x,y,z])
        mi = findmin(a,b,c)
        ma = b-a-1 + c-b-1
        return [mi,ma]

print Solution().numMovesStones(1,2,5)
print Solution().numMovesStones(4,3,2)
print Solution().numMovesStones(3,5,1)

