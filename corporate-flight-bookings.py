from typing import *
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        be = []
        for b in bookings:
            be.append((b[0],0,b[2]))
            be.append((b[1],1,b[2]))
        be.sort()
        rc,cr = [0]*(n+1),0
        #print(rc)
        for i,(f,sRe,v) in enumerate(be):
            #print((f,sRe,v)),
            if i==0: 
                rc[1:f] = [cr]*(f-1)
            else:
                p = be[i-1][0]
                if p != f:
                    rc[p+1:f] = [cr]*(f-p)
            if sRe: cr -= v
            else: cr += v
            rc[f] = max(rc[f],cr)
            #print(cr,rc)
                
        return rc[1:n+1]

print(Solution().corpFlightBookings(bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5))
print(Solution().corpFlightBookings(bookings = [[2,4,10],[2,3,20]], n = 6))
print(Solution().corpFlightBookings(bookings = [[3,4,10],[3,4,20]], n = 7))
