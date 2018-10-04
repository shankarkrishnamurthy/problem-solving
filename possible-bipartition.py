class Solution(object):
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        g = dict()
        for i in dislikes:
            g.setdefault(i[0], []).append(i[1])
            g.setdefault(i[1], []).append(i[0])
        gh = dict()
        for ea in g:
            if ea in gh: continue
            q = set([ea])
            cgrp = True
            while True:
                tmp = set()
                cgrp = not cgrp
                for p in q:
                    if p not in gh: gh.setdefault(p, cgrp)
                    elif gh[p] == cgrp: continue
                    else: return False
    
                    for dp in g[p]: tmp.add(dp)
                if not tmp: break
                q = tmp
        return True
                
        
print Solution().possibleBipartition(4, [[1,2],[1,3],[2,4]]) # Output: true
print Solution().possibleBipartition(3, [[1,2],[1,3],[2,3]]) # Output: false
print  Solution().possibleBipartition(5, [[1,2],[2,3],[3,4],[4,5],[1,5]]) # Output: false
