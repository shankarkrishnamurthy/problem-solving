class Solution(object):
    def numIslands(self, gr):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(i,j):
            visit.add((i,j))
            #print i,j
            for (n,m) in [(i+1,j),(i,j+1),(i,j-1),(i-1,j)]:
                if 0<=n<s and 0<=m<s and (n,m) not in visit: 
                    if gr[n][m] == '0': dfs(n,m)
            n,m = i+1,j+1
            if 0<=n<s and 0<=m<s and not (gr[i+1][j] == '2' and gr[i][j+1] == '2'):
                if (n,m) not in visit and gr[n][m] == '0' : dfs(n,m)
            n,m = i-1,j-1
            if 0<=i-1<s and 0<=j-1<s and not (gr[i][j-1] == '2' and gr[i-1][j] == '2'):
                if (n,m) not in visit and gr[n][m] == '0' : dfs(n,m)
            n,m = i+1,j-1
            if 0<=i+1<s and 0<=j-1<s and not (gr[i+1][j] == '1' and gr[i][j-1] == '1'):
                if (n,m) not in visit and gr[n][m] == '0' : dfs(n,m)
            n,m = i-1,j+1
            if 0<=i-1<s and 0<=j+1<s and not (gr[i-1][j] == '1' and gr[i][j+1] == '1'):
                if (n,m) not in visit and gr[n][m] == '0' : dfs(n,m)
            
        visit,isl,s=set(),0,len(gr)
        for i in range(len(gr)):
            for j in range(len(gr[0])):
                if (i,j) not in visit and gr[i][j] == '0':
                    dfs(i,j)
                    isl += 1
        return isl

    def regionsBySlashes(self, g):
        """
        :type grid: List[str]
        :rtype: int
        """
        n = len(g)
        m = len(g[0])
        #print g,n,m
        l = ['10','01']
        r = ['02','20']
        e = ['00','00']
        gr = []
        for s in g:
            n,i = len(s),0
            r1,r2 = '',''
            while i<n:
                if s[i] == "\\":
                    r1 += l[0]
                    r2 += l[1]
                elif s[i] == '/':
                    r1 += r[0]
                    r2 += r[1]
                else:
                    r1 += e[0]
                    r2 += e[1]
                i += 1
            gr.append(r1)
            gr.append(r2)
        print gr,len(gr)
        return self.numIslands(gr)

print Solution().regionsBySlashes([ " /", "/ " ])
print Solution().regionsBySlashes([ " /", "  " ])
print Solution().regionsBySlashes([ "\\/", "/\\" ])
print Solution().regionsBySlashes([ "/\\", "\\/" ])
print Solution().regionsBySlashes([ "//", "/ " ])
