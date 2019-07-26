class Solution(object):
    def smallestSubsequence(self, t):
        """
        :type t: str
        :rtype: str
        """
        h,ans,s={},[],set()
        for i,v in enumerate(t): h[v] = i
        for i,c in enumerate(t):
            if c in s: continue
            while ans and ans[-1] > c and h[ans[-1]] > i: 
                k=ans.pop()
                s.remove(k)
            ans+=[c]
            s.add(c)
        return ''.join(ans)

print Solution().smallestSubsequence("cbaacabcaaccaacababa")
print Solution().smallestSubsequence("ddeeeccdce")
print Solution().smallestSubsequence("cdadabcc")
print Solution().smallestSubsequence("abcd")
print Solution().smallestSubsequence("ecbacba")
print Solution().smallestSubsequence("leetcode")
