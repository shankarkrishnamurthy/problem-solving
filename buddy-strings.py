class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        a = len(A)
        b = len(B)
        if a != b or a < 2: return False
        d,h,samechar = [], {}, False
        for i in range(a):
            h[A[i]] = h.get(A[i], 0) + 1
            if h[A[i]] > 1: samechar = True
            if A[i] != B[i]: 
                d.append(i)
            if len(d) > 2: 
                return False
        #print d,a,b
        if len(d) == 0 and a > 1 and samechar: return True
        if len(d) == 2:
            i1,i2 = d[0], d[1]
            if A[i1] == B[i2] and A[i2] == B[i1]: 
                return True
        return False
        
print Solution().buddyStrings("ab", "ba")
print Solution().buddyStrings("ab", "ab")
print Solution().buddyStrings("aa", "aa")
print Solution().buddyStrings("aaaaaaabc", "aaaaaaacb")
print Solution().buddyStrings("","aa")
print Solution().buddyStrings("a","a")
