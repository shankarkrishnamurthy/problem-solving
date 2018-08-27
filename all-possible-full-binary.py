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
        self.nfst = {}
        self.fst = {}

    def one(self): return TreeNode(0)

    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        if N%2==0: return []
        if N==1: return [self.one()]
        if N in self.fst: return self.fst[N]
        val = []
        for i in range(1,N-1,2):
            v1 = self.allPossibleFBT(i)
            v2 = self.allPossibleFBT(N-1-i)
            #print 'N:',N, i,N-1-i,len(v1) ,'*',len(v2), v1, v2
            for k in v1:
                for l in v2:
                    r = TreeNode(0)
                    r.left = k
                    r.right = l
                    val.append(r)
        self.fst[N] = val
        #print ' N= ',N, ' Done'
        return val

    def nOfAllPossibleFBT(self,N):
        if N%2==0: return None
        if N==1: return 1
        if N in self.nfst: return self.nfst[N]
        val = 0
        for i in range(1,N-1,2):
            val += self.nOfAllPossibleFBT(i) * self.nOfAllPossibleFBT(N-1-i)
        self.nfst[N] = val
        return val
        
#for v in Solution().allPossibleFBT(3): TreeNode.printtn(v)
#for v in Solution().allPossibleFBT(5): TreeNode.printtn(v)
#for v in Solution().allPossibleFBT(7): TreeNode.printtn(v)
#for v in Solution().allPossibleFBT(11): TreeNode.printtn(v)
for v in Solution().allPossibleFBT(19): TreeNode.printtn(v)

#print Solution().nOfAllPossibleFBT(3)
#print Solution().nOfAllPossibleFBT(5)
#print Solution().nOfAllPossibleFBT(7)
#print Solution().nOfAllPossibleFBT(19)
#print Solution().nOfAllPossibleFBT(11)
        
