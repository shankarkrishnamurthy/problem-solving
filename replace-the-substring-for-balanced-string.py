from typing import *
class Solution:
    def balancedString(self, s: str) -> int:
        h,n = {},len(s)//4
        for i in s: h[i] = h.get(i,0)+1
        for i in list(h.keys()):
            if h[i] <= n: del h[i]
            else: h[i] = h[i] -n
        if not h: return 0

        print(h),n
        def is_suff():
            for i in h: 
                if i not in fh or fh[i] < h[i]: return False
            return True

        l,fh,msf = -1,{},len(s)
        for i,v in enumerate(s):
            if v not in h: continue
            if l <0: l = i
            fh[v] = fh.get(v,0) + 1
            if v == s[l] and fh[v] > h[v]: 
                fh[v] = h[v]
                while l < i:
                    l+=1
                    x=s[l]
                    if x not in h: continue
                    if fh[x] <= h[x]: break
                    fh[x] -= 1
            if is_suff():
                if msf > i-l+1: msf = i-l+1
        return msf
            
            
"""
print(Solution().balancedString("QWER"))
print(Solution().balancedString("QQWQ"))
print(Solution().balancedString("QEWQ"))
print(Solution().balancedString("QWQQ"))
print(Solution().balancedString("QQQQ"))
print(Solution().balancedString("WWEQERQWQWWRWWERQWEQ"))
"""
print(Solution().balancedString("WQWRQQQW"))
