# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        ha = {}
        for i in range(26): ha[i] = chr(ord('a') + i)
        res = []
        def dfs(r, anc):
            if not r: return
            if not r.left and not r.right: # leaf
                #print "ances ", anc
                res.append(''.join(anc + [ha[r.val]])[::-1])
                return
            anc.append(ha[r.val])
            dfs(r.left,anc)
            dfs(r.right,anc)
            anc.pop()
            return
        dfs(root,[])
        return min(res)

t = TreeNode(25)
t.left = TreeNode(1)
t.right = TreeNode(3)
t.left.left = TreeNode(1)
t.left.right = TreeNode(3)
t.right.left = TreeNode(0)
t.right.right = TreeNode(2)
print Solution().smallestFromLeaf(t)
t = TreeNode(0)
t.left = TreeNode(1)
t.right = TreeNode(2)
t.left.left = TreeNode(3)
t.left.right = TreeNode(4)
t.right.left = TreeNode(3)
t.right.right = TreeNode(4)
print Solution().smallestFromLeaf(t)
t = TreeNode(2)
t.left = TreeNode(2)
t.right = TreeNode(1)
t.left.right = TreeNode(1)
t.left.right.left = TreeNode(0)
t.right.left = TreeNode(0)
print Solution().smallestFromLeaf(t)
t = TreeNode(2)
print Solution().smallestFromLeaf(t)
