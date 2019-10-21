class Solution:
    def equalSubstring(self, s: str, t: str, mC: int) -> int:
        l,o,cwc,msf = 0,{},0,0
        for i in range(ord('a'),ord('z')+1): o[chr(i)] = i
        def cost(a,b): return abs(o[a]-o[b])

        for i,(m,n) in enumerate(zip(s,t)):
            cwc += cost(m,n)
            if cwc <= mC: 
                if msf < i-l+1: msf = i-l+1
                continue
            # else
            while cwc > mC:
                cwc -= cost(s[l],t[l])
                l += 1
            
        return msf

print(Solution().equalSubstring(s = "abcd", t = "bcdf", mC = 3))
print(Solution().equalSubstring(s = "abcd", t = "cdef", mC = 3))
print(Solution().equalSubstring(s = "abcd", t = "acde", mC = 0))
print(Solution().equalSubstring(s = "bcad", t = "cdae", mC = 0))
print(Solution().equalSubstring(s = "bcad", t = "efgh", mC = 0))
