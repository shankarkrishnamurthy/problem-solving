class Solution(object):
    def numMovesStonesII(self, A):
        """
        :type s: List[int]
        :rtype: List[int]
        """
        def maval():
            mav = A[-1] - A[0] -n + 1 # number of empty slots in 'n'
            lv = A[1]-A[0] - 1
            rv = A[-1] - A[-2] - 1
            if lv > rv: return mav - rv
            else: return mav-lv
        
        def mival():
            msf,j = 0,0
            for i in xrange(1,len(A)):
                while j < i:
                    cw = A[i]-A[j]+1
                    if cw > n: j +=1
                    else: break
                msf = max(msf, i-j+1)
            miv = n - msf # empty slots in the moving window which has max stones
            if miv == 1:
              if (A[-2]-A[0]+1==n-1 and A[-1]-A[-2]-1 > 1) or (A[1]-A[0]-1 > 1 and A[-1]-A[1]+1==n-1): miv = 2
            return miv
        A.sort()
        print A
        n = len(A)
        return [mival(),maval()]

print Solution().numMovesStonesII([8,7,6,5,10])
#print Solution().numMovesStonesII([7,4,9])
#print Solution().numMovesStonesII([6,5,4,3,10])
#print Solution().numMovesStonesII([100,101,104,102,103])
#print Solution().numMovesStonesII([2,5,10,15])
