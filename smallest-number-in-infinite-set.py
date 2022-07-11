
from heapq import *
class SmallestInfiniteSet:

    def __init__(o):
        o.hl = []
        for i in range(1,1001): heappush(o.hl, i)
        o.s = set(o.hl)
    def popSmallest(o):
        v = heappop(o.hl)
        o.s.remove(v)
        return v

    def addBack(o, num):
        if num in o.s: return
        heappush(o.hl, num)
        o.s.add(num)

