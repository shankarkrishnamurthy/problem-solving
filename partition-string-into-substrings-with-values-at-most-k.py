class Solution:
    def minimumPartition(self, s, k):
        pr, res = 0, 0
        if int(s[pr]) > k: return -1
        for i in range(1,len(s)):
            pv, cv = int(s[pr:i]), int(s[pr:i+1])
            if cv > k:
                res += 1
                pr = i
                if int(s[pr]) > k: return -1
        return 1+res
