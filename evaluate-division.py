from library_for_lc import *
class Solution(object):
    def calcEquation(self, eq, values, q):
        """
        :type eq: List[List[str]]
        :type values: List[float]
        :type q: List[List[str]]
        :rtype: List[float]
        """
        def dfs(a,t,ans,v):
            #print a,t,ans
            v.add(a)
            if (a,t) in ht: return ht[(a,t)]*ans
            for i in h[a]:
                if i in v: continue
                cv = dfs(i,t,ans*ht[(a,i)],v)
                if cv!=-1: return cv
            return -1.0

        uf = UnionFind()
        ht = {} # ht[(a,b)]=3.0
        h = {} # h['a'] = [b,c,d]
        for i,v in enumerate(eq):
            ht[tuple(v)] = values[i]
            ht[tuple([v[1],v[0]])] = 1.0/values[i]
            a,b = uf.find(v[0]),uf.find(v[1])
            if a!=b: uf.union(v[0],v[1])
            h.setdefault(v[0],[]).append(v[1])
            h.setdefault(v[1],[]).append(v[0])

        res = []
        #print eq
        #print values
        #print q
        #print h
        #print ht
        for i in q:
            if i[0] not in h or i[1] not in h: res.append(-1.0)
            elif i[0] == i[1]: res.append(1.0)
            else:
                a,b = uf.find(i[0]),uf.find(i[1])
                if a!=b: res.append(-1.0)
                else: res.append(dfs(i[0],i[1], 1.0, set()))
        return res
            
        
print Solution().calcEquation([ ["a", "b"], ["b", "c"] ],[2.0, 3.0],[ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ])
print Solution().calcEquation([["a","b"]],[4.0],[["a", "b"],["b","a"], ["x", "x"] ])
print Solution().calcEquation([["a","b"],["b","c"],["c","d"],["e","d"]],[2.0,3.0,1.5,4.0],[["a", "e"]])
