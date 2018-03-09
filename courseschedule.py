class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        def do_dfs(i,backedge):
            if not adjlist.has_key(i) or i in gvisit: 
                return False
            backedge.add(i)
            gvisit.add(i)
            for j in adjlist[i]:
                if j in backedge or do_dfs(j,backedge):
                    return True
            backedge.remove(i)
            return False
        adjlist=dict()
        for v in prerequisites:
            if adjlist.has_key(v[1]):
                adjlist[v[1]] += [v[0]]
            else:
                adjlist[v[1]] = [v[0]]
        #print adjlist,
        gvisit=set()
        for i in range(0,numCourses):
            loop = do_dfs(i,set())
            if loop: return False
        return True

print Solution().canFinish(2,[[0,1],[1,0]])
print Solution().canFinish(2,[[1,0]])
print Solution().canFinish(3,[[1,0],[2,1]])
print Solution().canFinish(6,[[0,5],[0,4],[1,4],[2,5],[3,2],[1,3]])
print Solution().canFinish(6,[[0,5],[0,4],[1,4],[2,5],[3,2],[1,3],[5,1]])
print Solution().canFinish(4,[[1,0],[2,0],[3,1],[3,2]])
