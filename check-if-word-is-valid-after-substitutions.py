class Solution(object):
    def isValid(self, S):
        """
        :type S: str
        :rtype: bool
        """
        s = []
        for i in S: 
            if i == 'c':
                if len(s) > 1 and s[-1] == 'b' and s[-2] == 'a':
                    s.pop() 
                    s.pop()
                else:
                    s.append(i)
            else:
                s.append(i)
        if len(s) > 0:
            return False
        else:
            return True

print Solution().isValid("aabcbc")
print Solution().isValid("abcabcababcc")
print Solution().isValid("abccba")
print Solution().isValid("cababc")
print Solution().isValid("abcabcababcc")
print Solution().isValid("abc")
print Solution().isValid("ababababababcccccc")
print Solution().isValid("ababababababccccc")
