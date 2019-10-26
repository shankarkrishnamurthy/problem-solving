from typing import *
class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        h = {}
        for i in range(1,25):
            h[i] = (2**(i-1),2**i-1)
            if label <= 2**i-1: break
        rc = [label]
        while rc[-1] > 1:
            i -= 1
            nrc = rc[-1]//2
            rc.append(h[i][0] + h[i][1] - nrc)
        return rc[::-1]
        
        

print(Solution().pathInZigZagTree(1))
print(Solution().pathInZigZagTree(2))
print(Solution().pathInZigZagTree(3))
print(Solution().pathInZigZagTree(14))
print(Solution().pathInZigZagTree(26))
print(Solution().pathInZigZagTree(10**6))
