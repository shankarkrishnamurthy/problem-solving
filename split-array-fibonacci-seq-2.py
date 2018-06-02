class Solution(object):
    def splitIntoFibonacci(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        def checkFib(res,val):
            if len(res) <=1 : return True
            v1 = res[-2]
            v2 = res[-1]
            if v1 != (v2 + val): return False
            return True

        def K_Partition(n,C):
            #print n,C,res
            if C == 0:
                if n > 10: return False
                if len(V[:n+1]) > 1 and V[0] == '0': return False
                val = int(''.join(V[:n+1]))
                if val > 2**31-1: return False
                if not checkFib(res,val): return False
                res.append(val)
                return True

            for i in range(n,C-1,-1):
                if n-i > 10: break
                if len(V[i:n+1]) > 1 and V[i] == '0': continue
                val = int(''.join(V[i:n+1]))
                if val > 2**31-1: break
                if not checkFib(res,val): continue
                res.append(val)
                rc = K_Partition(i-1,C-1)
                if rc: return rc
                res.pop(-1)
            return False
            
        V = list(S)
        #print "Input: ", V
        for i in range(2, len(V)):
            res=[] 
            #print "Partition ", i
            rc = K_Partition(len(V)-1, i)
            if rc: 
                return res[::-1]
        return []


print Solution().splitIntoFibonacci("26680333094522122405874374286875202793245124106023438638154307674529081118998476463547521258509819378850611547943714168887018710248914570324093142954155261448272417373604331561828074147927642892139798")
#print Solution().splitIntoFibonacci("502113822114324228146342470570616913086148370223967883880490627727810157768164350462659281443027860696206741126485341822692082949177424771869507721046921249291642202139633432706879765292084310")
"""
print Solution().splitIntoFibonacci("107374182410737418232147483647")
print Solution().splitIntoFibonacci("214748364721474836422147483641")
print Solution().splitIntoFibonacci("11235813")
print Solution().splitIntoFibonacci("123456579")
print Solution().splitIntoFibonacci("101")
print Solution().splitIntoFibonacci("1011")
print Solution().splitIntoFibonacci("12315")
print Solution().splitIntoFibonacci("112358130")
print Solution().splitIntoFibonacci("0123")
print Solution().splitIntoFibonacci("1101111")
print Solution().splitIntoFibonacci("68142236")
"""
