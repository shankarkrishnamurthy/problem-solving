class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        m,n = len(str1), len(str2)
        b = min(m,n)
        fa = [b]
        for i in xrange(b-1,0,-1):
            if b%i==0: fa.append(i)
        #print fa
        res = ""
        for v in fa:
            if n % v != 0 or m % v !=0: continue
            cs = str1[:v]
            if str1 != cs*(m/v) or str2 != cs*(n/v): continue
            return cs
        return ""

print Solution().gcdOfStrings("ABAABA", "ABA")
print Solution().gcdOfStrings("ABCABC", "ABC")
print Solution().gcdOfStrings("ABABAB", "ABAB")
print Solution().gcdOfStrings("LEET", "CODE")
print Solution().gcdOfStrings("L", "C")
print Solution().gcdOfStrings("C", "C")
