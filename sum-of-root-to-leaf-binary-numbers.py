# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.resal = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumRootToLeaf(self, r):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        def dfs(r,v):
            if not r: return
            if not r.left and not r.right:
                self.res += v <<1 | r.val
                return
            dfs(r.left,v << 1 | r.val)
            dfs(r.right,v << 1 | r.val)
            return

        dfs(r,0)
        return self.res
        
from library_for_lc import  *
t = deser( [1,0,1,0,1,0,1]) 
print Solution().sumRootToLeaf(t)
