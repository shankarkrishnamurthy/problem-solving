class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odd = 1 
        even = 0
        l = len(A)
        while odd < l and even < l:
            while odd < l and A[odd]%2==1:
                odd += 2
                continue
            while even < l and  A[even]%2 == 0:
                even +=2
                continue
            if odd < l and even < l:
                tmp = A[odd]
                A[odd] = A[even]
                A[even] = tmp
        return A
            
print Solution().sortArrayByParityII([4,2,5,7])
print Solution().sortArrayByParityII([3,4])
