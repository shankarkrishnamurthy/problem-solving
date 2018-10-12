class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        dh = {}
        for v in cpdomains:
            c,t = v.split(' ')
            tok = t.split('.')
            for k in xrange(len(tok)):
                ttok = '.'.join(tok[k:])
                dh[ttok] = dh.setdefault(ttok,0) + int(c)
                
        return ["%s %s"%(v,k) for (k,v) in dh.items()]

print Solution().subdomainVisits(["9001 discuss.leetcode.com"])
print Solution().subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"])
