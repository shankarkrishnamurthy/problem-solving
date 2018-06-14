class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        #print "Input ",seats
        l,r,md = -1,0,0
        while True:
            while r < len(seats) and seats[r] == 0: r+= 1
            if r == len(seats):
                mdist = len(seats) - l - 1
                #print l, r, mdist
                if mdist > md: md = mdist
                return md
            if l == -1:
                mdist = r
            else:
                mdist = (r-l)/2
            #print l, r, mdist
            if mdist > md: md = mdist
            l = r
            r +=1

print Solution().maxDistToClosest([0,0,0,1,0,1])
print Solution().maxDistToClosest([0,1])
print Solution().maxDistToClosest([1,0])
print Solution().maxDistToClosest([1,0,0,0,1,0,1])
print Solution().maxDistToClosest([1,0,0,0])
