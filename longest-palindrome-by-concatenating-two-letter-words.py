class Solution:
    def longestPalindrome(self, words):
        hw,msf,mid,ext = {},0,set(),0
        for w in words:
            hw[w] = hw.get(w,0) + 1
            if w[0] != w[1]: 
                pw = w[1]+w[0]
                if pw in hw and hw[pw] > 0:
                    ext += 2
                    hw[pw] -= 1
                    hw[w] -= 1
            else:
                if hw[w] > 1:
                    hw[w] -= 2
                    ext += 2
                if hw[w] == 0: mid.remove(w)
                else: mid.add(w)
        pal = ext + (1 if len(mid) > 0 else 0)
        return pal*2
