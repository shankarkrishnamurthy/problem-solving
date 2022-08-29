class Solution:
    def garbageCollection(self, g, tr):
        mc, mi, pc, pi, gc, gi = 0,-1,0,-1,0,-1
        for i, v in enumerate(g):
            for t in v:
                if t == 'M': mc, mi = mc+1, i
                if t == 'G': gc, gi = gc+1, i
                if t == 'P': pc, pi = pc+1, i
        #print(mc, mi, pc, pi, gc, gi)
        tvg = 0 if gi == -1 else sum(tr[:gi]) + gc
        tvp = 0 if pi == -1 else sum(tr[:pi]) + pc
        tvm = 0 if mi == -1 else sum(tr[:mi]) + mc
        return tvg + tvp + tvm
