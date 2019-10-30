from typing import *
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        dp=[set()]
        for a in arr:
            if len(set(a)) != len(a): continue
            for e in list(dp):
                if e & set(a): continue
                dp.append(e | set(a))
            #print(dp)
        return max(len(i) for i in dp)

print(Solution().maxLength(["un","iq","ue"]))
print(Solution().maxLength(["cha","r","act","ers"]))
print(Solution().maxLength(["abcdefghijklmnopqrstuvwxyz"]))
