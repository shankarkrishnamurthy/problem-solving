class Solution:
    def longestAwesome(self, s):
        hv, res, vh, ctot = {str(i):1<<i for i in range(10)}, 0, defaultdict(int), 0
        vh[0] = -1
        for i, c in enumerate(s):
            ctot, d = ctot ^ hv[c], 1
            if not ctot in vh:
                vh[ctot] = i
            else: 
                d = i - vh[ctot]
            for j in range(10):
                t = ctot^(1<<j)
                if t in vh: 
                    d= max(d, (i - vh[t] if i != vh[t] else i+1))
            res = max(res, d)
        return res
            
