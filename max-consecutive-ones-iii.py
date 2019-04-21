class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        lsf,zi,z = 0,-1,[]
        for i in range(len(A)):
            #print i, z
            if A[i] == 0:
                z.append(i)
                if len(z) <= K:
                    lsf = max(lsf, i+1)
                else:
                    zi +=1
                    lsf = max(lsf, i-(z[zi]+1)+1)
            else:
                if len(z) <= K:
                    lsf = max(lsf, i+1)
                else:
                    lsf = max(lsf, i-(z[zi]+1)+1)

        return lsf
                
        
#print Solution().longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2)
#print Solution().longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3)
#print Solution().longestOnes([0], 1)
#print Solution().longestOnes([1,0], 1)
#print Solution().longestOnes([1], 1)
#print Solution().longestOnes([1,1], 1)
#print Solution().longestOnes([0,0,0], 2)
#print Solution().longestOnes([0], 0)
print Solution().longestOnes([1], 0)

