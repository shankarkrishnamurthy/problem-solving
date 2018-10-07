class Solution(object):
    def spiralMatrixIII(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        def get_next(c,dr):
            if dr == 0: return (c[0],c[1]+1)     
            if dr == 1: return (c[0]+1,c[1])     
            if dr == 2: return (c[0],c[1]-1)     
            if dr == 3: return (c[0]-1,c[1])     
        def get_ndr(dr): return (dr+1) % 4
    
        NDR = { 'N': 'E', 'E':'S','S':'W','W':'N'}
        coset, dr = set([(r0,c0)]), 0
        st = (r0,c0)
        colist = [list(st)]
        while True:
            ne = get_next(st, dr)
            #print st, dr, 'next ',ne
            coset.add(ne)
            if 0<= ne[0] < R and 0 <= ne[1] < C:
                colist.append(list(ne))
            ndr = get_ndr(dr)
            st = ne

            # check if it can turn or go straight
            ne = get_next(st,ndr)
            if ne not in coset: dr = ndr

            if (0,0) in coset and (0,C-1) in coset and (R-1,C-1) in coset and (R-1,0) in coset: break
        return colist

            

print Solution().spiralMatrixIII(1,4,0,0) # [[0,0],[0,1],[0,2],[0,3]]
print Solution().spiralMatrixIII(5,6,1,4) # Output: [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]
#print Solution().spiralMatrixIII(100,100,5,40)
