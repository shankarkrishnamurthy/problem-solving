class Solution:
    def maxRunTime(self, n: int, b: List[int]) -> int:
        b.sort()
        ex,sf,k = sum(b[:-n]),0,len(b)-n
        for i in range(n):
            sf += b[i+k]
            v = (sf + ex)//(i+1)
            if i < n-1:
                if v <= b[i+k+1]: return v
            else: return v           
        
