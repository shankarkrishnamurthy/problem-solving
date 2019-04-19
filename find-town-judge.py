class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        hby = {}
        trusts = set()
        if N == 1 and len(trust)==0: return N
        for a,b in trust:
            trusts.add(a)
            hby[b] = hby.get(b,0) + 1
        for i in range(1,N+1):
            if i in trusts or i not in hby: continue
            if hby[i] == N-1: return i
        return -1

print Solution().findJudge(1, [])
print Solution().findJudge(2, [[1,2]])
print Solution().findJudge(3, [[1,3],[2,3]])
print Solution().findJudge(4, [[1,3],[2,3],[3,1]])
print Solution().findJudge(3, [[1,2],[2,3]])
print Solution().findJudge(4, [[1,3],[1,4],[2,3],[2,4],[4,3]])

