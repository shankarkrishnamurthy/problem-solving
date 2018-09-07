#Go Daddy
class Solution(object):
    def brk_str(self, tok, s):
        if not s:
            return True
        for i in range(1,len(s)+1):
            if s[:i] in tok:
                rc = self.brk_str(tok,s[i:])
                if rc == True: return True
        return False

    def brk_str1(self, tokens,s):
        tok = set()
        for i in tokens:
            tok.add(i)
        print tok
        return self.brk_str(tok,s)
    
if __name__ == "__main__":
    #print Solution().brk_str1(['i','like','play','foot','ball'], 'ilikeplayingfootball')
    print Solution().brk_str1(['i','like','play','foot','ball'], 'ilikeplayfootball')
