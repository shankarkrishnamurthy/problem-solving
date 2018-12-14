class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        n,D = len(A[0]),set()
        idx,d = list(range(len(A))),0
        for i in range(n):
            #print i, idx
            sidx,deld = set(),False
            for v in range(1,len(idx)):
                j = idx[v]
                yj = idx[v-1]
                if A[j][i] < A[yj][i]:
                    V = set(range(i+1)) - D
                    val1 = val2 = ''
                    for k in sorted(V):
                        val1 += A[j][k]
                        val2 += A[yj][k]
                    if val1 >= val2: continue
                    d+=1
                    D.add(i)
                    deld = True
                    break
                elif A[j][i] == A[yj][i]:
                    sidx.add(yj)
                    sidx.add(j)
            if not deld:
                if not sidx: return d
                else: idx = sorted(list(sidx))
        return d

        
print Solution().minDeletionSize(["ca","bb","ac"])
print Solution().minDeletionSize(["xc","yb","za"])
print Solution().minDeletionSize(["zyx","wvu","tsr"])
print Solution().minDeletionSize(["abc","bcd","bce", "bca"])
print Solution().minDeletionSize(["abx","agz","bgc","bfc"])
print Solution().minDeletionSize(["doeeqiy","yabhbqe","twckqte"])
