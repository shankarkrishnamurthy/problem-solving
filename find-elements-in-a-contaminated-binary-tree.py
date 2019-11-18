from library_for_lc import *
class FindElements:
    def __init__(self, root: TreeNode):
        self.ele  = set()
        def dfs(r,v):
            if not r: return
            self.ele.add(v)
            dfs(r.left,2*v+1)
            dfs(r.right,2*v+2)
            return
        dfs(root,0)

    def find(self, target: int) -> bool:
        return target in self.ele
        
call(inp = ["FindElements","find","find"],arg=[[deser([-1,null,-1])],[1],[2]])
call(inp = ["FindElements","find","find","find"],arg= [[deser([-1,-1,-1,-1,-1])],[1],[3],[5]])
call(inp = ["FindElements","find","find","find","find"],arg = [[deser([-1,null,-1,-1,null,-1])],[2],[3],[4],[5]])
