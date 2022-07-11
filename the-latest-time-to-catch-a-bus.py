class Solution:
    def latestTimeCatchTheBus(self, b, p, cap):
        lp, j, np, i = -1, 0, 0, 0
        b.sort(), p.sort()
        while i < len(p):
            t = p[i]
            if t <= b[j] and np < cap: 
                lp, np = i, np+1
            else:
                if j == len(b)-1: break
                j, np= j+1, 0
                continue
            i += 1
        pt,ps = p[lp], set(p)
        if np != cap or j != len(b)-1: pt = b[-1]
        while pt in ps: pt -= 1
        #print('lp', lp, 'bus', b, 'passenger', p, 'busptr', j)
        return pt
        
        
