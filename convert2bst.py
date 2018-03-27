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
    def __init__(self):
        self.root = None
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        def construct(l, r):
            root = None
            if l < r:
                mid = (l + r)//2
                root = TreeNode(nums[mid])
                root.left = construct(l, mid)
                root.right = construct(mid+1, r)
            return root
             
        return construct(0, len(nums))
        
t = Solution().sortedArrayToBST([-3,0,5])
TreeNode.printtn(t)
