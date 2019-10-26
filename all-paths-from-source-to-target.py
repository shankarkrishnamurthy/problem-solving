from typing import *
class Solution():
    def __init__(self):
        self.ans = []
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(i,v,anc):
            if i == len(graph)-1:
                self.ans.append(anc+[i])
                return
            v.add(i)
            for dst in graph[i]:
                if dst not in v:
                    dfs(dst,v,anc+[i])
            v.remove(i)
            return

        dfs(0,set(),[])
        return self.ans

print(Solution().allPathsSourceTarget([[1,2], [3], [1], []]))
print(Solution().allPathsSourceTarget([[1,2], [3], [3], []]))
print(Solution().allPathsSourceTarget([[1], []]))
