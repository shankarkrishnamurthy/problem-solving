class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        st,res = [],''
        for i,v in enumerate(S):
            if v == '(':
                st.append(i)
            else:
                j = st.pop()
                if not st: res += S[j+1:i]
        return res

print Solution().removeOuterParentheses("(()())(())")
print Solution().removeOuterParentheses("(()())(())(()(()))")
print Solution().removeOuterParentheses("()()")
