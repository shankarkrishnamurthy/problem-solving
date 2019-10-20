class Solution(object):
    def longestDecomposition(self, text):
        """
        :type text: str
        :rtype: int
        """
        l,r,c,res = 0, len(text)-1,0,0
        while l+c < r-c:
            if text[l:l+c+1] == text[r-c:r+1]:
                res += 2
                #print 'match ', text[l:l+c+1],' l ',l,' r ',r,' c ',c, 'ans ', res, 
                l = l+c+1
                r = r-c-1
                c = 0
                #print 'newl ',l, 'newr ', r 
            else:
                c+=1
        #print 'res ', res, l, r, text[l], c
        if c!=0 or l+c==r-c: res += 1
        return res
        
print Solution().longestDecomposition(text = "ghiabcdefhelloadamhelloabcdefghi")
print Solution().longestDecomposition(text = "merchant")
print Solution().longestDecomposition(text = "antaprezatepzapreanta")
print Solution().longestDecomposition(text = "aaa")
print Solution().longestDecomposition(text = "bb")
print Solution().longestDecomposition(text = "b")
print Solution().longestDecomposition(text = "bbbb")
