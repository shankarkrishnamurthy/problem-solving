class Solution(object):
    def subarrayBitwiseORs(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        cum , s= [], 0
        for i in A:
            cum.append(i | s)
            s = cum[-1]

        ans = set()
        for j in range(len(A)-1, -1,-1):
            s,l = 0,j
            while l >=0:
                s = s | A[l]
                ans.add(s)
                l -= 1
                if l >= 0 and s == (cum[l] | s): break

        #print ans
        return len(ans)

print Solution().subarrayBitwiseORs([1,2,4])
print Solution().subarrayBitwiseORs([1,1,2])
print Solution().subarrayBitwiseORs([0])
            
