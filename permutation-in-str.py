class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        phm = {}
        for p in s1: phm[p] = phm.get(p,0)+1
        cpy = {}
        for r in range(len(s2)):
            l = r - len(s1) + 1
            c = s2[r]
            if c in phm: cpy[c] = cpy.get(c,0) + 1
            if cpy == phm: return True
            if l < 0: continue
            oc = s2[l]
            if oc in phm: cpy[oc] = cpy.get(oc,0) - 1
        return False

print(Solution().checkInclusion("adc","dcda"))
print(Solution().checkInclusion("a", "eidbaooo"))
print(Solution().checkInclusion("c", "eidbaooo"))
print(Solution().checkInclusion("ab", "eidbaooo"))
print(Solution().checkInclusion("ab", "eidboaoo"))
