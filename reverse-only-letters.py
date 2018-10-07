class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        res = ''
        sign = []
        for i in range(len(S)):
            if ('a'<= S[i]<='z' or 'A'<=S[i]<='Z'):
                res += S[i]
            else:
                sign.append(i)
        res = res[::-1]
        for idx in sign:
            res = res[:idx] + S[idx] + res[idx:]
        return res

print Solution().reverseOnlyLetters("ab-cd")
print Solution().reverseOnlyLetters("a-bC-dEf-ghIj")
print Solution().reverseOnlyLetters("Test1ng-Leet=code-Q!")
