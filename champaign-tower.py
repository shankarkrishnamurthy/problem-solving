class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        if poured == 0: return 0.0
        if query_row == 0: return 1.0
        idx = query_row * (query_row + 1) / 2 + query_glass
        gl = [0.0] * (idx + 1)
        gl[0],pr,r = poured,0,1
        #print gl
        for i in range(1, query_row + 1):
            col,cnt = i + 1,0
            if query_row == i: col = query_glass + 1
            while cnt < col:
                pc = cnt-1 if cnt > 0 else 0
                if cnt == 0  or cnt == i: # single parent
                    #print '(%d,%d) ' %(i, cnt), 'parent', pr, pc
                    if gl[pr + pc] > 1.0:
                        gl[r+cnt] = (gl[pr + pc] - 1.0 ) / 2.0
                else:
                    #print '(%d,%d) ' %(i, cnt), 'parents', pr, pc,' ', pr,pc+1
                    if gl[pr + pc] > 1.0:
                        gl[r+cnt] = (gl[pr + pc] - 1.0 ) / 2.0
                    if gl[pr + pc + 1] > 1.0:
                        gl[r+cnt] += (gl[pr + pc + 1] - 1.0 ) / 2.0

                #print gl
                cnt += 1
            pr = r
            r += col
        return gl[idx] if gl[idx] <= 1.0 else 1.0

print Solution().champagneTower(10,2,2)
print Solution().champagneTower(1,1,1)
print Solution().champagneTower(2,1,1)
print Solution().champagneTower(3,2,2)
print Solution().champagneTower(4,2,2)
print Solution().champagneTower(4,2,1)
print Solution().champagneTower(10,5,5)
