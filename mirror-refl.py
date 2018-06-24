class Solution(object):
    def mirrorReflection2(self, p, q):
        def gcd(a,b):
            if b == 0: return a
            return gcd(b, a%b)
        gcdval = gcd(p,q)
        lcm = p*q / gcdval
        turns = lcm / p
        #print "gcd", gcdval, "lcm(%d,%d) = " % (p,q), lcm, 'turns', turns
        if turns % 2 == 0: return 0
        if lcm/q % 2 == 0: return 2
        else: return 1

    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        if q == 0: return 0
        toggle,np,slope,side = False,p, float(p)/float(q), 2
        while True:
            delta = np % q

            if delta == 0.0:
                if toggle==0:
                    if np/q % 2 == 0: return side
                    else: return (2 if side ==1 else 1)
                else:
                    return 0
            else:
                if int(np/q) % 2 == 0: side = (2 if side == 1 else 1)
                tmp1 = slope * delta
                np = p - 1/slope *(p - tmp1) # slope > 1 so 1/slope < 1
                np = int(round(np))
                #print slope, 'touch %s @' % ('ceiling' if not toggle else 'floor'), tmp1, 'np',np

            toggle = not toggle
                
print Solution().mirrorReflection(3,2) # 0
print Solution().mirrorReflection(5,3) # 1
print Solution().mirrorReflection(4,3) # 2
print Solution().mirrorReflection(2,2)
print Solution().mirrorReflection(9,6) # 1
print Solution().mirrorReflection(6,5) # 1
print Solution().mirrorReflection(11,7) # 1
print Solution().mirrorReflection(5,3) # 1
print Solution().mirrorReflection(4,3) # 2
print Solution().mirrorReflection(3,1)
print Solution().mirrorReflection(2,1)
print Solution().mirrorReflection(2,0)
