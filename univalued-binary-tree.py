# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isUnivalTree(self, r):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def dfs(ro):
            if not ro:
                return True
            if uv != ro.val: return False

            if not dfs(ro.left): return False
            if not dfs(ro.right): return False

            return True

        uv = r.val

        return dfs(r)
        
t = TreeNode(1)
t.left = TreeNode(1)
t.right = TreeNode(1)
t.right.left = TreeNode(1)

print Solution().isUnivalTree(t)

t = TreeNode(2)
t.left = TreeNode(2)
t.right = TreeNode(2)
t.right.left = TreeNode(2)
t.left.left = TreeNode(5)

print Solution().isUnivalTree(t)
