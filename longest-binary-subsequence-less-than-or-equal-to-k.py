class Solution:
    def longestSubsequence(self, s, k):
        lm = [float("inf")]*(len(s)+1)
        lm[0], msf = 0, 0
        for i in range(len(s)):
            for j in range(i+1, msf, -1):
                nm = (lm[j-1] << 1) + int(s[i])
                lm[j] = min(lm[j], nm)
                if j < len(lm)-1 and lm[j] == 0 and lm[j+1] == 0:
                    msf = j
        for j in range(len(s),0,-1):
            if lm[j] <= k: return j
        return 0
