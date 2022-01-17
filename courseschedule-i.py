class Solution(object):
    def canFinish(self, n, prereq):
        gout = {i : [] for i in range(n)}
        indeg=[0]*n
        for i,j in prereq:
            gout[j].append(i)
            indeg[i] += 1
        q,res = [i for i in range(n) if indeg[i] == 0],[]
        print(gout, q, indeg)
        while q:
            tmp = []
            for i in q:
                for k in gout[i]:
                    indeg[k] -= 1
                    if indeg[k]==0: tmp.append(k)
            res += q
            q = tmp
        return len(res) == n

print(Solution().canFinish(2,[[0,1],[1,0]]))
print(Solution().canFinish(2,[[1,0]]))
print(Solution().canFinish(3,[[1,0],[2,1]]))
print(Solution().canFinish(6,[[0,5],[0,4],[1,4],[2,5],[3,2],[1,3]]))
print(Solution().canFinish(6,[[0,5],[0,4],[1,4],[2,5],[3,2],[1,3],[5,1]]))
print(Solution().canFinish(4,[[1,0],[2,0],[3,1],[3,2]]))
