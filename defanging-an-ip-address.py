class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        ans = ""
        for i in address:
            if i == '.':
                ans += '[.]'
            else: ans += i
        return ans

print Solution().defangIPaddr("255.100.50.0")
print Solution().defangIPaddr("1.1.1.1")
