class Solution:
    def getCollisionTimes(self, cars):
        n = len(cars)
        res, st, p = [-1]*n, [], [-1]*n
        for i in range(n-1,-1,-1):
            while st and cars[st[-1]][1] >= cars[i][1]: st.pop()
            if not st: st.append(i)
            else:
                j = st[-1]
                st.append(i)
                while res[j] != -1 and (cars[j][0] - cars[i][0])/(cars[i][1] - cars[j][1]) > res[j]: j = p[j]
                res[i], p[i] = (cars[j][0] - cars[i][0])/(cars[i][1] - cars[j][1]), j
            #print('i', cars[i], 'parent', p, 'monostack', st, 'res', res[i])
            res[i] = round(res[i], 5)
        return res
