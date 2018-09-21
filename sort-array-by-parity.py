class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        even, odd = [] , []
        for i in A:
            if i % 2 == 0: 
                even.append(i)
            else:
                odd.append(i)
        return even + odd

print Solution().sortArrayByParity([3,1,2,4])
print Solution().sortArrayByParity([2,4,3,1])
print Solution().sortArrayByParity([2])
print Solution().sortArrayByParity([3])
