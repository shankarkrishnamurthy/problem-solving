class Solution(object):
    def localmin(self,l):
        print l
        if len(l) < 2: return []
        res = []
        for i,v in enumerate(l):
            left,right=1 if i==0 else 0,1 if i == len(l)-1 else 0
            if i >0 and v < l[i-1]: left = True
            if i < len(l)-1 and v < l[i+1] : right=True
            if left and right: res.append(i)

        return res

print Solution().localmin([9, 6, 3, 14, 5, 7, 4])
print Solution().localmin([1, 3, 2, 8, 4, 9])
