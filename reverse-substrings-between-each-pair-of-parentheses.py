class Solution:
    def reverseParentheses(self, s: str) -> str:
        st,ans = [],list(s)
        for i,v in enumerate(s):
            if v not in ('(',')'): continue
            if v == '(':
                st.append(i)
            else:
                ans[st[-1]:i+1] = ans[st[-1]:i+1][::-1]
                st.pop()
        return ''.join([j for j in ans if j not in ('(',')')])

print(Solution().reverseParentheses("(ed(et(oc))el)"))
print(Solution().reverseParentheses("(u(love)i)"))
print(Solution().reverseParentheses("(abcd)"))
