class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        h,c = {},ord('a')
        for i in range(5):
            for j in range(5):
                h[chr(c)] = (i,j)
                c += 1
        h['z'],rc = (5,0),''
        c = (0,0)
        for i in target:
            t = h[i]
            print(c,'->',t)
            m1= 'R' if t[1] >= c[1] else 'L'
            m2= 'D' if t[0] >= c[0] else 'U'
            if c[0] == 5:
                rc += m2*abs(t[0]-c[0])
                rc += m1*abs(t[1]-c[1])
            else:
                rc += m1*abs(t[1]-c[1])
                rc += m2*abs(t[0]-c[0])
            rc += '!'
            c = h[i]
        return rc

print(Solution().alphabetBoardPath('leet'))
print(Solution().alphabetBoardPath('code'))
print(Solution().alphabetBoardPath('z'))
print(Solution().alphabetBoardPath('a'))
print(Solution().alphabetBoardPath('ezw'))
