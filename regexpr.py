class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        def is_pat_over(i):
                pli = [x for x in range(i+1, pl) if len(pat[x]) == 1]
                if not pli: return True
                else: return False

        print 'pattern:', p, ';string:', s," : ",
        pat=[]
        for i in p:
            if i == '*': pat[-1] += '*'
            else: pat.append(i)
        pl = len(pat)
        if len(s) == 0: return is_pat_over(-1)
        q = set()
        q.add(0)
        print "plist", pat
        for i in range(pl):
            temp = set()
            for st in q:
                if len(pat[i]) > 1:
                    temp.add(st)
                    while st < len(s) and (s[st] == pat[i][0] or pat[i][0] == '.'):
                        st += 1
                        if st >= len(s):
                            if is_pat_over(i): return True
                            continue
                        temp.add(st)
                else:
                    if pat[i][0] == '.' or s[st] == pat[i][0]:
                        st += 1
                        if st >= len(s):
                            if is_pat_over(i): return True
                            continue
                        temp.add(st)
            print "i ",i," temp", temp
            if not temp:
                return is_pat_over(i-1)
            q = temp
        return False
        
print Solution().isMatch("ab",".*c")
print Solution().isMatch("","a*")
print Solution().isMatch("","")
print Solution().isMatch("a","")
print Solution().isMatch("","a")
print Solution().isMatch("aa","a*")
print Solution().isMatch("ab",".*")
print Solution().isMatch("aa","aa")
print Solution().isMatch("aa","a*bc.*")
print Solution().isMatch("aa","a")
print Solution().isMatch("aaa","aa")
print Solution().isMatch("aab", "c*a*b")
