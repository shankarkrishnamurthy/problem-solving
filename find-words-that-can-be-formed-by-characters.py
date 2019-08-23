class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        c,ans = {},0
        for i in chars: c[i] = c.get(i,0)+1
        for w in words:
            x,ok = {}, True
            for i in w: x[i] = x.get(i,0)+1
            for i in x:
                if i in c and x[i] <= c[i]: continue
                ok = False
            if (ok): ans += len(w)
        return ans
                
            

print Solution().countCharacters(["cat","bt","hat","tree"], "atach")
print Solution().countCharacters(["hello","world","leetcode"], "welldonehoneyr")
