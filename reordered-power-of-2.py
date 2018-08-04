class Solution(object):
    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        def is_anagram(a,b):
            if not b: return False
            x = sorted(a)
            for e in b:
                y = sorted(e)
                if x == y: return True
            return False
            
        if N == 1: return True
        ph = {}
        for i in range(31):
            p2 = 2**i 
            lenp = len(str(p2))
            ph[lenp] = ph.get(lenp, [] ) + [str(p2)]
        #print ph
        
        nl = len(str(N))
        
        return is_anagram(str(N), ph[nl])

print Solution().reorderedPowerOf2(1)
print Solution().reorderedPowerOf2(10)
print Solution().reorderedPowerOf2(16)
print Solution().reorderedPowerOf2(24)
print Solution().reorderedPowerOf2(46)
print Solution().reorderedPowerOf2(536870912)
print Solution().reorderedPowerOf2(1404943)
print Solution().reorderedPowerOf2(4194304)
