class Solution:
    def largestNumber(self, cost ,target):
        def big(arr):
            arr.sort(key=lambda x: (len(x), int(x)))
            return arr[-1]
        dp, ch = ['']+['#']*target, {}
        for i, c in enumerate(cost): ch[c] = str(i + 1)
        for t in range(1, target + 1):
            arr=[]
            for c, d in ch.items():
                if t-c < 0: continue
                if dp[t-c] != '#': arr.append(dp[t-c]+d)
            if arr: dp[t] = big(arr) 
        return "0" if dp[target] =='#' else dp[target]
