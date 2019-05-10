from library_for_lc import *
class Solution(object):
    #@timeit
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        A0,B0 =A[0],B[0]
        cnt = 2 if A0 != B0 else 1
        for i in range(1,len(A)):
            if A0 and A0!=A[i] and A0!=B[i]: 
                cnt -= 1
                if A0 == B0: return -1
                A0 = 0
            if B0 and B0!=A[i] and B0!=B[i]: 
                cnt -= 1
                B0 = 0
            if cnt == 0: return -1

        # we can optimize by merging these 2 operations into one loop
        print 'cnt ', cnt, 'lenA ', len(A)
        if cnt == 2:
            rot,k = 0, B0
            for l in A:
                if l != k: rot+=1
            return min(rot, len(A)-rot)
        else:
            up,down,k = 0,0, A0 if not B0 else B0
            for i,j in zip(A,B):
                if i != k: up+=1
                if j != k: down+=1
            return min(up,down)
            
#print Solution().minDominoRotations([2,1,2,4,2,2],[5,2,6,2,3,2])
#print Solution().minDominoRotations([3,5,1,2,3], [3,6,3,3,4])
#print Solution().minDominoRotations([3,2,3,2,4], [2,3,2,3,3])
#print Solution().minDominoRotations([2,1,1,3,2,1,2,2,1],[3,2,3,1,3,2,3,3,2])
#print Solution().minDominoRotations([2,1,1,1,2,2,2,1,1,2],[1,1,2,1,1,1,1,2,1,1])
print Solution().minDominoRotations([1,1,2,1,1,1,1,1,2,1,2,1,1,1,1,1,1,1,2,1,1,1,1,1,1,2,1,2,1,1,2,2,2,1,1,2,1,1,1,2,1,2,1,1,1,1,2,2,1,1,1,1,1,2,1,2,1,1,1,2,1,1,1,1,1,2,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,2,1,2,2,1,1,1,1,1,2,1,1,2,1,2,1,2,2,1,1,1,1,1,1,2,2,1,1,1,1,1,2,2,2,1,1,1,1,1,1,2,1,2,1,1,2,1,1,1,1,1,1,1,1,1,2,1,1,1,2,1,1,2,1,1,2,1,2,2,1,2,1,2,1,1,2,2,2,1,2,2,2,1,1,1,1,1,2,1,1,1,2,1,1,1,1,1,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,2,1,1,1,1,1,2,1,1,1,1,1,2,2,1,2,1,2,1,2,1,2,2,1,1,1,1,1,1,1,2,1,1,2,1,1,1,1,1,1,1,1,2,1,2,1,1,1,2,1,1,1,2,1,2,1,1,1,1,1,2,1,1,1,2,1,2,2,2,1,1,1,2,2,1,1,1,1,1,1,1,1,2,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,2,1,2,2,2,1,1,1,1,1,2,1,1,1,2,1,1,1,2,1,1,1,1,1,1,1,2,2,1,2,1,1,1,1,1,1,1,1,1,2,1,2,1,1,2,1,1,2,2,1,1,1,1,1,1,1,1,2,2,1,1,1,1,1,1,2,1,1,1,1,1,1,1,2,1,1,1,2,1,1,1,1,2,1,1,1,1,1,2,1,1,2,2,1,1,1,2,1,2,1,2,1,1,1,2,1,2,1,1,1,1,1,2,1,1,1,1,1,2,1,1,2,1,1,1,1,2,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,2,2,1,1,1,1,2,1,1,2,1,1,1,1,1,1,1,1,1,1,2,2,1,2,2,1,1,1,2,2,1,1,1,2,1,1,1,1,1,2,1,1,1,2,1,1,1,1,1,2,2,1,1,1,1,1,1,2,1,2,1,1,2,1,1,2,1,1,1,1,1,1,1,1,1,2,2,1,1,2,2,1,1,2,2,1,2,1,2,1,2,1,1,1,2,1,2,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,2,2,1,1,2,1,1,2,1,2,1,1,1,1,2,2,2,1,2,1,2,1,2,1,1,1,1,1,1,1,2,1,1,1,1,2,1,1,2,1,1,1,1,1,1,2,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,2,1,1,2,2,1,2,1,2,1,2,2,1,1,2,1,1,1,1,1,1,1,1,1,1,2,2,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,2,1,1,2,1,1,1,1,2,2,1,2,2,1,2,1,1,1,1,1,2,1,2,2,2,2,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,2,1,1,1,2,1,2,1,1,2,1,1,1,2,1,1,1,1,2,1,1,1,2,1,1,2,2,1,1,2,1,2,1,1,1,2,1,1,2,2,1,1,1,1,1,2,1,1,1,1,1,1,2,1,2,1,1,1,1,1,1,1,2,2,1,1,2,2,1,1,1,2,2,1,1,1,2,1,2,1,1,1,2,1,1,1,1,1,1,1,1,1,2,2,1,1,2,1,1,1,1,1,2,2,1,2,2,2,1,1,1,1,2,1,1,1,1,2,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,2,2,1,2,1,1,1,1,2,2,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,2,1,1,2,1,1,2,1,1,1,2,1,2,1,1,1,1,2,1,1,1,2,2,1,1,1,1,1,2,1,2,1,1,2,1,2,2,1,2,2,1,2,2,1,1,2,2,1,1,2,1,2,1,1,1,1,1,1,1,1,1,1,2,2,1,2,2,1,1,2,1,1,1,1,2,2,1,1,1,2,1,1,1,1,1,2,1,1,1,2,1,2,2,1,1,2,1,2,2,1,2,1,1,2,2,1,1,1,1,1,1,1,1,1,2,1,2,1,1,1,1,1,1,1,1,2,1,1,2,1,1,1,1,1,2,1,2,1,1,2,1,1,2,1,1,2,1,2,1,1,1,1,1,2,1,1,1,2,2,1,1,1,1,1,1,1,1,2,1,1,1,2,1,1,2,2,1,1,1,2,1,2,2,1,1,1,2,2,1,2,1,1,2,2,1,1,2,2,1,1,2,1,1,1,1,2,1,2,1,1,1,1,1,1,1,1,2,2,1,1,1,1,1,1,2,1,1,1,1,1,1,1,2,1,1,1,2,1,1,2,1,1,1,2,2,1,1,1,1,1,1,1,1,1,2,1,2,1,1,1,1,2,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,2,1,1,2,2,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,2,2,1,2,1,2,1,1,1,1,1,1,2,1,1,2,2,1,1,2,1,2,1,1,1,2,1,1,1,1,1,1,1,1,1,2,1,1,1,2,1,1,1,1,1,1,1,1,1,1,2,1,1,2,1,2,2,2,2,1,1,1,1,2,1,2,1,2,1,1,1,1,1,1,1,2,1,1,1,1,2,1,1,2,1,1,1,1,1,1,2,1,1,2,2,1,1,2,2,1,1,1,1,1,2,1,1,1,1,1,2,2,1,1,1,1,1,1,2,1,1,1,1,2,2,1,2,1,1,2,2,1,2,1,1,2,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,2,2,1,1,1,1,1,1,2,1,2,1,2,2,1,1,2,2,1,1,2,2,1,1,1,2,2,1,2,1,2,1,1,1,1,2,1,2,2,2,2,2,1,2,1,1,1,1,1,1,1,1,2,1,1,1,2,1,2,1,1,2,2,2,2,1,1,1,1,1,2,1,1,1,1,2,1,1,2,1,1,1,1,1,1,1,2,1,1,1,2,2,2,1,1,1,1,1,1,1,1,1,2,1,1,2,1,1,2,2,2,1,1,1,1,1,2,1,2,1,2,1,1,1,1,2,1,2,1,2,2,2,1,1,1,2,1,2,1,1,1,2,1,1,1,1,1,1,1,1,2,1,1,2,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,1,2,1,2,2,1,1,1,1,2,1,1,1,2,1,2,2,1,1,1,1,1,1,2,1,1,2,1,2,1,1,1,2,2,1,2,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,1,1,1,1,1,1,1,1,1,2,1,1,1,2,1,1,1,1,1,1,2,1,1,1,1,1,1,2,1,2,2,1,1,1,2,2,1,2,1,1,1,1,1,2,2,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,2,1,1,2,1,1,2,1,1,1,1,2,1,1,2,1,1,2,1,1,2,1,1,1,1,1,1,1,1,1,1,1,2,2,1,1,1,2,2,1,2,1,1,1,1,1,1,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,1,1,1,2,1,1,1,2,1,1,1,1,1,1,1,1,1,1,2,2,1,1,2,1,1,1,2,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,2,1,1,1,1,1,1,2,1,2,1,1,1,1,1,1,2,1,1,2,1,1,1,2,1,2,1,1,1,1,1,2,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,2,1,1,1,1,1,1,2,1,1,2,1,1,1,2,1,1,1,1,1,2,1,1,1,2,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,2,1,2,1,1,2,1,1,2,1,1,1,2,1,1,1,1,1,1,2,1,1,1,2,1,1,1,1,1,1,1,1,2,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,2,1,1,1,2,2,1,1,2,1,1,1,1,2,1,1,1,2,2,1,2,2,1,1,1,2,1,1,1,2,1,1,1,1,1,1,1,1,2,1,1,2,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,2,1,1,1,1,2,2,1,1,1,1,1,1,1,1,1,1,1,1,2,2,1,2,1,1,1,1,1,2,1,1,1,1,2,2,2,1,1,2,2,2,1,1,1,1,1,2,1,1,1,1,2,1,1,1,2,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,1,2,1,1,1,1,1,1,2,1,1,1,1,1,2,1,1,1,1,1,1,2,1,1,1,2,1,2,1,2,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,2,1,1,1,1,1,1,1,2,1,1,2,1,2,1,1,1,1,1,2,1,1,1,2,1,1,1,1,1,2,1,2,2,2,2,1,2,1,2,2,1,1,2,1,1,2,2,1,1,1,1,1,1,1,1,1,1,2,2,2,1,2,1,1,1,1,2,1,2,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,1,1,2,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,2,1,1,1,1,1,1,2,2,2,1,2,2,1,1,1,2,1,1,1,1,2,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,2,1,1,1,1,1,2,1,1,2,1,1,1,1,1,1,1,1,1,1,2,2,2,1,1,2,1,1,1,1,1,1,2,2,1,2,1,1,1,1,2,2,1,2,2,1,1,1,2,1,2,2,2,1,1,1,2,2,1,1,1,1,1,1,1,2,1,1,2,2,1,1,1,2,1,1,2,2,1,2,2,1,1,1,2,1,1,2,1,1,1,2,1,1,1,1,2,1,1,1,2,1,2,2,1,1,2,1,1,1,1,1,2,2,1,1,2,2,2,1,1,2,1,2,1,1,2,2,2,1,1,1,1,2,1,1,1,1,2,1,2,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,1,2,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1], [1,2,1,1,2,1,1,1,1,1,1,2,2,2,1,1,2,1,1,2,1,2,1,2,1,1,1,1,1,2,1,1,1,2,2,1,1,1,1,1,1,1,2,2,1,1,1,1,1,1,1,1,2,1,1,1,2,1,1,1,1,1,2,2,2,1,1,1,1,1,1,2,1,2,2,2,1,1,1,2,2,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,2,2,1,1,2,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,1,1,2,1,1,1,1,1,1,1,1,1,2,1,1,2,1,1,1,1,1,1,1,1,2,2,1,1,1,1,1,1,1,2,1,2,2,1,1,1,1,2,1,1,1,2,1,2,1,1,2,1,1,1,2,2,1,1,1,1,1,2,1,1,1,1,2,1,1,1,1,2,1,1,1,1,2,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,2,2,1,2,1,2,2,1,1,2,1,1,1,1,1,2,1,1,1,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,1,1,2,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,2,1,1,1,1,1,2,1,1,2,1,1,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,1,1,1,2,1,1,2,1,1,1,1,2,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,2,2,1,1,1,2,1,1,1,1,1,1,2,1,1,1,2,1,1,1,2,1,1,1,1,1,1,2,1,1,1,1,2,1,1,1,1,1,1,1,1,1,2,1,2,2,2,1,2,1,2,1,1,1,2,1,2,1,1,1,2,1,1,1,1,1,2,1,2,1,1,2,1,1,1,1,1,2,1,1,1,1,2,2,2,1,1,1,1,1,1,1,2,2,1,1,2,2,1,1,1,1,1,1,2,2,1,1,1,1,1,2,1,1,1,1,1,2,1,1,2,2,1,2,1,1,1,1,1,1,1,2,2,1,2,2,1,2,1,1,1,1,1,1,1,1,2,2,1,1,1,2,1,2,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,1,2,1,2,1,1,1,1,1,2,2,1,1,2,1,1,1,2,1,1,2,2,1,1,1,1,1,1,2,2,1,1,1,1,1,1,1,2,2,1,1,1,1,1,1,1,1,2,1,1,1,1,2,1,2,1,2,1,2,1,1,1,1,2,1,1,1,1,1,1,1,2,1,1,1,1,1,2,1,1,1,1,1,2,1,2,1,1,2,1,1,1,1,1,2,1,1,1,1,1,1,1,2,1,2,1,1,2,1,1,1,1,1,2,1,2,1,1,2,2,1,1,1,1,1,1,1,1,2,2,2,1,1,1,1,1,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,2,1,1,1,2,1,1,1,2,1,1,1,1,2,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,2,1,1,1,1,2,1,1,1,2,2,1,1,1,1,2,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,2,1,1,1,2,2,1,2,1,1,2,2,1,2,1,1,1,1,1,1,2,2,1,1,2,1,1,1,2,1,2,1,2,1,1,2,1,2,2,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,2,1,1,2,2,2,2,1,1,2,1,1,1,1,2,1,1,1,1,2,1,1,1,1,2,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,2,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,2,1,2,1,2,1,1,2,2,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,2,1,1,1,2,1,1,1,2,1,1,2,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,2,2,1,1,2,2,1,2,1,1,1,2,1,1,2,1,1,1,1,1,1,2,2,1,1,1,1,1,1,1,1,1,2,1,2,1,1,2,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,2,2,1,1,1,2,1,1,1,1,1,1,2,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,2,2,1,1,2,1,1,1,1,2,1,1,2,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,2,1,1,1,1,2,2,1,1,1,1,1,1,1,1,2,1,1,2,1,2,1,1,1,1,1,2,1,1,1,2,2,2,1,1,1,1,2,1,1,1,1,1,1,1,2,1,1,1,1,1,2,2,2,2,2,1,2,1,1,2,1,2,2,2,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,2,2,2,1,2,1,1,1,2,1,2,1,1,1,1,1,1,1,1,1,1,2,1,1,1,2,1,1,1,1,1,1,1,1,1,1,2,1,1,1,2,1,1,1,2,2,2,2,1,1,2,2,2,1,1,2,2,1,1,1,1,1,1,2,1,1,1,1,1,2,1,1,1,1,2,1,1,1,1,2,1,1,1,2,1,1,2,1,1,2,2,1,1,1,1,1,2,1,1,1,1,1,1,1,1,2,1,2,2,1,1,2,2,1,1,1,1,2,1,1,1,1,1,1,2,1,1,1,1,1,2,1,1,1,2,1,2,1,1,2,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,2,1,2,1,1,2,1,1,1,1,1,2,1,1,1,2,1,1,2,1,1,1,2,1,2,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,2,2,2,2,1,1,1,2,1,1,1,2,1,2,1,2,1,2,1,1,1,2,1,1,1,2,1,1,1,1,1,2,1,1,1,2,1,2,1,1,1,1,2,1,2,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,2,1,1,1,2,1,1,1,1,1,1,2,1,1,1,2,1,2,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,1,1,2,2,1,1,1,2,1,1,2,1,1,1,1,1,2,2,2,1,1,1,1,2,1,1,1,1,1,1,2,1,1,1,2,1,1,1,2,1,1,1,1,2,2,2,2,2,1,1,2,1,1,1,1,1,1,2,2,2,2,1,1,1,2,2,2,2,2,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,1,1,1,1,2,1,1,1,1,1,1,1,2,1,1,2,1,1,2,1,1,2,1,2,1,1,1,1,2,1,1,2,2,1,1,2,1,1,1,1,1,1,1,2,1,1,2,1,1,2,1,2,1,2,2,1,1,1,2,1,1,1,2,1,1,1,2,1,1,2,1,1,1,1,1,1,1,2,2,2,1,1,2,2,1,1,2,1,1,1,2,1,1,1,1,1,2,1,1,1,1,2,1,1,1,1,2,1,1,1,2,1,1,1,1,2,2,1,1,2,2,1,2,2,2,1,1,1,2,1,1,1,1,1,1,1,1,2,1,1,2,2,1,1,1,1,1,1,2,1,2,1,2,2,1,1,1,1,1,2,1,1,2,1,1,1,2,1,1,1,2,1,1,1,2,1,1,1,1,1,1,1,1,2,1,1,1,2,1,2,1,2,1,1,2,1,1,2,1,2,2,1,1,2,1,1,2,1,1,1,1,2,1,2,2,1,1,2,1,1,1,1,1,1,2,1,1,1,1,1,2,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,1,1,1,2,1,2,1,2,1,1,1,1,2,2,1,1,2,1,1,1,1,2,2,1,2,1,1,1,2,1,1,2,2,2,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,2,1,2,1,1,1,1,1,1,1,1,1,1,2,2,1,1,1,2,1,1,1,2,1,1,1,2,2,1,2,1,1,2,1,2,1,2,1,2,1,1,1,1,1,1,1,2,1,1,2,2,1,1,1,1,2,1,1,1,2,2,1,1,1,1,1,1,1,2,2,1,2,1,2,2,1,1,1,1,1,1,1,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,2,2,1,1,2,1,1,1,1,1,1,1,2,1,1,1,2,1,2,1,1,1,2,1,1,1,2,1,2,1,2,1,2,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,2,1,1,1,1,1,1,2,1,1,1,1,1,1,2,1,1,1,2,1,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,2,2,1,2,1,2,1,1,1,1,1,1,2,1,1,1,1,1,2,1,1,1,1,2,1,1,1,1,1,2,2,2,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,1,2,2,1,1,2,2,1,1,1,1,2,2,1,2,1,1,2,2,2,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,2,1,1,2,1,1,2,2,1,1,2,2,1,1,2,1,2,1,1,1,1,1,1,2,1,1,1,2,1,1,2,1,1,2,2,1,2,1,2,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,2,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,2,1,1,2,1,1,1,1,2,1,1,2,1,2,1,1,1,1,1,1,1,2,2,2,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,2,1,1,1,2,1,1,2,1,1,2,1,2,1,2,1,1,2,2,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,2,2,2,1,2,1,1,2,1,1,1,1,1,2,2,1,1,1,1,2,2,1,1,1,2,2,1,1,2,2,1,1,1,2,1,1,1,2,1,2,2])