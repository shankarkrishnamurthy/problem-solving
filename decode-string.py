class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        def do_ds(idx):
            k, final = '',''
            while idx < len(s):
                v = s[idx]
                if v.isdigit(): k += v
                if v.isalpha(): final += v
                if v == '[':
                    decstr, idx = do_ds(idx+1)
                    final += int(k) * decstr
                    k = ''
                if v == ']': return (final, idx)
                idx += 1
            return (final, idx)

        #print "Input: ",s
        decstr,i = do_ds(0)
        return decstr

#print Solution().decodeString("2[abc]3[cd]ef")
#print Solution().decodeString("3[a2[c]]")
#print Solution().decodeString("3[a]2[bc]")
print Solution().decodeString("3[a]")
print Solution().decodeString("c0[a]1[b]")
print Solution().decodeString("a")
print Solution().decodeString("")
