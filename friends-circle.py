class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        m = len(M)
        n = len(M[0])
        res = []
        for i in range(m):
            for j in range(i,n):
                if M[i][j] == 0: continue
                found,one,two = False,set(),set()
                for f in res:
                    if i in f or j in f: found = True
                    if i in f: one = f
                    if j in f: two = f
                if not found: 
                    res.append(set([i,j]))
                else:
                    tog = one.union(two,set([i,j]))
                    if two in res: res.remove(two)
                    if one in res: res.remove(one)
                    res.append(tog)
        return len(res)

print Solution().findCircleNum([[1,1,0], [1,1,1], [0,1,1]])
print Solution().findCircleNum([[1,1,0], [1,1,0], [0,0,1]])
