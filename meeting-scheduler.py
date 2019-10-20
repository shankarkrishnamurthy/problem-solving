from typing import *
class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        evt = []
        for i in slots1:
            evt.append((i[0],0))
            evt.append((i[1],1))
        for i in slots2:
            evt.append((i[0],0))
            evt.append((i[1],1))
        evt.sort()
        s,n = 0,0 # start time of n==2
        for e in evt:
            a,b = e # time, start or end, user
            if not b:  # starting time
                n += 1
                if n == 2: d = a
            else: # ending time
                if n == 2 and a-d >=duration:
                    return [d,d+duration]
                n -= 1
        return []


print (Solution().minAvailableDuration(slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 12))
print (Solution().minAvailableDuration(slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8))
