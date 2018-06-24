class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        n = len(S)
        stack, val=[], []
        for i in range(n):
            if S[i] == '(': stack.append(i)
            else:
                j = stack.pop(-1)
                if i-j == 1: val.append((j,1))
                else:
                    k,v = val[-1]
                    s = 0
                    while k > j: 
                        s += v
                        val.pop()
                        if not val: break
                        k,v = val[-1]
                    val.append((j,2*s))
        #print val
        if len(val) > 1:
            k,v = val[-1]
            s = 0
            while val: 
                s += v
                val.pop()
                if not val: break
                k,v = val[-1]
            val.append((k,s))
        k,v = val[-1]
        return v

print Solution().scoreOfParentheses("()")
print Solution().scoreOfParentheses("(())")
print Solution().scoreOfParentheses("()()")
print Solution().scoreOfParentheses("(()(()))")
