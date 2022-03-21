from heapq import *
class B:
    def __init__(o,s,n):o.val = (s,n)
    def __repr__(o):return str(o.val)
class N(B):
    def __lt__(o,oth):
        if o.val[0] == oth.val[0]: return oth.val[1] < o.val[1]
        else: return o.val[0] < oth.val[0]
class M(B):
    def __lt__(o,oth):
        if o.val[0] == oth.val[0]: return oth.val[1] > o.val[1]
        else: return o.val[0] < oth.val[0]
class SORTracker:
    def __init__(o): o.minh, o.maxh, o.i = [],[], 0
    def swap(o, a, b):
        e = heappop(a)
        if type(e) == N: v = M(-e.val[0],e.val[1])
        else: v = N(-e.val[0],e.val[1])
        heappush(b, v)
    def add(o, name: str, score: int) -> None:
        c = N(score,name)
        if  o.i == (len(o.minh) + len(o.maxh)): heappush(o.minh,c)
        else:
            if o.minh[0] < c: # better score
                o.swap(o.minh,o.maxh)
                heappush(o.minh,c)
            else: heappush(o.maxh,M(-score,name))
        return

    def get(o) -> str:
        res = o.minh[0]
        o.i += 1
        if o.i != (len(o.minh) + len(o.maxh)): o.swap(o.maxh, o.minh)
        return res.val[1]

# Your SORTracker object will be instantiated and called as such:
# obj = SORTracker()
# obj.add(name,score)
# param_2 = obj.get()
