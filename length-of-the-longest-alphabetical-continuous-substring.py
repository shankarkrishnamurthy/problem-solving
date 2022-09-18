class Solution:
    def longestContinuousSubstring(self, s):
        w, ws, res = string.ascii_lowercase, set(), 1
        for i in range(len(w)):
            for j in range(i): ws.add(w[j:i+1])
        for i in range(1, len(s)):
            if s[i-res:i+1] in ws: res += 1
        return res
