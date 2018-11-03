# Test
class Solution(object):
    def isMatch(self, s, p):
        def is_pat_over(i):
            if i >= pl: return True
            if i == pl-1 and pat[i] == '*': return True
            return False
                
        pat = []
        i = 0
        for v in p:
            if i > 0 and pat[-1] == '*': 
                if v == '*': continue
                pat[-1] += v
            else: pat.append(v)
            i += 1
        pl = len(pat)
        if len(s) == 0: return is_pat_over(0)
        q = set()
        q.add(0)
        print pat, s, ":",
        for i in range(pl):
            t = set()
            #print i, list(q)
            for item in q:
                st = item
                if len(pat[i]) == 1 and pat[i] == '*': return True
                if len(pat[i]) > 1:
                    np = pat[i][1]
                    while st < len(s):
                        if np != s[st] and np != '?':
                            st += 1
                            continue
                        st+=1
                        if st >= len(s): 
                            if is_pat_over(i+1): return True
                            else: continue
                        t.add(st)
                else:
                    if pat[i][0] == s[st] or pat[i][0] == '?':
                        st+=1
                        if st >= len(s): 
                            if is_pat_over(i+1): return True
                            else: continue
                        t.add(st)
            if not t:
                return is_pat_over(i)
            q = t
        return False

print Solution().isMatch("cfa","c*a")
print Solution().isMatch("ca", "c*a")
print Solution().isMatch("ca", "ca")
print Solution().isMatch("cga", "c?a")
print Solution().isMatch("cga", "c??a")
print Solution().isMatch("cfkjgsaerel", "c*a")
print Solution().isMatch("cfkjgsa", "c*a")
print Solution().isMatch("cfkjgs", "c*a")
print Solution().isMatch("","")
print Solution().isMatch("","a*")
print Solution().isMatch("a","*")
print Solution().isMatch("a","")
print Solution().isMatch("","?")
print Solution().isMatch("f","?")
print Solution().isMatch("aab", "c*a*b")
print Solution().isMatch("aaaa", "***a")
