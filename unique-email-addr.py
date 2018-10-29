class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        eh = {}
        for e in emails:
            ln,dn = e.split('@')
            s = ''
            for v in ln:
                if v == '.': continue
                if v == '+': break
                s += v 
            if s: eh.setdefault(s+'@'+dn,0)
        return len(eh)

print Solution().numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"])
