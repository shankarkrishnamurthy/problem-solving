class Solution:
    def shiftingLetters(self, s, sh):
        da, aa = [0]*(len(s)+1), [chr(ord('a') + i) for i in range(26)]
        ah, res = {chr(ord('a') + i):i for i in range(26)}, []
        #print('aa', aa, '\n', 'ah', ah)
        for a,b,c in sh:
            if c == 0: da[a], da[b+1] = da[a] - 1, da[b+1] + 1
            else: da[a], da[b+1] = da[a] + 1, da[b+1] - 1
        for i in range(1, len(da)): 
            da[i] += da[i-1]
        #print('da', da)
        for i in range(len(s)):
            j = (ah[s[i]] + da[i]) % 26
            res.append(aa[j])
        #print(res)       
        return ''.join(res)
