class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        G = [0 for _ in range(n+1)]
        G[0] = 1
        G[1] = 1
        for i in range(2, n+1):
            for j in range(0,i//2):
                G[i] += G[j]*G[i-j-1]
            G[i] *= 2
            if i % 2 == 1: G[i] += G[i//2]*G[i//2]
        return G[n]
            
print Solution().numTrees(5)
print Solution().numTrees(1)
