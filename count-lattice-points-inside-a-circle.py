class Solution:
    def countLatticePoints(self, cir):
        res, omit, n = set(), set(), len(cir)
        def scan(x,y,r):
            r2 = r*r
            for i in range(x-r, x+r+1):
                v1 = (i-x)**2
                for j in range(y-r,y+r+1):
                    if (i,j) in res: continue
                    if v1 + (j-y)**2 <= r2: res.add((i,j))
        
        cir.sort(key=lambda x: x[2], reverse=True)
        def optimize():
            for i in range(n-1):
                x1,y1,r1 = cir[i]
                for j in range(i+1, n):
                    x2,y2,r2 = cir[j]
                    if (x1-x2)**2  + (y1-y2)**2 <= (r1 - r2)**2: omit.add(j)
        optimize()
        #print('cir', cir, 'omit list ', omit)
        for i in range(n):
            if i in omit: continue
            #print('scan', cir[i])
            scan(*cir[i])
            
        return len(res)
