class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        ps,fleetcnt,prev = zip(position,speed),0, None
        ps.sort(reverse=True)
        for p,s in ps:
            d = target - p
            t = float(d)/float(s)  # time to reach target
            if not prev:
                prev = t
                fleetcnt = 1
            else:
                if t > prev:
                    prev = t
                    fleetcnt += 1
            print p, s, t, fleetcnt
        return fleetcnt
            
        

print Solution().carFleet(100, [1],  [3])
print Solution().carFleet(100, [1,10],  [3,1])
print Solution().carFleet(12, [],  [])
#print Solution().carFleet(12, [10,8,0,5,3],  [2,4,1,1,3])
