class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        n = len(A[0])
        d = 0
        for i in range(n):
            for j in range(1,len(A)):
                if A[j][i] < A[j-1][i]: 
                    d+=1
                    break
        return d
        

print Solution().minDeletionSize(["cba","daf","ghi"])
print Solution().minDeletionSize(["a","b"])
print Solution().minDeletionSize(["zyx","wvu","tsr"])
