class Solution:
    def canIWin(self, mci, dt):
        def ciw(st, r):
            if r<=0: return False
            if vis[st] != -1: return vis[st]
            for i in range(mci):
                if st & 1<<i > 0: continue
                if not ciw(st|1<<i, r - i - 1):
                    vis[st] = 1
                    return True
            vis[st] = 0
            return False
        if mci*(mci+1)/2 < dt: return False
        if dt == 0: return True
        if mci*(mci+1)/2 == dt: return mci % 2
        vis = [-1]*(1<<mci)
        return ciw(0, dt)
