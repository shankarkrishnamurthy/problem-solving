class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(A)
        n = len(A[0])
        return [[A[j][i] for j in range(m)] for i in range(n)]
        
        

print Solution().transpose([[1,2,3],[4,5,6],[7,8,9]])
print Solution().transpose([[1,2,3],[4,5,6]])
