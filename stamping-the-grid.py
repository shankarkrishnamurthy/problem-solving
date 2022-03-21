# Difference array 2D
class Solution:
    def possibleToStamp(self, gr, sh, sw):
        m, n = len(gr), len(gr[0])
        pre, pre2 = [[0]*n for i in range(m)], [[0]*n for i in range(m)]
        def isoccu(i,j):
            x,y = i+sh-1, j+sw-1
            if x-sh < 0 and y-sw < 0: return pre[x][y]  > 0
            elif x-sh < 0: return pre[x][y] - pre[x][y-sw] > 0
            elif y-sw < 0: return pre[x][y] - pre[x-sh][y] > 0
            else: return pre[x][y] - pre[x-sh][y] - pre[x][y-sw] + pre[x-sh][y-sw] > 0
        def update(i,j):
            x,y = i+sh,j+sw
            pre2[i][j] += 1
            if x < m: pre2[x][j] -= 1 
            if y < n: pre2[i][y] -= 1
            if x <m and y < n: pre2[x][y] += 1    
        def check():
            for i in range(m):
                for j in range(n):
                    if i > 0: pre2[i][j] += pre2[i-1][j]
                    if j > 0: pre2[i][j] += pre2[i][j-1]
                    if i > 0 and j > 0: pre2[i][j] -= pre2[i-1][j-1]
                    if pre2[i][j] == 0 and gr[i][j] != 1: return False
            return True
        for i in range(m):
            for j in range(n):
                if i ==0 and j ==0: pre[0][0] = gr[0][0]
                elif i == 0: pre[0][j] = gr[0][j] + pre[0][j-1]
                elif j == 0: pre[i][0] = gr[i][0] + pre[i-1][0]
                else: pre[i][j] = gr[i][j] + pre[i-1][j] + pre[i][j-1] - pre[i-1][j-1]
                    
        for i in range(m-sh+1):
            for j in range(n-sw+1):
                if isoccu(i,j): continue
                update(i,j)
        return check()
        
