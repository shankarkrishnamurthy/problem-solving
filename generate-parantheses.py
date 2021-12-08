class Solution:
    def __init__(o):
        o.out=[]
    def generateParenthesis(s, n):
        def dfs(anc, o, c):
            if o==0 and c==0:
                s.out.append(anc)
                return
            if o > 0: dfs(anc + '(', o-1,c)
            if c > o: dfs(anc + ')', o,c-1)
        dfs('',n,n)
        return s.out

print(Solution().generateParenthesis(1))
print(Solution().generateParenthesis(3))
