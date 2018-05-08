class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        helper=[0]*26
        for x in tasks:
            helper[ord(x)-65]+=1
        helper.sort(reverse=True)
        ans=helper[0]*(n+1)-n
        for i in range(1,len(helper)):
            if helper[i]==helper[0]:
                ans+=1
            else:
                break
        return max(ans,sum(helper))      

print Solution().leastInterval(['A','A','A','A','B','B','B','C','C','C'],1)
