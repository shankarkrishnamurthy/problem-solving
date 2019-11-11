from typing import *
class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        ans = [[0]*len(colsum),[0]*len(colsum)]
        for i,v in enumerate(colsum):
            #print('i',i,'v',v,'u',upper,'l',lower)
            if v == 0: continue
            if v == 2:
                if upper > 0 and lower > 0:
                    upper -= 1
                    lower -= 1
                    ans[0][i] = ans[1][i] = 1
                    continue
                else: return []
            if upper ==0 and lower==0: return []
            if upper > lower:
                upper -= 1
                ans[0][i] = 1
            else:
                lower -= 1
                ans[1][i] = 1
        if upper > 0 or lower > 0: return []
        return ans

#print(Solution().reconstructMatrix(upper = 2, lower = 1, colsum = [1,1,1]))
#print(Solution().reconstructMatrix(upper = 2, lower = 3, colsum = [2,2,1,1]))
print(Solution().reconstructMatrix(upper = 5, lower = 5, colsum = [2,1,2,0,1,0,1,2,0,1]))
print(Solution().reconstructMatrix(4,7,[2,1,2,2,1,1,1]))
