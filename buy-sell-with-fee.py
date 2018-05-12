class Solution(object):
    def localmin(self,l,fee):
        print l
        if len(l) < 2: return []
        stk = []
        dp = [0]*len(l)
        for i,v in enumerate(l):
            left,right=1 if i==0 else 0,1 if i == len(l)-1 else 0
            if i >0 and v < l[i-1]: left = True
            if i < len(l)-1 and v < l[i+1] : right=True
            if left and right: 
                stk.append(i)

            maxima,left,right=False,1 if i==0 else 0,1 if i == len(l)-1 else 0
            if i > 0 and v >= l[i-1]: left = True
            if i < len(l)-1 and v > l[i+1]:  right= True
            if left and right: maxima=True

            dp[i] = dp[i-1]
            if maxima and len(stk) > 0:
                cp = v - l[stk[-1]] - fee
                while len(stk) > 1:
                    np = v - l[stk[-2]] - fee
                    if dp[stk[-2]] + np >= dp[stk[-1]] + cp: 
                        stk.pop()
                        cp = np
                        continue
                    break
                dp[i] = max(dp[i-1],0,dp[stk[-1]] + cp)
                #dp[i] = max(0,dp[stk[-1]] + cp)
            print dp,stk,i

        return dp[len(l)-1]

print Solution().localmin([4,5,2,4,3,3,1,2,5,4] ,1)
print Solution().localmin([2,1,4,4,2,3,2,5,1,2],1)
"""
print Solution().localmin([9, 6, 3, 14, 5, 7, 4],1)
print Solution().localmin([1, 3, 2, 8, 4, 9],2)
print Solution().localmin([1, 4, 1, 8, 4, 9],2)
print Solution().localmin([1, 4, 2, 6, 5, 9],2)
print Solution().localmin([11, 8, 7, 4, 0],2)
print Solution().localmin([1, 3, 4, 6],1)
print Solution().localmin([9,8,7,1,2],3)
"""
