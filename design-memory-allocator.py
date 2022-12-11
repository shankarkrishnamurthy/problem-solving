class Allocator:

    def __init__(o, n: int):
        o.f, o.mid = [0]*n, defaultdict(int)
        return

    def allocate(o, size: int, mID: int) -> int:
        cs, sb = 0, -1
        for i in range(len(o.f)):
            if o.f[i] != 0: cs = 0
            else: cs += 1
            if cs == size: 
                sb = i - cs + 1
                break
        if sb == -1: return -1
        o.f[sb:sb+size] = [mID]*size
        o.mid[mID] += size
        #print('Alloc ', o.f)
        return sb

    def free(o, mID: int) -> int:
        if mID not in o.mid: return 0
        sz=0
        for i in range(len(o.f)):
            if o.f[i] == mID: o.f[i], sz = 0, sz + 1
            if sz == o.mid[mID]: break
        del o.mid[mID]
        #print('Del ', o.f)
        return sz


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.free(mID)
