class Solution(object):
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        B = A + A
        n = len(A)
        msf = -300001
        meh = 0
        idx = 0
        if len(set(A)) == 1: 
            if A[0] <= 0: return A[0]
            else: return sum(A)
        for i in range(len(B)):
            #print i,idx, 'B[i]',B[i],'meh', meh, 'msf', msf
            if i-idx +1 > n:
                tmeh,tidx = 0,idx+1
                for j in range(idx+1,i+1):
                    tmeh += B[j]
                    if tmeh < 0:
                        tidx = j
                        tmeh = 0
                meh = tmeh
                idx = tidx
            else:
                meh = meh + B[i] 
            if (msf < meh): msf = meh 
  
            if meh < 0: 
                meh = 0   
                idx = i
        return msf 

print Solution().maxSubarraySumCircular([1,-2,3,-2]) # 3
print Solution().maxSubarraySumCircular([5,-3,5]) # 10
print Solution().maxSubarraySumCircular([3,-1,2,-1]) # 4
print Solution().maxSubarraySumCircular([3,-2,2,-3]) # 3
print Solution().maxSubarraySumCircular([-2,-3,-1]) # -1

