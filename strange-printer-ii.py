class Solution:
    def isPrintable(self, targetGrid):
        m, n, r = len(targetGrid), len(targetGrid[0]), defaultdict(list)
        def testrect(c):
            x1, y1, x2, y2 = r[c][0][0], r[c][0][1], r[c][1][0], r[c][1][1]
            for i in range(x1, x2+1):
                for j in range(y1,y2+1):
                    if targetGrid[i][j] not in (0,c): return False
            return True
        def setrect(c):
            x1, y1, x2, y2 = r[c][0][0], r[c][0][1], r[c][1][0], r[c][1][1]
            for i in range(x1, x2+1):
                for j in range(y1,y2+1):
                    targetGrid[i][j]=0
        for i in range(m):
            for j in range(n):
                c = targetGrid[i][j]
                if c not in r: r[c] = [[i,j], [i,j]]
                else:
                    r[c][0][0], r[c][0][1] = min(i, r[c][0][0]), min(j, r[c][0][1])
                    r[c][1][0], r[c][1][1] = max(i, r[c][1][0]), max(j, r[c][1][1])
        while r:
            cc = []
            for c in r:
                if testrect(c): cc.append(c)
            for c in cc:
                setrect(c)
                del r[c]
            if not cc: return False            
        return True
