class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSumAnc(self, root, sum, anc,res):
        if not root:
            return []
        if root.left==None and root.right==None and root.val == sum:
            res.append(list(anc + [root.val]))
        anc.append(root.val)
        l = self.pathSumAnc(root.left, sum-root.val, anc,res)
        r = self.pathSumAnc(root.right, sum-root.val,anc,res)
        anc.pop()

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        self.pathSumAnc(root,sum,[], res)
        return res

t1 = TreeNode(5)
t1.left = TreeNode(4)
t1.left.left = TreeNode(11)
t1.left.left.left = TreeNode(7)
t1.left.left.right = TreeNode(2)
t1.right = TreeNode(8)
t1.right.left = TreeNode(13)
t1.right.right = TreeNode(4)
t1.right.right.left = TreeNode(5)
t1.right.right.right = TreeNode(1)

print Solution().pathSum(t1, 22)        
