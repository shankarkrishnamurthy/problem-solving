class Solution(object):
    def maxWidthRamp(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        md = 0
        lm = [0]
        rm = [n-1]
        for i in range(1, n): 
            if A[i] < A[lm[-1]]: 
                lm.append(i)
        for j in range(n - 2, -1, -1): 
            if A[j] > A[rm[-1]]: 
                rm.append(j)
  
        #rm = rm[::-1]
        #print A
        #print lm, rm
        i, j = 0, 0
        md = 0
        while (j < len(rm) and i < len(lm)): 
            if (A[lm[i]] <= A[rm[j]]): 
                print lm[i],rm[j]
                if md < rm[j]-lm[i]:
                    md = rm[j] - lm[i]
                j = j + 1
            else: i = i+1
    
        return md 

print Solution().maxWidthRamp([9,8,1,0,1,9,4,0,4,1])
print Solution().maxWidthRamp([6,0,8,2,1,5])
