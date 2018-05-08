class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        wl = S.split(' ')
        res = []
        for i,v in enumerate(wl):
            ans,ele = '',v.lower()
            if ele[0] == 'a' or  ele[0] == 'e' or  ele[0] == 'i' or  ele[0] == 'o'  or  ele[0] == 'u' :
                ans = v + 'ma'      
            else:
                ans = v[1:] + v[0] + 'ma'
            ans += (i+1)*'a'
            res.append(ans)
        return ' '.join(res)

print Solution().toGoatLatin("I speak Goat Latin")
print Solution().toGoatLatin("The quick brown fox jumped over the lazy dog")
