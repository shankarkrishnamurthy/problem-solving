class Solution:
    def mostPoints(self, questions):
        dp,msf=[0]*len(questions),0
        print('q ', questions)
        for i,(p,b) in enumerate(questions):
            if i+b+1 < len(questions):
                dp[i+b+1] = max(dp[i+b+1], p+dp[i])
            else:
                msf = max(msf, dp[i]+p)
            if i < len(questions)-1: dp[i+1] = max(dp[i], dp[i+1])
            print(' i' , i, ' dp ', dp)
        return msf

print(Solution().mostPoints([[3,2],[4,3],[4,4],[2,5]]))
print(Solution().mostPoints([[1,1],[2,2],[3,3],[4,4],[5,5]]))
print(Solution().mostPoints([[21,5],[92,3],[74,2],[39,4],[58,2],[5,5],[49,4],[65,3]]))
