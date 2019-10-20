# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from library_for_lc import *
class Solution(object):
    def __init__(self):
        self.h = {}
        self.m = 0
        self.ans = []

    def lcaDeepestLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def filt(ll):
            if not self.ans:
                self.ans = ll
                return
            i = 0
            while i < len(self.ans):
                if self.ans[i] != ll[i]: break
                i += 1
            if i != len(self.ans):
                self.ans = self.ans[:i]

        def dfs(r,h):
            if not r: return
            self.h.setdefault(h,[]).append(r)
            self.m = max(self.m,h)
            dfs(r.left,h+1)
            dfs(r.right,h+1)
            return

        def dfs2(r,anc):
            if not r: return 
            dfs2(r.left,anc+[r])
            dfs2(r.right,anc+[r])
            if r in ns: filt(anc)
            return
            
        dfs(root,0)
        ns = set(self.h[self.m])
        if len(ns) == 1: return ns.pop()
        dfs2(root,[])
        return self.ans[-1]
        
        
t = Solution().lcaDeepestLeaves(deser([1]))
print ser(t)
t = Solution().lcaDeepestLeaves(deser([1,2]))
print ser(t)
t = Solution().lcaDeepestLeaves(deser([1,2,3]))
print ser(t)
t = Solution().lcaDeepestLeaves(deser([1,2,3,4]))
print ser(t)
t = Solution().lcaDeepestLeaves(deser([1,2,3,4,5]))
print ser(t)
t = Solution().lcaDeepestLeaves(deser([1,2,3,4,null,null,5]))
print ser(t)
