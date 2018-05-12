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
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def do_prune(root):
            if not root: return 0

            l = do_prune(root.left)
            r = do_prune(root.right)
            if not l: root.left = None
            if not r: root.right = None

            return root.val + l + r
        ones = do_prune(root)
        if not ones: return None
        return root

t1 = TreeNode(1)
t1.left = TreeNode(1)
t1.left.left = TreeNode(0)
t1.right = TreeNode(0)
TreeNode.printtn(t1)
t = Solution().pruneTree(t1)
TreeNode.printtn(t)
t1 = TreeNode(0)
t1.left = TreeNode(0)
t1.right = TreeNode(0)
TreeNode.printtn(t1)
t = Solution().pruneTree(t1)
TreeNode.printtn(t)
