class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(A)
        if not m: return A
        n = len(A[0])
        if not n: return A
        for i in range(m):
            tmp = [1-x for x in A[i][::-1]]
            A[i] = tmp
        return A

print Solution().flipAndInvertImage([[1]])
print Solution().flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]])
print Solution().flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]])
