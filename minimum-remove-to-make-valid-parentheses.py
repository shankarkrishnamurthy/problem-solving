from typing import *
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        st,et = [],set()
        for i,v in enumerate(s):
            if v not in ('(',')'): continue
            if v == '(': st.append(i)
            else: 
                if st: st.pop()
                else: et.add(i)
        st,ans = set(st),''
        for i,v in enumerate(s):
            if i in st or i in et: continue
            ans += v
        return ans
        
            

print(Solution().minRemoveToMakeValid(s = "lee(t(c)o)de)"))
print(Solution().minRemoveToMakeValid(s = "a)b(c)d"))
print(Solution().minRemoveToMakeValid(s = "))(("))
print(Solution().minRemoveToMakeValid(s = "(a(b(c)d)"))
