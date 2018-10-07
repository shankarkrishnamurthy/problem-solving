class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        ban = set(banned)
        dh,p = {},''
        for i in paragraph:
            if i == '!' or i == '?' or i=="'" or i==',' or i==';' or i =='.':
                i=' '
            p += i.lower()
        wl = p.split(' ')
        ans = 0
        for w in wl: 
            if w in ban or not w: continue
            dh[w] = dh.setdefault(w, 0) + 1
            if dh[w] > ans:
                res = w
                ans = dh[w]
        return res
                

print Solution().mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.",['hit'])
print Solution().mostCommonWord("a,a,a,a,b,b,b , c, c",['a'])
