# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        ha = {}
        for i in range(26): ha[i] = chr(ord('a') + i)
        res = []
        def dfs(r, anc):
            if not r: return
            if not r.left and not r.right: # leaf
                #print "ances ", anc
                res.append(''.join(anc + [ha[r.val]])[::-1])
                return
            anc.append(ha[r.val])
            dfs(r.left,anc)
            dfs(r.right,anc)
            anc.pop()
            return
        dfs(root,[])
        return min(res)

def deser(tl):
    p,c = 0,1
    if not tl: return None
    tl[p] = TreeNode(tl[p])
    while p < len(tl):
        if tl[p] == None: 
            p+=1
            continue
        if c >= len(tl): 
            p+=1
            continue
        if tl[c] != None: tl[c] = TreeNode(tl[c])
        tl[p].left = tl[c]
        c+=1
        if c >= len(tl): 
            p+=1
            continue
        if tl[c] != None: tl[c] = TreeNode(tl[c])
        tl[p].right = tl[c]
        c+=1
        p+=1
    return tl[0]

null = None
t = deser([25,1,3,1,3,0,2])
print Solution().smallestFromLeaf(t)
t = deser([0,1,2,3,4,3,4])
print Solution().smallestFromLeaf(t)
t = deser([2,2,1,null,1,0,null,0])
print Solution().smallestFromLeaf(t)
t = deser([2])
print Solution().smallestFromLeaf(t)


