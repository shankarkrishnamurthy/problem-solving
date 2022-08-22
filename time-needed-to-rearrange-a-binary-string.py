class Solution:
    def secondsToRemoveOccurrences(self, s):
        cnt, res, s = 1, 0, list(map(int, s))
        while cnt > 0:
            i, cnt = 0, 0
            while i < len(s)-1:
                if s[i] == 0 and s[i+1] == 1: 
                    s[i], s[i+1], cnt, i = 1, 0, 1, i+2
                else: i += 1
            if cnt > 0: res += 1
        return res
