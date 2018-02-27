class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        print s,
        stack = []
        msf = 0 # max so far
        lvi = -1 # last valid index
        lvl = 0 # last valid longest
        for i,p in enumerate(s):
            if p == ')':
                if not stack:
                    lvi = -1
                    lvl = 0
                    continue
                else:
                    idx,lvi,lvl = stack.pop()
                    curr = i - idx + 1
                    if lvi != -1:
                        curr += lvl
                    msf = max(msf, curr)
                    lvi = i
                    lvl = curr
            else:
                stack.append((i,lvi,lvl));
                lvi = -1
                lvl = 0
        return msf

print Solution().longestValidParentheses(")()())")
print Solution().longestValidParentheses("(())")
print Solution().longestValidParentheses("(()")
print Solution().longestValidParentheses(")")
print Solution().longestValidParentheses("(")
print Solution().longestValidParentheses("")
print Solution().longestValidParentheses("()()()()()()()")
print Solution().longestValidParentheses("()()()()(()()()")
print Solution().longestValidParentheses("(()((((")
print Solution().longestValidParentheses("(()(((()")
print Solution().longestValidParentheses(")))()(((")
print Solution().longestValidParentheses("(((())))))")
