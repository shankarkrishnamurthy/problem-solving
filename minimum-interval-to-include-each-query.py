class Solution:
    def minInterval(self, iv, q):
        fh, hm, res = [], [], [-1]*len(q)
        for i,(a,b) in enumerate(iv):
            fh.append((a,0,i)), fh.append((b,2,i))
        for i,v in enumerate(q): fh.append((v,1,i))
        fh.sort()
        for (v, t, i) in fh:
            if t == 0:
                (a,b) = iv[i]
                heappush(hm, (b-a+1, b))
            elif t == 1:
                while hm and hm[0][1] < v: heappop(hm)
                if hm: res[i] = hm[0][0]
            else: pass
        return res
                
