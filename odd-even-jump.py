from bisect import *
class Solution(object):
    def oddEvenJumps(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        def closest(v, i): # (closest bigger value index,closest smaller value index)
            cl = bisect_left(sf, v) # find next biggest element
            cr = bisect(sf,v)
            if cl == len(sf):
                gr = -1
                sm = sfi[sf[-1]]
            elif cr == 0:
                gr = sfi[sf[0]]
                sm = -1
            else:
                gr = sfi[sf[cl]]
                sm = sfi[sf[cr-1]]
            insort_left(sf,v)
            sfi[v] = i
            return (gr,sm)

        n = len(A)
        sf,sfi = [A[-1]],{ A[-1]: n-1 }
        rc,ans = [(1,1)],1
        for i in range(n-2,-1,-1):
            j,k = closest(A[i],i)
            odd = rc[n-j-1][1] if j != -1 else 0
            even = rc[n-k-1][0] if k != -1 else 0
            rc.append((odd,even))
            ans += odd 
            #print rc[::-1],'\n    ', sf, sfi
        return ans

#print Solution().oddEvenJumps([10,13,12,14,15])
#print Solution().oddEvenJumps([5,1,3,4,2])
print Solution().oddEvenJumps([2,3,1,1,4])

