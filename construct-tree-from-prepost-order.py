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
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        if not pre: return None
        if len(pre) == 1: return TreeNode(pre[0])
        
        assert(pre[0] == post[len(post)-1])
        root = TreeNode(pre[0])
        for i in range(len(post)-1):
            if post[i] == pre[1]: break

        n = i+1

        root.left = self.constructFromPrePost(pre[1:n+1], post[:n])
        root.right = self.constructFromPrePost(pre[n+1:], post[n:len(post)-1])

        return root

if __name__ == "__main__":
    s = Solution().constructFromPrePost([1,2,4,5,3,6,7], [4,5,2,6,7,3,1])
    TreeNode.printtn(s)
    s = Solution().constructFromPrePost([1,2,3,4,5], [2,4,5,3,1])
    TreeNode.printtn(s)
    s = Solution().constructFromPrePost([1,2,3], [3,2,1])
    TreeNode.printtn(s)
    s = Solution().constructFromPrePost([1,2,3], [2,3,1])
    TreeNode.printtn(s)
    
