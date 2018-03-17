class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        self.help(s, res, 0, 0, ('(', ')'))
        return res
    
    def help(self, s, res, start, end, dic):
        stack = 0
        for i in range(start, len(s)):
            if s[i] == dic[0]: stack += 1
            if s[i] == dic[1]: stack -= 1
            if stack >= 0: continue
            
            for j in range(end, i + 1):
                if s[j] == dic[1] and (j == end or s[j] != s[j - 1]) :
                    self.help(s[:j] + s[j+1:], res, i, j, dic)
            return
        revers = s[::-1]
        if dic[0] == '(':
            self.help(revers, res, 0, 0, (')', '('))
        else:
            res.append(revers)
        return 
"""
class Solution(object):
    def removeInvalidParentheses(self, s):
        def invalid(s):
            cnt, notvalid, nevervalid, openonce=0,False, True, False
            for c in s:
                if c=='(': 
                    cnt += 1
                    openonce = True
                if c==')': 
                    cnt -= 1
                    if openonce: nevervalid = False
                if cnt < 0: notvalid = True
            if cnt != 0: notvalid = True
            return (notvalid, nevervalid)
        l,cn = {s}, 0
        while l:
            tmp,skip=set(), set()
            for i in l:
                (nov, nev) = invalid(i)
                if not nov: tmp.add(i)
                if nov and nev: 
                    skip.add(i)
                    yes=filter(lambda x: x!='(' and x!=')', s)
                    if yes and len(l) == 1: return [yes]
            if tmp: return list(tmp)
            l = {it[:k] + it[k+1:] for it in l-skip for k in range(len(it))}
        return [""]
"""
    
print Solution().removeInvalidParentheses("()())()")
print Solution().removeInvalidParentheses("(a)())()")
print Solution().removeInvalidParentheses("a)b)c)d)e)f)g)h)i)j)k)l)m)n)o)p)q)r)s)t)u)v)w)x)y)z)((((((((((((((((((((")
print Solution().removeInvalidParentheses("))((")
print Solution().removeInvalidParentheses("((")
print Solution().removeInvalidParentheses("xyz")
print Solution().removeInvalidParentheses("x(")
print Solution().removeInvalidParentheses("))")
print Solution().removeInvalidParentheses(")()(")
print Solution().removeInvalidParentheses("((i)")
print Solution().removeInvalidParentheses("(((()p")
