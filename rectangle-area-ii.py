class Solution:
    def rectangleArea(self, rect):
        def getHgt():
            if not intv: return 0
            hgt, py = intv[0][1] - intv[0][0], intv[0][1]
            for i in range(1, len(intv)):
                y1,y2 = intv[i]
                ly = max(y1, py)
                py = max(y2, ly)
                hgt += max(0, (py - ly))
            return hgt
        evt = []
        for i,j,p,q in rect: _, __ = evt.append((i, 0, j, q)), evt.append((p, 1, j, q))
        evt.sort()
        #print("evt", evt)
        intv, res, px = [], 0, 0
        for x,t,y1,y2 in evt:
            hgt = getHgt()
            res += hgt * (x-px)
            #print("hgt @ ", x, "is ", hgt, "int", intv, "px", px, 'val', hgt * (x-px))
            px, res = x, res % 1000000007
            if t == 0: 
                intv.append((y1,y2))
                intv.sort()
            else: intv.remove((y1,y2))
        return res
