class Solution(object):
    def prisonAfterNDays(self, c, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        h,rh,ic = {}, {}, 0
        while True:
            n = []
            #print ic, c
            if N == ic: return c
            cs =tuple(c)
            if cs in h: break
            h[cs] = ic
            rh[ic] = c
            for j in range(len(c)):
                if j == 0 or j == len(c)-1:
                    n.append(0)
                    continue
                if c[j-1] == c[j+1]: n.append(1)
                else: n.append(0)
                    
            c = n
            ic += 1
        #print 'prev i ', h[cs], ' curr i ', ic
        rem = (N-h[cs]) % (ic-h[cs])
        #print ' remainder ', rem
        return rh[h[cs]+rem]
        
        

print Solution().prisonAfterNDays([0,1,0,1,1,0,0,1], 7)
print Solution().prisonAfterNDays([1,0,0,1,0,0,1,0], 1000000000)

