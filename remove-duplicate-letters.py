class Solution(object):
    def removeDuplicateLetters(self, t):
        """
        :type s: str
        :rtype: str
        """
        h,ans={},[]
        for i,v in enumerate(t): h[v] = i
        for i,c in enumerate(t):
            if c in ans: continue
            while ans and ans[-1] > c and h[ans[-1]] > i: 
                k=ans.pop()
            ans+=[c]
        return ''.join(ans)

print Solution().removeDuplicateLetters("cbaacabcaaccaacababa")
print Solution().removeDuplicateLetters("ddeeeccdce")
print Solution().removeDuplicateLetters("cdadabcc")
print Solution().removeDuplicateLetters("abcd")
print Solution().removeDuplicateLetters("ecbacba")
print Solution().removeDuplicateLetters("leetcode")

