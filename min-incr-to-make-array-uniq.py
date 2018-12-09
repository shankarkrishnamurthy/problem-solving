class Solution(object):
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 2: return 0
        A.sort()
        fs = mi = A[0]
        for v in A:
            if v in hsf:
                fs = free_slot(max(fs,v))
                res += fs - 
            else:
                hsf.add(v)

        return res
        

print Solution().minIncrementForUnique([1,2,2])
print Solution().minIncrementForUnique([3,2,1,2,1,7])
