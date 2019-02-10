from library_for_lc import UnionFind
class Solution(object):
    def equationsPossible(self, eq):
        """
        :type equations: List[str]
        :rtype: bool
        """
        cc = 0
        uf = UnionFind()
        for a,o1,o2,b in eq:
            if o1 == '=':
                x = uf.find(a)
                y = uf.find(b)
                if x != y: uf.union(x,y)
        for a,o1,o2,b in eq:
            if o1 == '!':
                if uf.find(a) == uf.find(b): return False
        return True
        
print Solution().equationsPossible(["a==b","b!=a"])
print Solution().equationsPossible(["b==a","a==b"])
print Solution().equationsPossible(["a==b","b==c","a==c"])
print Solution().equationsPossible(["a==b","b!=c","c==a"])
print Solution().equationsPossible(["c==c","b==d","x!=z"])
print Solution().equationsPossible(["c==c","f!=a","f==b","b==c"])
