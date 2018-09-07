class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        flag=0 # None = not decided, 1 = Incr, 2 = Decr
        for i in range(1,len(A)):
            #print A[i-1], A[i], flag
            if A[i] == A[i-1]:
                continue
            elif A[i-1] < A[i]:
                if flag == 0:
                    flag = 1
                    continue
                if flag != 1: return False
            elif A[i] < A[i-1]:
                if flag == 0:
                    flag = 2
                    continue
                if flag != 2: return False
            else:
                print 'Cannot Come here'
        return True
        

print Solution().isMonotonic([1,2,2,3])
print Solution().isMonotonic([6,5,4,4])
print Solution().isMonotonic([1,3,2])
print Solution().isMonotonic([1,2,4,5])
print Solution().isMonotonic([1,1,1])
