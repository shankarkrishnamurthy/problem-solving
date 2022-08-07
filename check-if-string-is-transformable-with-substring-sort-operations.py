class Solution:
    def isTransformable(self, s, t):
        dp = [deque() for _ in range(10)]
        for i,v in enumerate(s): dp[int(v)].append(i)
        for v in t:
            v = int(v)
            if not dp[v]: return False
            for low in range(int(v)):
                if not dp[low]: continue
                if dp[low][0] < dp[v][0]: return False
            dp[v].popleft()
        return True
