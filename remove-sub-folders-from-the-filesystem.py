from typing import *
class Solution:
    def removeSubfolders(self, f: List[str]) -> List[str]:
        h,res = set(),[]
        f.sort()
        for i in f:
            fl,found = i.split('/'),False
            for k in range(1,len(fl)):
                if '/'.join(fl[:k]) in h: found = True
            if found: continue
            h.add(i)
        return list(h)
        
        

print(Solution().removeSubfolders(["/a","/a/b","/c/d","/c/d/e","/c/f"]))
print(Solution().removeSubfolders(["/a","/a/b/c","/a/b/d"]))
print(Solution().removeSubfolders(["/a/b/c","/a/b/ca","/a/b/d"]))
