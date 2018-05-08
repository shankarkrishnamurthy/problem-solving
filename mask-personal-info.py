class Solution(object):
    def maskPII(self, S):
        """
        :type S: str
        :rtype: str
        """
        def do_email(S):
            n1,n2 = S.split('@')
            a = n1.lower()
            res = a[0]+'*****'+a[-1]+'@'+n2.lower()
            return res
        def do_phone(S):
            ph=""
            for i in range(len(S)):
                if ord(S[i]) >= ord('0') and ord(S[i]) <= ord('9'):
                    ph += S[i]
            l = len(ph)
            if l ==10: 
                res = '***-***-' + ph[-4:]
            else:
                res = '+'+'*' * (l-10)+'-***-***-' + ph[-4:]
            return res
                
        if '@' in S:
            return do_email(S)
        else:
            return do_phone(S)

print Solution().maskPII("AB@qQ.com")
print Solution().maskPII("1(234)567-890")
print Solution().maskPII("86-(10)12345678")
print Solution().maskPII("+(501321)-50-23431")
