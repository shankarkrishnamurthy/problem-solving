class Solution(object):
    def sumOfDistancesInTree(self, N, edges):
        """
        :type N: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        def create_adjlist():
            for e in edges:
                if e[0] in g: g[e[0]].add(e[1])
                else: g[e[0]] = set([e[1]])
                if e[1] in g: g[e[1]].add(e[0])
                else: g[e[1]] = set([e[0]])
        def do_dfs(n, visit):
            visit.add(n)
            c[n] = [0,0]
            for k in g[n] - visit: 
                [a,b] = do_dfs(k,visit)
                c[n][0] += a+1
                c[n][1] += a+b+1
            return c[n]
        def do_dfs2(n,p,visit): # currentNode, ParentNode, VisitedSet
            visit.add(n)
            if p != n:
                psn = N-1-c[n][0]
                psd = c[p][1]-(c[n][1] + c[n][0] + 1)+psn
                res[n] = psd + c[n][1]
                c[n] = [N-1, res[n]]
            else:
                res[p] = c[p][1]
            for k in g[n] - visit: 
                do_dfs2(k,n,visit)
            return
        if N < 2: return [0]
        g = {}
        create_adjlist()
        c = {}        
        do_dfs(0,set()) # for each node, count subtree nodes and their distances
        res = [0]*N
        do_dfs2(0,0,set()) # for total distance to all nodes
        return res

print Solution().sumOfDistancesInTree(2, [[0,1]])
print Solution().sumOfDistancesInTree(6, [[0,1],[0,2],[2,3],[2,4],[2,5]])
print Solution().sumOfDistancesInTree(6, [[0,3],[0,2],[3,4],[2,1],[2,5]])
print Solution().sumOfDistancesInTree(7, [[0,3],[0,2],[3,4],[2,1],[2,5],[1,6]])
