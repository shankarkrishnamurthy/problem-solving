# Calculating Levenshtein distance 
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1 = len(word1) + 1
        l2 = len(word2) + 1
        dp = [[0]*l2 for i in range(l1)]
        for i in range(l1):
            dp[i][0] = i
        for i in range(l2):
            dp[0][i] = i
        for i in range(1,l1):
            for j in range(1,l2):
                dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1] + (word1[i-1] != word2[j-1]))
        return dp[l1-1][l2-1]

print Solution().minDistance("","")
print Solution().minDistance("","ab")
print Solution().minDistance("ab","")
print Solution().minDistance("a","b")
print Solution().minDistance("","")
print Solution().minDistance("horse","ros")
print Solution().minDistance("krithika","shankar")
print Solution().minDistance("shankar","krithika")
