# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """

        def find_distance(root, d):
            q, cnt = {root}, d
            while(True):
                if cnt == 0: return list(q)
                tmp = set()
                for n in q:
                    if n.left: tmp.add(n.left)
                    if n.right: tmp.add(n.right)
                if not tmp: return []
                q = tmp
                cnt -= 1

        def find_anc(root, target, anc):
            if not root: return None
            anc.append(root)
            if root == target: return anc
            l = find_anc(root.left, target, anc)
            r = find_anc(root.right, target, anc)
            if l or r : return anc
            anc.pop(-1)

        res = []
        al =  find_anc(root,target,[])
        al = al[::-1]
        for i,v in enumerate(al):
            print "ancestor " ,v.val, K-i , i
            if K-i <0: break
            node, d = v, K-i
            if i and d > 0:
                chi = al[i-1]
                if chi == v.left: node = v.right
                else: node = v.left
                d -= 1
                
            if d >= 0 and node:
                #print "find dist", node.val, d
                c = find_distance(node, d)
                for m in c: res.append(m.val)
                
        #print res
        return res
        
"""
t = TreeNode(3)
t.left = TreeNode(5)
t.right = TreeNode(1)
t.right.left = TreeNode(0)
t.right.right = TreeNode(8)
t.left.left = TreeNode(6)
t.left.right = TreeNode(2)
t.left.right.left = TreeNode(7)
t.left.right.right = TreeNode(4)
"""
t = TreeNode(0)
t.right = TreeNode(1)
t.right.right = TreeNode(2)
t.right.right.right = TreeNode(3)
l = Solution().distanceK(t,t.right,2)
print l
#for i in l: print ' - ',i.val
