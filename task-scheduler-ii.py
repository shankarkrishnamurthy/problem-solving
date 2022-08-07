class Solution:
    def taskSchedulerII(self, t, sp):
        nd, th = 0, defaultdict(int)
        for i,v in enumerate(t):
            nd = max(th[v], nd+1)
            th[v] = nd+sp+1
            #print('i', i+1, 'v', v, 'nd', nd, dict(th))
        return nd
