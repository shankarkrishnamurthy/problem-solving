class Solution:
    def longestIdealString(self, s, k):
        ch, dp = {chr(i): i-ord('a') for i in range(ord('a'), ord('z')+1)}, defaultdict(int)
        for c in s:
            v, t = ch[c], 0
            for i in range(-k, k+1):
                if 0<=v+i<26: t = max(t, dp[v+i])
            dp[v] = t+1
        #print(dict(dp))
        return max(dp.values())
