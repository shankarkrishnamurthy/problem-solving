from typing import *
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        st = []
        for i,v in enumerate(s):
            if st and st[-1][0] == v and st[-1][1] == k-1:
                st[-k+1:] = []
            else:
                if st and st[-1][0] == v: st.append((v,st[-1][1]+1))
                else: st.append((v,1))
        return ''.join([v[0] for v in st])
                    
        
print (Solution().removeDuplicates(s = "pbbcggttciiippooaais", k = 2))
print (Solution().removeDuplicates(s = "deeedbbcccbdaa", k = 3))
