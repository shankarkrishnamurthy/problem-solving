# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        hgt,visit = {},set()
        def do_dfs(n,h):
            global mh
            visit.add(n.val)
            if h not in hgt:
                mh = h
                hgt[mh] = n.val
            if n.left and n.left not in visit: do_dfs(n.left, h+1)
            if n.right and n.right not in visit: do_dfs(n.right, h+1)
        global mh
        mh = 5
        do_dfs(root,0)
        return hgt[mh]
        
t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(3)
print Solution().findBottomLeftValue(t)

t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(3)
t.left.left = TreeNode(4)
t.right.left = TreeNode(5)
t.right.right = TreeNode(6)
t.right.left.left = TreeNode(7)
print Solution().findBottomLeftValue(t)
