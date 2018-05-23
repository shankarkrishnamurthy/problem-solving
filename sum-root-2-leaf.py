# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def do_sn(n, anc):
            if not n: return
            anc.append(str(n.val))
            if n.left: do_sn(n.left, anc)
            if n.right: do_sn(n.right, anc)
            if not n.left and not n.right: res.append(''.join(anc))
            anc.pop(-1)
            
        res=[]
        do_sn(root,[])
        return sum([int(x) for x in res])
        
print Solution().sumNumbers(None)
t1 = TreeNode(1)
t1.left = TreeNode(2)
t1.right = TreeNode(3)
print Solution().sumNumbers(t1)
t1 = TreeNode(4)
t1.left = TreeNode(9)
t1.left.left = TreeNode(5)
t1.left.right = TreeNode(1)
t1.right = TreeNode(0)
print Solution().sumNumbers(t1)
