class Solution(object):
    def actual(self,S,K):
        b = ''
        for v in S:
            if '1' <= v <= '9': 
                b = b*int(v)
            else:
                b += v
        print '\nactual ans', b, b[K-1]

    def decodeAtIndex(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        #self.actual(S,K)
        ih = {}
        ssf, p = '', 0
        for i,v in enumerate(S):
            if '1' <= v <= '9': 
                n = (p+len(ssf))*int(v)
                ih[n] = (p,ssf)    
                p = n
                ssf = ''
            else: 
                ssf += v
            if K<=p: break
        if len(ssf) > 0:
            n = p+len(ssf)
            ih[n] = (p, ssf)
        while n > 0:
            p,ssf = ih[n]
            r = (K-1) % (p+len(ssf))
            if p<=r<(p+len(ssf)):
                return ssf[r-p]
            n = p
            K = r+1
        
#print Solution().decodeAtIndex("l3a2c23",54)
#print Solution().decodeAtIndex("l3a2c23",53)
#print Solution().decodeAtIndex("l3a2c23",52)
#print Solution().decodeAtIndex("ixm5xmgo78",711)
print Solution().decodeAtIndex("leet2code3ts",38)
print Solution().decodeAtIndex("leet2code3ts",37)
print Solution().decodeAtIndex("leet2code3ts",36)
print Solution().decodeAtIndex("leet2code3",36)
print Solution().decodeAtIndex("leet2code3",35)
print Solution().decodeAtIndex("leet2code3",30)
print Solution().decodeAtIndex("leet2code3",14)
print Solution().decodeAtIndex("leet2code3",13)
print Solution().decodeAtIndex("leet2code3",12)
print Solution().decodeAtIndex("leet2code3",11)
print Solution().decodeAtIndex("leet2code3",10)
print Solution().decodeAtIndex("leet2code3",9)
print Solution().decodeAtIndex("leet2code3",8)
print Solution().decodeAtIndex("leet2code3",7)
print Solution().decodeAtIndex("leet2code3",6)
print Solution().decodeAtIndex("leet2code3",5)
print Solution().decodeAtIndex("leet2code3",4)
print Solution().decodeAtIndex("leet2code3",3)
print Solution().decodeAtIndex("leet2code3",2)
print Solution().decodeAtIndex("leet2code3",1)
print Solution().decodeAtIndex("ha22",8)
print Solution().decodeAtIndex("ha22",7)
print Solution().decodeAtIndex("ha22",6)
print Solution().decodeAtIndex("ha22",5)
print Solution().decodeAtIndex("ha22",4)
print Solution().decodeAtIndex("ha22",3)
print Solution().decodeAtIndex("ha22",2)
print Solution().decodeAtIndex("ha22",1)
#print Solution().decodeAtIndex("a2345678999999999999999",1)
