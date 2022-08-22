class Solution:
    def largestPalindromic(self, num):
        z, dh, res, fodd = 0, defaultdict(int), "", ""
        for i in num:
            if i == "0": z+=1
            else: dh[i] += 1
        for d in sorted(dh, reverse=True):
            if dh[d] % 2 == 1 and len(fodd) == 0: fodd = d
            res += d*(dh[d]//2)
            #print('d', d, 'dh', dh[d], 'res', res)
        if z % 2 == 1: fodd = "0" if len(fodd)==0 else fodd
        if len(res) == 0: return fodd if len(fodd) != 0 else "0"
        res += (z//2)*"0"
        return res + fodd + res[::-1]
