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
    
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def build(pre, s, inord):
            if not inord:
                return None
            root = TreeNode(pre[s])
            rootidx = inord.index(root.val)
            root.left = build(pre, s+1, inord[:rootidx])
            root.right = build(pre, s+rootidx+1, inord[rootidx+1:])
            return root
            
        return build(preorder, 0, inorder)

t=Solution().buildTree([1,2,3],[2,1,3])
TreeNode.printtn(t)
t=Solution().buildTree([3,9,20,15,7], [9,3,15,20,7])
TreeNode.printtn(t)
t=Solution().buildTree([], [])
TreeNode.printtn(t)
