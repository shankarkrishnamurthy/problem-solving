class Solution(object):
    def longestStrChain(self, w):
        """
        :type words: List[str]
        :rtype: int
        """
        ws,msf={i:1 for i in w},1
        w.sort(key=lambda x:len(x), reverse=True)
        #print w
        for t in w:
            for i in xrange(len(t)):
                c = t[:i] + t[i+1:]
                if c in ws:
                    ws[c] = max(ws[c], 1 + ws[t])
                    msf = max(msf, ws[c])
        #print ws
        return msf

print Solution().longestStrChain(["a","abc"])
print Solution().longestStrChain(["a"])
print Solution().longestStrChain(["a","b","ba","bca","bda","bdca"])
