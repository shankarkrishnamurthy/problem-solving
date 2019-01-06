# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flipMatchVoyage(self, root, voyage):
        """
        :type root: TreeNode
        :type voyage: List[int]
        :rtype: List[int]
        """
        def dfs(r, i, j):
            if not r and j==i: return True
            if not r or j==i: return False
            if r.val != voyage[i]: return False
            li = ri = None
            if r.left: 
                li = vh[r.left.val]
                if not (i <= li < j): return False
            if r.right: 
                ri = vh[r.right.val]
                if not (i<= ri <j): return False
            #print r.val, 'i', i, 'j', j, 'li', li, 'ri', ri

            if li and ri:
                if ri < li:
                    res.append(r.val)
                    return dfs(r.left, li, j) and dfs(r.right,ri,li)
                else:
                    return dfs(r.left,li,ri) and dfs(r.right,ri,j)
            else:
                if li or ri: return dfs(r.left or r.right,li or ri, j)

            return True

        vh = {v:k for k,v in enumerate(voyage)}
        res = []
        rc = dfs(root,0,len(voyage))
        if not rc: return [-1]
        return res

t1 = TreeNode(4)
t1.left = TreeNode(9)
t1.right = TreeNode(0)
print Solution().flipMatchVoyage(t1, [4,9,0])
print Solution().flipMatchVoyage(t1, [4,0,9])
print Solution().flipMatchVoyage(t1, [9,4])

