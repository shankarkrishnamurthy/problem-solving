class Solution:
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        ll,dl = [],[]
        for l in logs:
            a = l.split()
            if a[1].isdigit():
                dl.append(l)
            else:
                ll.append((a[1:],a[0]))
        ll.sort()
        return [ ' '.join([b]+a) for (a,b) in ll] + dl
        
        
# (["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"])
print Solution().reorderLogFiles(["a1 9 2 3 1","h1 act car","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"])
