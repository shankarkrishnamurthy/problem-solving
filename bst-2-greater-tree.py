# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    @staticmethod
    def printtn(root):
        print "[",
        q = [root]
        while True:
            nq = []
            for n in q:
                if not n:
                    print 'None,',
                    nq.append(None)
                    nq.append(None)
                    continue
                print n.val,",",
                nq.append(n.left)
                nq.append(n.right)
            while not nq[-1]:
                nq.pop()
                if not nq: break
            if not nq: break
            q = nq
        print "]"


class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def do_convbst(root,rsum):
            if not root: return 0
            print root.val, rsum
            r = do_convbst(root.right, rsum)
            l = do_convbst(root.left, r+root.val+rsum)
            cval = root.val
            root.val += r + rsum
            return r + l + cval
                
        do_convbst(root, 0)
        return root

t = TreeNode(5)
t.left = TreeNode(2)
t.left.left = TreeNode(1)
t.left.right = TreeNode(3)
t.right = TreeNode(13)
t.right.left = TreeNode(11)
t.right.right = TreeNode(15)
a=Solution().convertBST(t)
TreeNode.printtn(a)
