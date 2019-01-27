class Solution(object):
    def strWithout3a3b(self, A, B):
        """
        :type C: int
        :type D: int
        :rtype: str
        """
        #print "Problem ", A, B
        global C,D,res
        res,C,D = '',A,B
        while C > 0 and D > 0:
            if C > D:
                av = (1 if C < 2 else 2)
                res += 'a'*av + 'b'
                C-=av
                D-=1
            elif C==D:
                if res and res[-1]== 'a':
                    res += 'ba'*C
                else:
                    res += 'ab'*C
                C=D=0
            else: 
                bv = (1 if D < 2 else 2)
                res += 'b'*bv+ 'a'
                D-=bv
                C-=1
            #print C,D,res
        if C > 0: res += 'a'*C
        if D > 0: res += 'b'*D
        return res
        
print Solution().strWithout3a3b(1,2)
print Solution().strWithout3a3b(1,3)
print Solution().strWithout3a3b(4,1)
print Solution().strWithout3a3b(2,5)
print Solution().strWithout3a3b(3,3)
print Solution().strWithout3a3b(4,5)
print Solution().strWithout3a3b(5,4)
