class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = []        
        for i in range(len(S)):
            if S[i] == ')' and len(stack) > 0:
                if stack[-1] == '(': 
                    stack.pop()
                    continue
            stack.append(S[i])
        return len(stack)

print Solution().minAddToMakeValid("())")
print Solution().minAddToMakeValid("(((")
print Solution().minAddToMakeValid("()")
print Solution().minAddToMakeValid("()))((")
