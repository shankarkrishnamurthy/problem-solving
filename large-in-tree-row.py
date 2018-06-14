# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        hgt,visit={},set()
        def do_lv(n,h):
            if not n: return
            hgt[h] = max(n.val, hgt.get(h, n.val))
            do_lv(n.left, h+1)
            do_lv(n.right, h+1)
            
        do_lv(root,0)
        return [hgt[k] for k in sorted(hgt.keys())]
        
#t1 = TreeNode(1)
t1 = None
#t1.left = TreeNode(3)
#t1.right = TreeNode(2)
#t1.left.left = TreeNode(5)
#t1.left.right = TreeNode(3)
#t1.right.right = TreeNode(9)
print Solution().largestValues(t1)
