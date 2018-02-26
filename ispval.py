class Solution(object):
    def isValid(self, st):
        """
        :type s: str
        :rtype: bool
        """
        p = []
        d = {'{': '}', '(': ')', '[':']'}
        for e in st:
            if e=='[' or e=='{' or e=='(' : 
                p.append(e)
            else:
                if (not p or e != d[p.pop()]):
                    return False
        if len(p) > 0:
            return False
        return True

a = "{[()]}"; val = Solution().isValid(a)
print a, "PASS" if (val) else "FAIL"
a = "{[(]]}"; val = Solution().isValid(a)
print a, "PASS" if (val) else "FAIL"
a = "{}"; val = Solution().isValid(a)
print a, "PASS" if (val) else "FAIL"
a = "}"; val = Solution().isValid(a)
print a, "PASS" if (val) else "FAIL"
a = ""; val = Solution().isValid(a)
print  a,"PASS" if (val) else "FAIL"
a = "["; val = Solution().isValid(a)
print  a,"PASS" if (val) else "FAIL"
a = "[(){}][{()()}]"; val = Solution().isValid(a)
print  a,"PASS" if (val) else "FAIL"
